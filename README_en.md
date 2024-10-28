<!-- LANGUAGE_LINKS_START -->
[🇩🇪 German](README_de.md) | <span style="color: grey;">🇬🇧 English</span> | [🇪🇸 Spanish](README_es.md) | [🇫🇷 French](README_fr.md) | [🇮🇹 Italian](README_it.md)
<!-- LANGUAGE_LINKS_END -->

# Translate-MD: Markdown translation script

<div style="display: flex; align-items: center;">
  <img src="translate-md.png" alt="translate-md" style="width: 64px; margin-right: 10px;">
  <span>Translate-MD is a Python script and is used to translate files into several languages ​​from a Markdown document template, such as template.md, and to save them in specified target languages. Coded content such as code blocks, anchors and headings should be retained during the translation process. <br>
  It uses Google Translator to automatically translate the content while leaving certain sections unchanged. Additionally, it implements language links in all translated files to enable easy navigation between different language versions.
  </span>
</div>

## Table of contents

- [Translate-MD: Markdown translation script](#translate-md-markdown-translation-script)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Install dependencies](#install-dependencies)
    - [Dependency Check](#dependency-checking)
    - [Option 1: Install and run in a virtual environment (recommended)](#option-1-install-and-run-in-a-virtual-environment-recommended)
    - [Option 2: System-wide installation](#option-2-system-wide-installation)
    - [Alternative installation of googletrans from GitHub repository (not recommended)](#alternative-installation-of-googletrans-from-github-repository-not-recommended)
  - [Usage](#use)
    - [Summary of parameters](#summary-of-parameters)
    - [1. Standard usage with the default parameters](#1-standard-use-with-the-standard-parameters)
    - [2. Specifying a specific template file and an output directory](#2-specifying-a-specific-template-file-and-an-output-directory)
    - [3. Setting a custom file prefix and name for the main document](#3-set-a-custom-file-prefix-and-name-for-the-main-document)
    - [4. Using a configuration file](#4-using-a-configuration-file)
    - [5. Combination of command line parameters and configuration file](#5-combination-of-command-line-parameters-and-configuration-file)
    - [6. How to use voice link disable option](#6-using-the-option-to-disable-voice-links)
    - [7. Combined use of all options](#7-combined-use-of-all-options)
    - [8. View version information](#8-view-version-information)
    - [9. Show help](#9-show-help)
    - [10. Example with language links disabled and using a different prefix](#10-example-with-language-links-disabled-and-using-a-different-prefix)
    - [11. Using the short form of options](#11-use-of-the-short-form-of-options)
  - [GitHub Actions Integration Example](#example-of-github-actions-integration)

## Features

- **Automatic language recognition**: `Translate-MD`automatically recognizes the source language from the template.
- **Multilingual translation**: `Translate-MD`translates the content into several languages, which can be supplemented in the script under `TARGET_LANGUAGES` or optionally via a json configuration file if necessary.
- **Preserves formatting**: Code blocks, anchors and headings are identified and treated separately to preserve their functionality.
- **Language Navigation Links**: A main file with links to other translations as well as links within each translated file will be added or updated to allow the reader to easily switch between different language versions.

## installation

Use `curl` to download the script directly to a location of your choice:

```bash
curl -o translate-md.py https://raw.githubusercontent.com/dbt1/translate-md/master/translate-md.py
```

**or**

Use `git clone` to clone the entire source to a location of your choice:

```bash
git clone https://github.com/dbt1/translate-md.git
```

You can run `Translate-MD` from a location of your choice, either directly where it is after cloning or in the same directory where the Markdown template (default: `template.md`) is located. If `Translate-MD` is to be executed directly, the script must be made executable by changing the permission depending on the system.

```bash
chmod +x dateiname.py
```

### Install dependencies

If not already available, `Translate-MD` still requires **googletrans 3.1.0a0**:

   > **Note:** The latest "stable" version of `googletrans` may cause problems. The `3.1.0a0` version is usually more stable and works better.

### Dependency checking

This is how you can check whether the required modules have been installed correctly:

```bash
python3 -c "from googletrans import Translator; print('Installation erfolgreich')"
```

### Option 1: Install and run in a virtual environment (recommended)

To do this, change to the directory from where you want to execute `Translate-MD`!

Create a virtual environment, activate and install `googletrans`:

   ```bash
   python3 -m venv venv && source venv/bin/activate && pip install googletrans==3.1.0a0 && pip install --upgrade setuptools
   ```


### Option 2: System-wide installation

If you don't want to use a virtual environment and your system allows it, which is not always the case with Ubuntu or Debian, for example, you can also install the required modules globally:

```bash
pip install googletrans==3.1.0a0
```

### Alternative installation of googletrans from GitHub repository (not recommended)

  If you encounter problems, you can try installing `googletrans` directly from GitHub:

  ```bash
  pip install git+https://github.com/ssut/py-googletrans.git
  ```

You can then run `Translate-MD` as usual.

## use

Here are several examples of how you can use the script with all possible parameters:

---

### Summary of parameters

| Kurzform | Langform              | Beschreibung                                                                           | Standardwert                           |
|----------|-----------------------|-----------------------------------------------------------------------------------------|----------------------------------------|
| @INLINE_CODE_15@     | @INLINE_CODE_16@       | Pfad zur Template-Datei Standard:                                                       | @INLINE_CODE_17@ (im aktuellen Verzeichnis) |
| @INLINE_CODE_18@     | @INLINE_CODE_19@        | Verzeichnis, in dem die übersetzten Dateien gespeichert werden sollen                   | @INLINE_CODE_20@ (aktuelles Verzeichnis)            |
| @INLINE_CODE_21@     | @INLINE_CODE_22@            | Präfix für die Namen der übersetzten Dateien                                             | @INLINE_CODE_23@                                 |
| @INLINE_CODE_24@     | @INLINE_CODE_25@          | Name der Hauptdokument-Datei                                                              | @INLINE_CODE_26@                               |
| @INLINE_CODE_27@     | @INLINE_CODE_28@       | Pfad zur Konfigurationsdatei (optional)                                                  | @INLINE_CODE_29@                                 |
| @INLINE_CODE_30@     | @INLINE_CODE_31@ | Verhindert das Einfügen von Sprachlinks und überspringt die Erstellung der Hauptdokument-Datei | @INLINE_CODE_32@ (Sprachlinks aktiviert)        |
| @INLINE_CODE_33@     | @INLINE_CODE_34@       | Quellsprache (optional)                                                                 | @INLINE_CODE_35@ (automatisch)        |
| @INLINE_CODE_36@     | @INLINE_CODE_37@           | Zeigt die Version des Skripts an und beendet die Ausführung                            |                                        |
| @INLINE_CODE_38@     | @INLINE_CODE_39@              | Zeigt die Hilfsnachricht mit allen verfügbaren Optionen an                              |                                        |

---

The following examples should help you use the script flexibly and according to your needs.

### 1. Standard use with the standard parameters

```bash
python translate-md.py
```

**Description:**
- **Template file:** `template.md` must already exist in the same directory as `translate-md.py`!
- **Output directory:** current directory (`.`)
- **File prefix:** `DOC_`
- **Main document:** `DOC.md`
- **Configuration file:** Not used
- **Language Links:** Enabled

---

### 2. Specifying a specific template file and an output directory

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations
```

**Description:**
- **Template file:** `path/to/my_template.md`
- **Output directory:** `path/to/translations`
- **Other parameters:** Default values
- **Language Links:** Enabled

---

### 3. Set a custom file prefix and name for the main document

```bash
python translate-md.py -p README_ -m main_README.md
```

**Description:**
- **File prefix:** `README_`
- **Main document:** `main_README.md`
- **Other parameters:** Default values
- **Language Links:** Enabled

---

### 4. Using a configuration file

**Parameter formatting:**
In the configuration file, the parameters must be specified as key-value pairs. All keys (the `config-file` key doesn't really make sense ;)) correspond to the long names of the command line parameters without `--` at the beginning. For example:

- `template_md` corresponds to `--template-md`
- `output_dir` corresponds to `--output-dir`
- `prefix` corresponds to `--prefix`
- `main_doc` corresponds to `--main-doc`
- `no_language_links` corresponds to `--no-language-links`

Suppose you have an `config.json` with the following content:

```json
{
    "template_md": "path/to/my_template.md",
    "output_dir": "path/to/translations",
    "prefix": "README_",
    "main_doc": "main_README.md",
    "no_language_links": false,
    "target_languages": {
        "de": ["Deutsch", "🇩🇪"],
        "en": ["English", "🇬🇧"],
        "fr": ["Français", "🇫🇷"]
    }
}
```

**Command:**

```bash
python translate-md.py -c path/to/config.json
```

**Description:**
- **Parameters:** Are taken from the `config.json`. All other parameters not entered use default settings.

   > **Note:** The default `target_languages` can only be used via the configuration file, otherwise only `de` and `en` are used.


### 5. Combination of command line parameters and configuration file

If the configuration file does not have a parameter defined, you can apply it as usual with command line parameters.

   > **Note:** The settings in the configuration file take precedence, which means that command line parameters are ignored if they have already been entered in the configuration file.

**Command:**

```bash
python translate-md.py -c config.json -p DOC_ -n
```

**Description:**
- **Template file, output directory, main document:** From the `config.json`
- **File prefix:** Overwrites the value defined in the `config.json` and sets to `DOC_`
- **Language Links:** Disabled (`-n` or `--no-language-links`)

---

### 6. Using the option to disable voice links

```bash
python translate-md.py -n
```

**Description:**
- **Language Links:** Disabled
- **Main Document:** Not created
- **Other parameters:** Default values
- **Warning message:** The script issues a warning that the `-m` option will be ignored.

---

### 7. Combined use of all options

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations -p README_ -m main_README.md -c config.json --no-language-links
```

**Description:**
- **Template file:** `path/to/my_template.md` (from command line)
- **Output directory:** `path/to/translations` (from command line)
- **File prefix:** `README_` (from command line)
- **Main document:** `main_README.md` (from command line, but is ignored)
- **Configuration file:** `config.json` (may contain additional settings)
- **Language Links:** Disabled (`--no-language-links`)
- **Warning message:** The script warns that the `-m` option will be ignored.

---

### 8. View version information

```bash
python translate-md.py --version
```

**Description:**
- **Function:** Displays the version of the script and stops execution.

---

### 9. Show help

```bash
python translate-md.py --help
```

**Description:**
- **Function:** Displays a help message with all available options and their descriptions.

---

### 10. Example with language links disabled and using a different prefix

```bash
python translate-md.py -p LANG_ -n
```

**Description:**
- **File prefix:** `LANG_`
- **Language Links:** Disabled
- **Main Document:** Not created
- **Other parameters:** Default values

---

### 11. Use of the short form of options

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations -p DOC_ -m main_README.md -c config.json -n
```

**Description:**
- **Short options:** `-t`, `-o`, `-p`, `-m`, `-c`, `-n`
- **Functionality:** Equivalent to using all long options combined.


## Example of GitHub Actions integration

`Translate-MD` can also be used in GitHub Actions, for example, to automatically translate a README file during certain events (e.g. after a push to the master branch).
  
> **Note about GitHub Actions permissions**: In order for the GitHub Actions workflow to have the necessary permissions to push changes to the repository, you may need to set up an `Personal Access Token (PAT)` in your account. This token is needed to ensure authentication, especially if you need write permissions to push to your repositories. For more information about setting up an `PAT`, see the [GitHub token configuration documentation](https://docs.github.com/en/enterprise-server@3.1/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Here is an example of an `YAML-Datei` that needs to be created and pushed under `.github/workflows/` if it doesn't already exist.

The assumption here is that you want to create localized README.md files that are located in the root directory of your repo.
This example uses a template file `template.md` that has already been saved in the root directory of your repository. The translations are also output to the root directory `.`. In this case, it is assumed that adjustments are made to this template and that the push checks whether changes have been made to this file. If this is the case, this workflow is triggered, which is specified in the `on` section under `push`. The branch `master` and the template `template.md` are monitored. It is important that write permissions are activated, which must be entered under the `permissions` section. Further entries ensure that the necessary environment is set up with some dependencies in order to ultimately push the changes into the repo.

`[ci skip]` is appended to the final commit. This is to prevent the commit from triggering the workflow again if it is not desired. This could save unnecessary resources and avoid loops. 


  **Note:** It makes sense to test a workflow locally. Further information about this [here](https://github.com/nektos/act)!

```yaml
name: Translate README

on:
  push:
    branches:
      - master
    paths:
      - 'template.md'

permissions:
  contents: write

jobs:
  translate:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.x

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install --upgrade googletrans==3.1.0a0

    - name: Translate README
      run: |
        python translate-md.py --template-md template.md --output-dir . --prefix README_ --main-doc README.md --source-lang de

    - name: Commit and push translated README
      run: |
        git config --global user.email "actions@github.com"
        git config --global user.name "GitHub Actions"
        git add -A
        git commit -m 'README: Automated translation update [ci skip]'
        git push
```
