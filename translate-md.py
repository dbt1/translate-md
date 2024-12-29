#!/usr/bin/env python3
"""
Markdown File Translation Script

This script translates a Markdown template file into multiple languages, handling specific placeholders
and ensuring that important content like code blocks, anchors, headers, URLs, images, HTML elements,
inline code, LaTeX formulas, and table separator lines are preserved throughout the translation process.

It uses Google Translate to automatically translate content while keeping specific sections intact.
It also updates language links in all translated markdown files to allow easy navigation between different
language versions.

Features:
- Detects the source language automatically or allows specifying it via a command-line argument.
- Translates the content into specified target languages.
- Handles placeholders for code blocks, anchors, headers, URLs, images, HTML elements, inline code,
  LaTeX formulas, and table separator lines to ensure the consistency of formatting.
- Updates or adds language links to navigate between different language versions (unless disabled).
- Allows specifying the output directory, file prefix, main document file name, configuration file, and
  an option to disable language links.
- Optionally prevents the insertion of language links into the target files and skips the creation
  of the main document file when language links are disabled.

Usage:
- Run the script from the command line, specifying the Markdown template file using the `-t` argument.
- Optionally, specify the output directory with `-o`, the file prefix with `-p`, the main document file name
  with `-m`, and the configuration file with `-c`.
- Use the `--no-language-links` or `-n` option to prevent the insertion of language links and skip the creation
  of the main document file.
- Use the `-s` or `--source-lang` option to specify the source language code (e.g., 'de' for German).
- Example: `python translate_readme.py -t template.md -o translated_readmes -p DOC_ -s de -n -c config.json`
- Use also argument `--help` or take a look at the README file.

Dependencies:
- googletrans (to install: `pip install googletrans==3.1.0a0`)
  **NOTE:** Version >= 4 may not work stably or may cause problems!

License:
- GPL2

Author:
- (C) Thilo Graf 2024
"""

import os
import re
import sys
import json
import logging
import argparse

VERSION_MAJOR = "1"
VERSION_MINOR = "2"
VERSION_PATCH = "11"
VERSION = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"

GOOGLETRANS_VERSION = "3.1.0a0"

try:
    from importlib.metadata import version as get_version, PackageNotFoundError  # Python 3.8+
except ImportError:
    from importlib_metadata import version as get_version, PackageNotFoundError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

TARGET_LANGUAGES = {}

def check_googletrans_version(required_version=GOOGLETRANS_VERSION):
    """
    Checks if the installed version of googletrans matches the required version.
    """
    try:
        installed_version = get_version('googletrans')
        if installed_version != required_version:
            logging.warning(
                f"Warning: Installed googletrans version is {installed_version}, "
                f"but {required_version} is required. "
                f"Please install with 'pip install googletrans=={required_version}'."
            )
    except PackageNotFoundError:
        logging.error(
            "The module 'googletrans' is not installed. "
            f"Install it with 'pip install googletrans=={GOOGLETRANS_VERSION}'."
        )
        sys.exit(1)

# Ensure googletrans is installed in the correct version
check_googletrans_version(GOOGLETRANS_VERSION)

try:
    from googletrans import Translator, LANGUAGES
except ImportError:
    logging.error(
        "The module 'googletrans' is not installed. "
        f"Install it with 'pip install googletrans=={GOOGLETRANS_VERSION}'."
    )
    sys.exit(1)

# Default target languages with flag emojis
DEFAULT_TARGET_LANGUAGES = {
    'en': ('English', '🇬🇧'),  # default language
}

# Various placeholders
CODE_PLACEHOLDER = "@CODE_BLOCK_{}@"
ANCHOR_PLACEHOLDER = "@ANCHOR_{}@"
HEADER_PLACEHOLDER = "@HEADER_PLACEHOLDER_{}@"
URL_PLACEHOLDER = "@URL_PLACEHOLDER_{}@"
IMAGE_PLACEHOLDER = "@IMAGE_{}@"
HTML_PLACEHOLDER = "@HTML_{}@"
INLINE_CODE_PLACEHOLDER = "@INLINE_CODE_{}@"
LATEX_PLACEHOLDER = "@LATEX_{}@"
TABLE_SEPARATOR_PLACEHOLDER = "@TABLE_SEPARATOR_{}@"

# Markers for language links
LANGUAGE_LINKS_START = "<!-- LANGUAGE_LINKS_START -->"
LANGUAGE_LINKS_END = "<!-- LANGUAGE_LINKS_END -->"


def detect_language(text, translator):
    try:
        detection = translator.detect(text)
        return detection.lang.lower()
    except Exception as e:
        logging.exception(f"Error during language detection: {e}")
        sys.exit(1)

def load_template(template_file, target_filenames):
    if not os.path.exists(template_file):
        logging.error(f"Error: The template file '{template_file}' was not found.")
        sys.exit(1)
    if os.path.getsize(template_file) == 0:
        logging.error(f"Error: The template file '{template_file}' is empty.")
        sys.exit(1)
    if not template_file.lower().endswith('.md'):
        logging.error(f"Error: The template file '{template_file}' is not a Markdown file.")
        sys.exit(1)
    if os.path.abspath(template_file) in [os.path.abspath(f) for f in target_filenames]:
        logging.error("Error: The template file must not have the same name as any of the target files.")
        sys.exit(1)
    try:
        with open(template_file, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        logging.exception(f"Error reading the template file '{template_file}': {e}")
        sys.exit(1)

def extract_placeholders(content):
    code_blocks = []
    anchor_placeholders = {}
    headers = []
    url_placeholders = {}
    images = []
    html_elements = []
    inline_codes = []
    latex_formulas = []
    table_separators = []

    def replace_code_block(match):
        code_block = match.group(0)
        code_blocks.append(code_block)
        index = len(code_blocks) - 1
        return CODE_PLACEHOLDER.format(index)

    content = re.sub(r'```[\s\S]*?```', replace_code_block, content, flags=re.DOTALL)

    def replace_inline_code(match):
        inline_code = match.group(0)
        inline_codes.append(inline_code)
        index = len(inline_codes) - 1
        return INLINE_CODE_PLACEHOLDER.format(index)

    content = re.sub(r'`[^`]+`', replace_inline_code, content)

    def replace_latex(match):
        latex = match.group(0)
        latex_formulas.append(latex)
        index = len(latex_formulas) - 1
        return LATEX_PLACEHOLDER.format(index)

    content = re.sub(r'\$\$[\s\S]*?\$\$|\$[^$]+\$', replace_latex, content, flags=re.DOTALL)

    def replace_image(match):
        image = match.group(0)
        images.append(image)
        index = len(images) - 1
        return IMAGE_PLACEHOLDER.format(index)

    content = re.sub(r'!\[.*?\]\(.*?\)', replace_image, content)

    def replace_url(match):
        url = match.group(1)
        index = len(url_placeholders)
        placeholder = URL_PLACEHOLDER.format(index)
        url_placeholders[placeholder] = url
        return f"({placeholder})"

    content = re.sub(r'\((https?://[^\s)]+)\)', replace_url, content)

    def replace_html(match):
        html_element = match.group(0)
        html_elements.append(html_element)
        index = len(html_elements) - 1
        return HTML_PLACEHOLDER.format(index)

    content = re.sub(r'<[^>]+>', replace_html, content)

    def replace_anchor(match):
        anchor = match.group(1)
        index = len(anchor_placeholders)
        placeholder = ANCHOR_PLACEHOLDER.format(index)
        anchor_placeholders[placeholder] = anchor
        return f"({placeholder})"

    content = re.sub(r'\(#([^)]+)\)', replace_anchor, content)

    def replace_header(match):
        header_marks = match.group(1)
        header_text = match.group(2)
        header_level = len(header_marks)
        headers.append((header_level, header_text))
        return HEADER_PLACEHOLDER.format(len(headers)-1)

    content = re.sub(r'^(#+)\s+(.*)', replace_header, content, flags=re.MULTILINE)

    def replace_table_separator_line(match):
        separator_line = match.group(0)
        table_separators.append(separator_line)
        index = len(table_separators) - 1
        return TABLE_SEPARATOR_PLACEHOLDER.format(index)

    content = re.sub(
        r'^\s*\|[:\-]+\|(?:[:\-]+\|)+\s*$',
        replace_table_separator_line,
        content,
        flags=re.MULTILINE
    )

    return (
        content,
        code_blocks,
        anchor_placeholders,
        headers,
        url_placeholders,
        images,
        html_elements,
        inline_codes,
        latex_formulas,
        table_separators
    )

def generate_anchor(text):
    anchor = re.sub(r'[^\w\s-]', '', text).strip().lower()
    anchor = re.sub(r'[\s]+', '-', anchor)
    return anchor

def translate_section(translator, section_text, src_lang, dest_lang):
    if not section_text.strip():
        return section_text
    try:
        return translator.translate(section_text, src=src_lang, dest=dest_lang).text
    except Exception as e:
        logging.exception(f"Error during translation to '{dest_lang}': {e}")
        sys.exit(1)

def translate_content_in_chunks(content, translator, src_lang, dest_lang):
    if src_lang == dest_lang:
        return content
    parts = re.split(r'(' + HEADER_PLACEHOLDER.replace("{}", r'\d+') + r')', content)

    translated_parts = []
    for part in parts:
        if re.match(HEADER_PLACEHOLDER.replace("{}", r'\d+'), part):
            translated_parts.append(part)
        else:
            translated_parts.append(translate_section(translator, part, src_lang, dest_lang))

    return "".join(translated_parts)

def restore_placeholders(
    translated_content,
    code_blocks,
    anchor_placeholders,
    headers,
    url_placeholders,
    images,
    html_elements,
    inline_codes,
    latex_formulas,
    table_separators,
    translator,
    src_lang,
    dest_lang
):
    new_anchors = {}
    for i, (header_level, header_text) in enumerate(headers):
        placeholder = HEADER_PLACEHOLDER.format(i)
        try:
            if src_lang != dest_lang:
                h_tr = translator.translate(header_text, src=src_lang, dest=dest_lang)
                translated_header_text = h_tr.text.strip()
            else:
                translated_header_text = header_text.strip()
        except Exception as e:
            logging.exception(f"Error translating header '{header_text}': {e}")
            translated_header_text = header_text

        reconstructed_header = f"{'#' * header_level} {translated_header_text}"
        new_anchor = generate_anchor(translated_header_text)
        new_anchors[placeholder] = (reconstructed_header, new_anchor)

    # 1) Replace header placeholders with line breaks before/after
    for placeholder, (full_header_line, _) in new_anchors.items():
        translated_content = translated_content.replace(placeholder, f"\n{full_header_line}\n")

    # 2) Replace anchor placeholders
    for placeholder, original_anchor in anchor_placeholders.items():
        header_index = None
        for idx, (lvl, txt) in enumerate(headers):
            if generate_anchor(txt) == original_anchor:
                header_index = idx
                break
        if header_index is not None:
            new_anchor = new_anchors[HEADER_PLACEHOLDER.format(header_index)][1]
        else:
            new_anchor = original_anchor
        translated_content = translated_content.replace(placeholder, f"#{new_anchor}")

    # 3) Table separators
    for i, separator_line in enumerate(table_separators):
        placeholder = TABLE_SEPARATOR_PLACEHOLDER.format(i)
        translated_content = translated_content.replace(placeholder, separator_line)

    # 4) Code blocks
    for i, code_block in enumerate(code_blocks):
        placeholder = CODE_PLACEHOLDER.format(i)
        translated_content = translated_content.replace(placeholder, code_block)

    # 5) URLs
    for placeholder, url in url_placeholders.items():
        translated_content = translated_content.replace(placeholder, url)

    # 6) Images
    for i, image in enumerate(images):
        placeholder = IMAGE_PLACEHOLDER.format(i)
        translated_content = translated_content.replace(placeholder, image)

    # 7) HTML elements
    for i, html_element in enumerate(html_elements):
        placeholder = HTML_PLACEHOLDER.format(i)
        translated_content = translated_content.replace(placeholder, html_element)

    # 8) Inline code
    for i, inline_code in enumerate(inline_codes):
        placeholder = INLINE_CODE_PLACEHOLDER.format(i)
        translated_content = translated_content.replace(placeholder, inline_code)

    # 9) LaTeX
    for i, latex in enumerate(latex_formulas):
        placeholder = LATEX_PLACEHOLDER.format(i)
        translated_content = translated_content.replace(placeholder, latex)

    # 10) Remove extra spaces in links
    translated_content = re.sub(r'\]\s*\(', '](', translated_content)

    # **NEUER SCHRITT**: Sicherstellen, dass nach jeder Zeile mit "</div>" eine Leerzeile folgt.
    # Falls z.B. steht: </div>\n## Table of contents => wir wollen \n\n## Table of contents
    translated_content = re.sub(
        r'(</div>)([ \t]*)\n(?!\n)',
        r'\1\n\n',
        translated_content
    )

    # 11) Ensure at least one blank line after each heading
    translated_content = re.sub(
        r'^(#+\s[^\n]+)\n(?!\n)',
        r'\1\n\n',
        translated_content,
        flags=re.MULTILINE
    )

    # 12) Reduce triple+ newlines to double
    translated_content = re.sub(r'\n{3,}', '\n\n', translated_content)

    # 13) Remove trailing spaces on each line
    lines = [ln.rstrip() for ln in translated_content.splitlines()]
    translated_content = "\n".join(lines)

    return translated_content

def is_filename_in_namespace(main_doc, prefix):
    main_base = os.path.splitext(main_doc)[0].lower()
    if prefix.endswith('_'):
        expected_base = prefix[:-1].lower()
    else:
        expected_base = prefix.lower()
    if main_base == expected_base or main_base.startswith(expected_base + '_'):
        return True
    else:
        return False

def add_or_update_language_links(content, translated_files, main_doc, prefix, current_lang_code=None):
    language_links = []
    for code, (lang_name, flag) in sorted(TARGET_LANGUAGES.items()):
        if code == current_lang_code:
            link = f"<span style=\"color: grey;\">{flag} {lang_name}</span>"
        else:
            link = f"[{flag} {lang_name}]({translated_files[code]})"
        language_links.append(link)

    language_links_block = f"{LANGUAGE_LINKS_START}\n{' | '.join(language_links)}\n{LANGUAGE_LINKS_END}"

    if LANGUAGE_LINKS_START in content and LANGUAGE_LINKS_END in content:
        pattern = re.compile(
            f"{re.escape(LANGUAGE_LINKS_START)}.*?{re.escape(LANGUAGE_LINKS_END)}",
            re.DOTALL
        )
        content = pattern.sub(language_links_block, content)
    else:
        content = f"{language_links_block}\n\n{content}"

    return content

def create_main_doc(output_dir, main_doc, translated_files, prefix):
    main_output_file = os.path.join(output_dir, main_doc)
    logging.info(f"Creating/updating main document at '{main_output_file}'")

    language_links = []
    for code, (lang_name, flag) in sorted(TARGET_LANGUAGES.items()):
        link = f"[{flag} {lang_name}]({translated_files[code]})"
        language_links.append(link)

    language_links_block = f"{LANGUAGE_LINKS_START}\n{' | '.join(language_links)}\n{LANGUAGE_LINKS_END}"

    main_content = (
        f"# Documentation\n\n"
        f"This document is available in the following languages:\n\n"
        f"{language_links_block}\n\n"
        f"Please choose your preferred language by clicking on the links above."
    )

    try:
        with open(main_output_file, 'w', encoding='utf-8') as file:
            file.write(main_content)
        logging.info(f"Main document saved to '{main_output_file}'")
    except Exception as e:
        logging.exception(f"Error writing to '{main_output_file}': {e}")
        sys.exit(1)

def prepare_target_files(output_dir, translated_files, source_lang_code, source_lang_name):
    for code, filename in translated_files.items():
        tf_path = os.path.join(output_dir, filename)
        content = "<!-- TRANSLATED_CONTENT -->\n"
        try:
            with open(tf_path, 'w', encoding='utf-8') as file:
                file.write(content)
            logging.info(f"Prepared target file '{tf_path}'.")
        except Exception as e:
            logging.exception(f"Error preparing target file '{tf_path}': {e}")
            sys.exit(1)

def insert_translated_content(translated_file_path, translated_content):
    try:
        with open(translated_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        if '<!-- TRANSLATED_CONTENT -->' not in content:
            logging.error(
                f"Placeholder '<!-- TRANSLATED_CONTENT -->' not found in '{translated_file_path}'. "
                "Insertion skipped."
            )
            return

        updated_content = content.replace('<!-- TRANSLATED_CONTENT -->', translated_content)
        with open(translated_file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        logging.info(f"Inserted translated content into '{translated_file_path}'.")
    except Exception as e:
        logging.exception(f"Error inserting translated content into '{translated_file_path}': {e}")

def get_flag_emoji(country_code):
    if len(country_code) != 2:
        return ''
    country_code = country_code.upper()
    try:
        return ''.join(chr(0x1F1E6 + ord(char) - ord('A')) for char in country_code)
    except:
        return ''

def main():
    parser = argparse.ArgumentParser(
        description=f'%(prog)s v{VERSION}, Translates a Markdown template into multiple languages.',
        formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=40, width=100)
    )

    default_template_file = 'template.md'
    default_output_dir = '.'
    default_prefix = 'DOC_'
    default_main_doc = 'DOC.md'
    default_config_file = None

    parser.add_argument('-t', '--template-md',
        metavar='TEMPLATE_FILE',
        default=default_template_file,
        help=f'Path to the template file (default: {default_template_file})'
    )
    parser.add_argument('-o', '--output-dir',
        metavar='OUTPUT_DIR',
        default=default_output_dir,
        help=f'Directory to save the translated files (default: {default_output_dir})'
    )
    parser.add_argument('-p', '--prefix',
        metavar='PREFIX',
        default=default_prefix,
        help=f'Prefix for the translated file names (default: {default_prefix})'
    )
    parser.add_argument('-m', '--main-doc',
        metavar='MAIN_DOC',
        default=default_main_doc,
        help=f'Name of the main document file (default: {default_main_doc})'
    )
    parser.add_argument('-c', '--config-file',
        metavar='CONFIG_FILE',
        default=default_config_file,
        help='Path to configuration file (optional)'
    )
    parser.add_argument('-n', '--no-language-links',
        action='store_true',
        help='Prevent insertion of language links in the target files and skip creation of main document file'
    )
    parser.add_argument('-s', '--source-lang',
        metavar='SOURCE_LANG_CODE',
        default=None,
        help='Source language code (optional). If not provided, the script will detect automatically.'
    )
    parser.add_argument('--version',
        action='version',
        version=f'%(prog)s v{VERSION}'
    )
    args = parser.parse_args()

    config = {}
    if args.config_file:
        if not os.path.exists(args.config_file):
            logging.error(f"Configuration file '{args.config_file}' not found.")
            sys.exit(1)
        try:
            with open(args.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            logging.info(f"Using external configuration file: {os.path.abspath(args.config_file)}")
        except Exception as e:
            logging.exception(f"Error loading configuration file '{args.config_file}': {e}")
            sys.exit(1)

    template_file = config.get('template_md', args.template_md)
    output_dir = config.get('output_dir', args.output_dir)
    prefix = config.get('prefix', args.prefix)
    main_doc = config.get('main_doc', args.main_doc)
    no_language_links = config.get('no_language_links', args.no_language_links)
    target_languages_config = config.get('target_languages', None)
    source_lang_code_arg = config.get('source_lang', args.source_lang)

    global TARGET_LANGUAGES
    if target_languages_config:
        if isinstance(target_languages_config, dict):
            valid = True
            for code, value in target_languages_config.items():
                if not (isinstance(value, (list, tuple))) or len(value) != 2:
                    logging.error(f"Invalid format for language '{code}': {value}. Must be [name, flag].")
                    valid = False
            if not valid:
                logging.error("Invalid 'target_languages' format in configuration. Each language must have a name and a flag.")
                sys.exit(1)
            TARGET_LANGUAGES = target_languages_config
        else:
            logging.error("Invalid format for 'target_languages' in configuration.")
            sys.exit(1)
    else:
        TARGET_LANGUAGES = DEFAULT_TARGET_LANGUAGES

    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            logging.info(f"Created output directory '{output_dir}'.")
        except Exception as e:
            logging.exception(f"Error creating output directory '{output_dir}': {e}")
            sys.exit(1)

    target_filenames = [os.path.join(output_dir, f"{prefix}{code}.md") for code in TARGET_LANGUAGES]

    content = load_template(template_file, target_filenames)
    translator = Translator()

    if source_lang_code_arg:
        source_lang_code = source_lang_code_arg.lower()
        source_lang_name = LANGUAGES.get(source_lang_code, source_lang_code).capitalize()
        logging.info(f"Using specified source language: {source_lang_name} ({source_lang_code})")
    else:
        source_lang_code = detect_language(content, translator)
        source_lang_name = LANGUAGES.get(source_lang_code, source_lang_code).capitalize()
        logging.info(f"Detected source language: {source_lang_name} ({source_lang_code})")

    # If missing, add source lang
    if source_lang_code not in TARGET_LANGUAGES:
        source_lang_flag = get_flag_emoji(source_lang_code)
        TARGET_LANGUAGES[source_lang_code] = (source_lang_name, source_lang_flag)
    else:
        source_lang_name, source_lang_flag = TARGET_LANGUAGES[source_lang_code]

    translated_files = {code: f"{prefix}{code}.md" for code in TARGET_LANGUAGES}

    if os.path.abspath(template_file) in [os.path.abspath(f) for f in target_filenames]:
        logging.error("Error: The template file must not have the same name as any target file.")
        sys.exit(1)

    if not is_filename_in_namespace(main_doc, prefix):
        logging.warning(
            f"The main document file name '{main_doc}' does not start with the namespace '{prefix}'. "
            "Use '-m' or adjust '-p'."
        )

    if not no_language_links:
        create_main_doc(output_dir, main_doc, translated_files, prefix)
    else:
        logging.warning(
            "Language links are disabled; the main document file will not be created. "
            "The '-m' option is ignored with '--no-language-links'."
        )

    prepare_target_files(output_dir, translated_files, source_lang_code, source_lang_name)

    (
        content_placeholder,
        code_blocks,
        anchor_placeholders,
        headers,
        url_placeholders,
        images,
        html_elements,
        inline_codes,
        latex_formulas,
        table_separators
    ) = extract_placeholders(content)

    for dest_lang in TARGET_LANGUAGES:
        tname, tflag = TARGET_LANGUAGES[dest_lang]
        translated_file = os.path.join(output_dir, translated_files[dest_lang])
        logging.info(f"Translating '{template_file}' from {source_lang_name} ({source_lang_code}) to {tname} ({dest_lang})")

        chunked_translated = translate_content_in_chunks(content_placeholder, translator, source_lang_code, dest_lang)

        final_translated = restore_placeholders(
            chunked_translated,
            code_blocks,
            anchor_placeholders,
            headers,
            url_placeholders,
            images,
            html_elements,
            inline_codes,
            latex_formulas,
            table_separators,
            translator,
            src_lang=source_lang_code,
            dest_lang=dest_lang
        )

        if not no_language_links:
            final_translated = add_or_update_language_links(
                final_translated,
                translated_files,
                main_doc,
                prefix,
                current_lang_code=dest_lang
            )
        insert_translated_content(translated_file, final_translated)

    if not no_language_links:
        md_path = os.path.join(output_dir, main_doc)
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                main_content = f.read()
        except Exception as e:
            logging.exception(f"Error reading '{md_path}': {e}")
            sys.exit(1)

        missing_links = []
        for code in TARGET_LANGUAGES:
            check_link = f"[{TARGET_LANGUAGES[code][1]} {TARGET_LANGUAGES[code][0]}]({translated_files[code]})"
            if check_link not in main_content:
                missing_links.append(check_link)

        if missing_links:
            logging.warning(
                f"The main document '{main_doc}' is missing links to these files: {', '.join(missing_links)}. "
                f"Ensure they point to the correct prefix '{prefix}'."
            )

    logging.info("Translation process completed successfully.")

if __name__ == "__main__":
    main()
