<!-- LANGUAGE_LINKS_START -->
[🇩🇪 German](README_de.md) | <span style="color: grey;">🇬🇧 English</span>
<!-- LANGUAGE_LINKS_END -->

# Translate-MD: Markdown translation script

<div style="display: flex; align-items: center;">
  <img src="translate-md.png" alt="translate-md" style="width: 64px; margin-right: 10px;">
  <span>The Translate-MD script is used to translate a Markdown document template, such as README.md files, into multiple languages. Coded content such as code blocks, anchors and headings, etc. should be retained during the translation process. <br>
  It uses Google Translator to automatically translate the content while leaving certain sections unchanged. Additionally, it implements language links in all translated files to enable easy navigation between different language versions.
  </span>
</div>

## Table of contents

- [Translate-MD: Markdown translation script](#translate-md-markdown-translation-script)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Install dependencies](#install-dependencies)
      - [Additional Notes](#additional-notes)
    - [Dependency Check](#dependency-checking)
    - [Option 1: Install and run in a virtual environment (recommended)](#option-1-install-and-run-in-a-virtual-environment-recommended)
    - [Option 2: System-wide installation](#option-2-system-wide-installation)
  - [Usage](#use)
    - [Example](#example)
    - [Example of GitHub Actions Integration](#example-of-github-actions-integration)

## Features

- **Automatic language recognition**: The script automatically recognizes the source language from the template.
- **Multilingual translation**: It translates the content into several languages, which can be added to the script under `TARGET_LANGUAGES` or optionally via a json configuration file if necessary.
- **Preserves formatting**: Code blocks, anchors and headings etc. are identified and treated separately to maintain their functionality
- **Language navigation links**: Language links are added or updated in each translated file, allowing the reader to easily switch between different language versions.

## installation

```bash
git clone https://github.com/dbt1/translate-md.git
```

You can run the translation script from a location of your choice or directly where it is after cloning or in the same directory where the Markdown template (default: `template.md`) is located. If you want to run the translation script directly, you must make the script executable by changing the permission.

   ```bash
   chmod +x dateiname.py
   ```
   
### Install dependencies

This script requires `googletrans` for translation:

Installation: 
  
  ```bash
  pip install googletrans==3.1.0a0
  ```

  **Note:** Version >= 4 appears to be unstable or cause problems. Therefore version `3.1.0a0` is recommended.

#### Additional notes

- **Alternative installation of googletrans from GitHub repository**:

  If you encounter any problems, you can install `googletrans` directly from GitHub:

  ```bash
  pip install git+https://github.com/ssut/py-googletrans.git
  ```

### Dependency checking

  After installing the dependencies, you can check whether the required modules were installed correctly:

  ```bash
  python3 -c "from googletrans import Translator; print('Installation erfolgreich')"
  ```

### Option 1: Install and run in a virtual environment (recommended)

1. **Creating a virtual environment, enabling and installing `googletrans`**:

   ```bash
   python3 -m venv venv && source venv/bin/activate && pip install googletrans==3.1.0a0 && pip install --upgrade setuptools
   ```
   > **Note:** The latest stable version of `googletrans` may cause issues. The `3.1.0a0` version is generally more stable and works better.

2. **Make script executable** (only for Unix-based systems, optional):

   ```bash
   chmod +x translate-md.py
   ```

3. **Run script**:

   ```bash
   python3 translate-md.py
   ```

### Option 2: System-wide installation

If you don't want to use a virtual environment, you can also install the required modules globally:

   ```bash
   pip install googletrans==3.1.0a0
   ```

You can then run the script as usual.

## use

Run the script from the command line by specifying the Markdown template file with the `-t` argument. If no argument is given, the script defaults to `template.md` from the current directory and the translations are also created in the same directory. The script can be used locally or for automated translation, e.g. via a workflow of a Git repository like GitHub, for example by calling it accordingly via commit processes. It could also be used in a similar way via Git hooks, depending on how it is integrated.

### Example

   ```bash
   python translate-md.py -t template.md
   ```

### Example of GitHub Actions integration

The translation script can also be used in GitHub Actions, for example to automatically translate a README file on certain events (e.g. after a commit to the main branch).
  
**Note about GitHub Actions permissions**: In order for the GitHub Actions workflow to have the necessary permissions to push changes to the repository, you may need to set up an `Personal Access Token (PAT)`. This token is needed to ensure authentication, especially when pushing to a repository. For more information about setting up an `PAT`, see the [GitHub token configuration documentation](https://docs.github.com/en/enterprise-server@3.1/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Here is an example of an `YAML-Datei` that needs to be created under `.github/workflows/`. This workflow directory must be created and pushed if it does not already exist.
Here it is assumed that you want to translate a README.md, which is usually located in the root directory of a repo.
This example specifies a template saved at `./templates/README_de.md`. Specifically, in this case it is assumed that adjustments will only be made to this template on a regular basis. As you may notice, this is actually the name of a target file, but that's not a problem since this file is not in the same directory as the target file.

`[ci skip]` is appended to the final commit. This is to prevent the commit from triggering the workflow again if it is not desired. This could save unnecessary resources and avoid loops: 

```yaml
name: Translate README

on:
  push:
    branches:
      - main

jobs:
  translate-readme:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        pip install googletrans==3.1.0a0

    - name: Run translation script
      run: |
        python translate-md.py --template-md ./templates/README_de.md --output-dir . --prefix README_ --main-doc README.md

    - name: Commit changes
      run: |
        git config --global user.name 'github-actions'
        git config --global user.email 'github-actions@github.com'
        git add .
        git commit -m 'README: Automated translation update [ci skip]'
        git push
```

  **Note:** It makes sense to test a workflow locally. Further information about this [here](https://github.com/nektos/act)!
