<!-- LANGUAGE_LINKS_START -->
[🇩🇪 German](README_de.md) | [🇬🇧 English](README_en.md) | [🇪🇸 Spanish](README_es.md) | <span style="color: grey;">🇫🇷 French</span> | [🇮🇹 Italian](README_it.md)
<!-- LANGUAGE_LINKS_END -->

# Translate-MD : script de traduction Markdown

<div style="display: flex; align-items: center;">
  <img src="translate-md.png" alt="translate-md" style="width: 64px; margin-right: 10px;">
  <span>Translate-MD est un script Python utilisé pour traduire des fichiers dans plusieurs langues à partir d'un modèle de document Markdown, tel que template.md, et pour les enregistrer dans des langues cibles spécifiées. Le contenu codé tel que les blocs de code, les ancres et les titres doit être conservé pendant le processus de traduction. <br>
  Il utilise Google Translator pour traduire automatiquement le contenu tout en laissant certaines sections inchangées. De plus, il implémente des liens linguistiques dans tous les fichiers traduits pour permettre une navigation facile entre les différentes versions linguistiques.
  </span>
</div>

## Table des matières

- [Translate-MD : script de traduction Markdown](#translate-md-script-de-traduction-markdown)
  - [Table des matières](#table-des-matières)
  - [Fonctionnalités](#caractéristiques)
  - [Installation](#installation)
    - [Installer les dépendances](#installer-les-dépendances)
    - [Contrôle des dépendances](#vérification-des-dépendances)
    - [Option 1 : Installer et exécuter dans un environnement virtuel (recommandé)](#option-1-installer-et-exécuter-dans-un-environnement-virtuel-recommandé)
    - [Option 2 : Installation à l'échelle du système](#option-2-installation-à-léchelle-du-système)
    - [Installation alternative de googletrans à partir du référentiel GitHub (non recommandé)](#installation-alternative-de-googletrans-à-partir-du-référentiel-github-non-recommandé)
  - [Utilisation](#utiliser)
    - [Résumé des paramètres](#résumé-des-paramètres)
    - [1. Utilisation standard avec les paramètres par défaut](#1-utilisation-standard-avec-les-paramètres-standards)
    - [2. Spécification d'un fichier modèle spécifique et d'un répertoire de sortie](#2-spécification-dun-fichier-modèle-spécifique-et-dun-répertoire-de-sortie)
    - [3. Définition d'un préfixe et d'un nom de fichier personnalisés pour le document principal](#3-définissez-un-préfixe-et-un-nom-de-fichier-personnalisés-pour-le-document-principal)
    - [4. Utilisation d'un fichier de configuration](#4-utilisation-dun-fichier-de-configuration)
    - [5. Combinaison de paramètres de ligne de commande et de fichier de configuration](#5-combinaison-de-paramètres-de-ligne-de-commande-et-de-fichier-de-configuration)
    - [6. Comment utiliser l'option de désactivation du lien vocal](#6-utilisation-de-loption-pour-désactiver-les-liens-vocaux)
    - [7. Utilisation combinée de toutes les options](#7-utilisation-combinée-de-toutes-les-options)
    - [8. Afficher les informations sur la version](#8-afficher-les-informations-sur-la-version)
    - [9. Afficher l'aide](#9-afficher-laide)
    - [10. Exemple avec les liens linguistiques désactivés et utilisant un préfixe différent](#10-exemple-avec-des-liens-linguistiques-désactivés-et-utilisant-un-préfixe-différent)
    - [11. Utiliser la forme courte des options](#11-utilisation-de-la-forme-abrégée-des-options)
  - [Exemple d'intégration d'actions GitHub](#exemple-dintégration-de-github-actions)

## Caractéristiques

- **Reconnaissance automatique de la langue** : `Translate-MD`reconnaît automatiquement la langue source du modèle.
- **Traduction multilingue** : `Translate-MD`traduit le contenu en plusieurs langues, qui peut être complété dans le script sous `TARGET_LANGUAGES` ou éventuellement via un fichier de configuration json si nécessaire.
- **Préserve le formatage** : les blocs de code, les ancres et les titres sont identifiés et traités séparément pour préserver leur fonctionnalité.
- **Liens de navigation linguistique** : un fichier principal avec des liens vers d'autres traductions ainsi que des liens dans chaque fichier traduit sera ajouté ou mis à jour pour permettre au lecteur de basculer facilement entre les différentes versions linguistiques.

## installation

Utilisez `curl` pour télécharger le script directement à l'emplacement de votre choix :

```bash
curl -o translate-md.py https://raw.githubusercontent.com/dbt1/translate-md/master/translate-md.py
```

**ou**

Utilisez `git clone` pour cloner l'intégralité de la source vers un emplacement de votre choix :

```bash
git clone https://github.com/dbt1/translate-md.git
```

Vous pouvez exécuter `Translate-MD` à partir d'un emplacement de votre choix, soit directement là où il se trouve après le clonage, soit dans le même répertoire où se trouve le modèle Markdown (par défaut : `template.md`). Si `Translate-MD` doit être exécuté directement, le script doit être rendu exécutable en modifiant l'autorisation en fonction du système.

```bash
chmod +x dateiname.py
```

### Installer les dépendances

S'il n'est pas déjà disponible, `Translate-MD` nécessite toujours **googletrans 3.1.0a0** :

   > **Remarque :** La dernière version "stable" de `googletrans` peut causer des problèmes. La version `3.1.0a0` est généralement plus stable et fonctionne mieux.

### Vérification des dépendances

Voici comment vérifier si les modules requis ont été correctement installés :

```bash
python3 -c "from googletrans import Translator; print('Installation erfolgreich')"
```

### Option 1 : installer et exécuter dans un environnement virtuel (recommandé)

Pour ce faire, accédez au répertoire à partir duquel vous souhaitez exécuter `Translate-MD` !

Créez un environnement virtuel, activez et installez `googletrans` :

   ```bash
   python3 -m venv venv && source venv/bin/activate && pip install googletrans==3.1.0a0 && pip install --upgrade setuptools
   ```


### Option 2 : installation à l'échelle du système

Si vous ne souhaitez pas utiliser d'environnement virtuel et que votre système le permet, ce qui n'est pas toujours le cas avec Ubuntu ou Debian par exemple, vous pouvez également installer globalement les modules requis :

```bash
pip install googletrans==3.1.0a0
```

### Installation alternative de googletrans à partir du référentiel GitHub (non recommandé)

  Si vous rencontrez des problèmes, vous pouvez essayer d'installer `googletrans` directement depuis GitHub :

  ```bash
  pip install git+https://github.com/ssut/py-googletrans.git
  ```

Vous pouvez ensuite exécuter `Translate-MD` comme d'habitude.

## utiliser

Voici plusieurs exemples de la façon dont vous pouvez utiliser le script avec tous les paramètres possibles :

---

### Résumé des paramètres

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

Les exemples suivants devraient vous aider à utiliser le script de manière flexible et selon vos besoins.

### 1. Utilisation standard avec les paramètres standards

```bash
python translate-md.py
```

**Description:**
- **Fichier modèle :** `template.md` doit déjà exister dans le même répertoire que `translate-md.py` !
- **Répertoire de sortie :** répertoire actuel (`.`)
- **Préfixe du fichier :** `DOC_`
- **Document principal :** `DOC.md`
- **Fichier de configuration :** Non utilisé
- **Liens linguistiques :** activés

---

### 2. Spécification d'un fichier modèle spécifique et d'un répertoire de sortie

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations
```

**Description:**
- **Fichier modèle :** `path/to/my_template.md`
- **Répertoire de sortie :** `path/to/translations`
- **Autres paramètres :** Valeurs par défaut
- **Liens linguistiques :** activés

---

### 3. Définissez un préfixe et un nom de fichier personnalisés pour le document principal

```bash
python translate-md.py -p README_ -m main_README.md
```

**Description:**
- **Préfixe du fichier :** `README_`
- **Document principal :** `main_README.md`
- **Autres paramètres :** Valeurs par défaut
- **Liens linguistiques :** activés

---

### 4. Utilisation d'un fichier de configuration

**Formatage des paramètres :**
Dans le fichier de configuration, les paramètres doivent être spécifiés sous forme de paires clé-valeur. Toutes les clés (la touche `config-file` n'a pas vraiment de sens ;)) correspondent aux noms longs des paramètres de ligne de commande sans `--` au début. Par exemple:

- `template_md` correspond à `--template-md`
- `output_dir` correspond à `--output-dir`
- `prefix` correspond à `--prefix`
- `main_doc` correspond à `--main-doc`
- `no_language_links` correspond à `--no-language-links`

Supposons que vous ayez un `config.json` avec le contenu suivant :

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

**Commande:**

```bash
python translate-md.py -c path/to/config.json
```

**Description:**
- **Paramètres :** Sont extraits du `config.json`. Tous les autres paramètres non saisis utilisent les paramètres par défaut.

   > **Remarque :** Le `target_languages` par défaut ne peut être utilisé que via le fichier de configuration, sinon seuls `de` et `en` sont utilisés.


### 5. Combinaison de paramètres de ligne de commande et de fichier de configuration

Si le fichier de configuration n'a pas de paramètre défini, vous pouvez l'appliquer comme d'habitude avec les paramètres de ligne de commande.

   > **Remarque :** Les paramètres du fichier de configuration sont prioritaires, ce qui signifie que les paramètres de ligne de commande sont ignorés s'ils ont déjà été saisis dans le fichier de configuration.

**Commande:**

```bash
python translate-md.py -c config.json -p DOC_ -n
```

**Description:**
- **Fichier modèle, répertoire de sortie, document principal :** À partir du `config.json`
- **Préfixe de fichier :** Écrase la valeur définie dans `config.json` et définit sur `DOC_`
- **Liens linguistiques :** Désactivé (`-n` ou `--no-language-links`)

---

### 6. Utilisation de l'option pour désactiver les liens vocaux

```bash
python translate-md.py -n
```

**Description:**
- **Liens linguistiques :** Désactivé
- **Document principal :** Non créé
- **Autres paramètres :** Valeurs par défaut
- **Message d'avertissement :** Le script émet un avertissement indiquant que l'option `-m` sera ignorée.

---

### 7. Utilisation combinée de toutes les options

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations -p README_ -m main_README.md -c config.json --no-language-links
```

**Description:**
- **Fichier modèle :** `path/to/my_template.md` (à partir de la ligne de commande)
- **Répertoire de sortie :** `path/to/translations` (à partir de la ligne de commande)
- **Préfixe du fichier :** `README_` (à partir de la ligne de commande)
- **Document principal :** `main_README.md` (à partir de la ligne de commande, mais est ignoré)
- **Fichier de configuration :** `config.json` (peut contenir des paramètres supplémentaires)
- **Liens linguistiques :** Désactivé (`--no-language-links`)
- **Message d'avertissement :** Le script prévient que l'option `-m` sera ignorée.

---

### 8. Afficher les informations sur la version

```bash
python translate-md.py --version
```

**Description:**
- **Fonction :** Affiche la version du script et arrête l'exécution.

---

### 9. Afficher l'aide

```bash
python translate-md.py --help
```

**Description:**
- **Fonction :** Affiche un message d'aide avec toutes les options disponibles et leurs descriptions.

---

### 10. Exemple avec des liens linguistiques désactivés et utilisant un préfixe différent

```bash
python translate-md.py -p LANG_ -n
```

**Description:**
- **Préfixe du fichier :** `LANG_`
- **Liens linguistiques :** Désactivé
- **Document principal :** Non créé
- **Autres paramètres :** Valeurs par défaut

---

### 11. Utilisation de la forme abrégée des options

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations -p DOC_ -m main_README.md -c config.json -n
```

**Description:**
- **Options courtes :** `-t`, `-o`, `-p`, `-m`, `-c`, `-n`
- **Fonctionnalité :** Équivalent à l'utilisation de toutes les options longues combinées.


## Exemple d'intégration de GitHub Actions

`Translate-MD` peut également être utilisé dans GitHub Actions, par exemple, pour traduire automatiquement un fichier README lors de certains événements (par exemple après un push vers la branche master).
  
> **Remarque sur les autorisations GitHub Actions** : pour que le workflow GitHub Actions dispose des autorisations nécessaires pour transmettre les modifications au référentiel, vous devrez peut-être configurer un `Personal Access Token (PAT)` dans votre compte. Ce jeton est nécessaire pour garantir l'authentification, en particulier si vous avez besoin d'autorisations d'écriture pour transférer vos données vers vos référentiels. Pour plus d'informations sur la configuration d'un `PAT`, consultez la [documentation sur la configuration du jeton GitHub](https://docs.github.com/en/enterprise-server@3.1/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Voici un exemple de `YAML-Datei` qui doit être créé et placé sous `.github/workflows/` s'il n'existe pas déjà.

L'hypothèse ici est que vous souhaitez créer des fichiers README.md localisés situés dans le répertoire racine de votre dépôt.
Cet exemple utilise un fichier modèle `template.md` qui a déjà été enregistré dans le répertoire racine de votre référentiel. Les traductions sont également sorties dans le répertoire racine `.`. Dans ce cas, on suppose que des ajustements ont été apportés à ce modèle et que le push vérifie si des modifications ont été apportées à ce fichier. Si tel est le cas, ce workflow est déclenché, ce qui est spécifié dans la section `on` sous `push`. La branche `master` et le modèle `template.md` sont surveillés. Il est important que les autorisations d'écriture soient activées et doivent être saisies dans la section `permissions`. D'autres entrées garantissent que l'environnement nécessaire est mis en place avec certaines dépendances afin de finalement transférer les modifications dans le dépôt.

`[ci skip]` est ajouté au commit final. Cela permet d'empêcher le commit de déclencher à nouveau le workflow si cela n'est pas souhaité. Cela pourrait économiser des ressources inutiles et éviter les boucles. 


  **Remarque :** Il est logique de tester un flux de travail localement. Plus d'informations à ce sujet [ici](https://github.com/nektos/act) !

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
