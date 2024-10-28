<!-- LANGUAGE_LINKS_START -->
<span style="color: grey;">🇩🇪 German</span> | [🇬🇧 English](README_en.md) | [🇪🇸 Spanish](README_es.md) | [🇫🇷 French](README_fr.md) | [🇮🇹 Italian](README_it.md)
<!-- LANGUAGE_LINKS_END -->

# Translate-MD: Markdown Übersetzungsskript

<div style="display: flex; align-items: center;">
  <img src="translate-md.png" alt="translate-md" style="width: 64px; margin-right: 10px;">
  <span>Translate-MD ist ein Python-Script und dient dazu, aus einer Markdown-Dokumentvorlage, wie z.B. template.md, Dateien in mehrere Sprachen zu übersetzen und in vorgegebene Zielsprachen zu speichern. Dabei sollen codierte Inhalte wie Codeblöcke, Anker und Überschriften während des Übersetzungsprozesses erhalten bleiben. <br>
  Es verwendet Google Translator, um den Inhalt automatisch zu übersetzen und dabei bestimmte Abschnitte unverändert zu lassen. Zusätzlich implementiert es Sprachlinks in allen übersetzten Dateien, um eine einfache Navigation zwischen verschiedenen Sprachversionen zu ermöglichen.
  </span>
</div>

## Inhaltsverzeichnis

- [Translate-MD: Markdown Übersetzungsskript](#translate-md-markdown-übersetzungsskript)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Funktionen](#funktionen)
  - [Installation](#installation)
    - [Abhängigkeiten installieren](#abhängigkeiten-installieren)
    - [Überprüfung der Abhängigkeiten](#überprüfung-der-abhängigkeiten)
    - [Option 1: Installation und Ausführung in einer virtuellen Umgebung (empfohlen)](#option-1-installation-und-ausführung-in-einer-virtuellen-umgebung-empfohlen)
    - [Option 2: Systemweite Installation](#option-2-systemweite-installation)
    - [Alternative Installation von googletrans vom GitHub-Repository (nicht empfohlen)](#alternative-installation-von-googletrans-vom-github-repository-nicht-empfohlen)
  - [Verwendung](#verwendung)
    - [Zusammenfassung der Parameter](#zusammenfassung-der-parameter)
    - [1. Standardverwendung mit den Standardparametern](#1-standardverwendung-mit-den-standardparametern)
    - [2. Angabe einer spezifischen Template-Datei und eines Ausgabeverzeichnisses](#2-angabe-einer-spezifischen-template-datei-und-eines-ausgabeverzeichnisses)
    - [3. Festlegen eines benutzerdefinierten Dateipräfixes und Namens für das Hauptdokument](#3-festlegen-eines-benutzerdefinierten-dateipräfixes-und-namens-für-das-hauptdokument)
    - [4. Verwendung einer Konfigurationsdatei](#4-verwendung-einer-konfigurationsdatei)
    - [5. Kombination von Kommandozeilenparametern und Konfigurationsdatei](#5-kombination-von-kommandozeilenparametern-und-konfigurationsdatei)
    - [6. Verwendung der Option zum Deaktivieren von Sprachlinks](#6-verwendung-der-option-zum-deaktivieren-von-sprachlinks)
    - [7. Kombinierte Verwendung aller Optionen](#7-kombinierte-verwendung-aller-optionen)
    - [8. Anzeigen der Versionsinformation](#8-anzeigen-der-versionsinformation)
    - [9. Hilfe anzeigen](#9-hilfe-anzeigen)
    - [10. Beispiel mit deaktivierten Sprachlinks und Verwendung eines anderen Präfixes](#10-beispiel-mit-deaktivierten-sprachlinks-und-verwendung-eines-anderen-präfixes)
    - [11. Verwendung der Kurzform der Optionen](#11-verwendung-der-kurzform-der-optionen)
  - [Beispiel für GitHub Actions Integration](#beispiel-für-github-actions-integration)

## Funktionen

- **Automatische Spracherkennung**: `Translate-MD`erkennt automatisch die Ausgangssprache aus der Vorlage.
- **Mehrsprachige Übersetzung**: `Translate-MD`übersetzt den Inhalt in mehrere Sprachen, die im Skript unter `TARGET_LANGUAGES` oder optional über eine json-Konfigurationsdatei bei Bedarf ergänzt werden können.
- **Bewahrt Formatierung**: Codeblöcke, Anker und Überschriften werden identifiziert und separat behandelt, um deren Funktionalität beizubehalten.
- **Sprachnavigationslinks**: Es wird eine Hauptdatei mit Links zu anderen Übersetzungen als auch Links in jeder übersetzten Datei hinzugefügt oder aktualisiert, damit für den Leser ein einfacher Wechsel zwischen verschiedenen Sprachversionen möglich ist.

## Installation

Verwende `curl`, um das Skript direkt an einen Ort deiner Wahl herunterzuladen:

```bash
curl -o translate-md.py https://raw.githubusercontent.com/dbt1/translate-md/master/translate-md.py
```

**oder**

Verwende `git clone`, um die gesamten Sourcen an einen Ort deiner Wahl zu klonen:

```bash
git clone https://github.com/dbt1/translate-md.git
```

Du kannst `Translate-MD` von einem Ort deiner Wahl ausführen, entweder direkt dort, wo es sich nach dem Klonen befindet, oder im selben Verzeichnis, in dem sich die Markdown-Vorlage (Standard: `template.md`) befindet. Wenn `Translate-MD` direkt ausgeführt werden soll, muss das Skript je nach System ausführbar gemacht werden, indem du die Berechtigung änderst.

```bash
chmod +x dateiname.py
```

### Abhängigkeiten installieren

Falls nicht bereits vorhanden, benötigt `Translate-MD` noch **googletrans 3.1.0a0**:

   > **Hinweis:** Die neueste "stabile" Version von `googletrans` kann Probleme verursachen. Die Version `3.1.0a0` ist in der Regel stabiler und funktioniert besser.

### Überprüfung der Abhängigkeiten

So kannst du überprüfen, ob die benötigten Module korrekt installiert wurden:

```bash
python3 -c "from googletrans import Translator; print('Installation erfolgreich')"
```

### Option 1: Installation und Ausführung in einer virtuellen Umgebung (empfohlen)

Wechsle dafür in das Verzeichnis, von wo du `Translate-MD` ausführen willst!

Erstelle einer virtuellen Umgebung, Aktiviere und Installiere `googletrans`:

   ```bash
   python3 -m venv venv && source venv/bin/activate && pip install googletrans==3.1.0a0 && pip install --upgrade setuptools
   ```


### Option 2: Systemweite Installation

Wenn du keine virtuelle Umgebung verwenden möchtest und dein System dies zulässt, was z.B. bei Ubuntu oder Debian nicht immer der Fall ist, kannst du die erforderlichen Module auch global installieren:

```bash
pip install googletrans==3.1.0a0
```

### Alternative Installation von googletrans vom GitHub-Repository (nicht empfohlen)

  Falls Probleme auftreten, kannst du versuchen `googletrans` direkt von GitHub installieren:

  ```bash
  pip install git+https://github.com/ssut/py-googletrans.git
  ```

Anschließend kannst du `Translate-MD` wie gewohnt ausführen.

## Verwendung

Hier sind mehrere Beispiele, wie du das Skript mit allen möglichen Parametern verwenden kannst:

---

### Zusammenfassung der Parameter

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

Die folgende Beispiele sollten dir helfen, das Skript flexibel und entsprechend deinen Anforderungen zu verwenden.

### 1. Standardverwendung mit den Standardparametern

```bash
python translate-md.py
```

**Beschreibung:**
- **Template-Datei:** `template.md` muss bereits im gleichen Verzeichnis vorhanden sein wie `translate-md.py`!
- **Ausgabeverzeichnis:** aktuelles Verzeichnis (`.`)
- **Dateipräfix:** `DOC_`
- **Hauptdokument:** `DOC.md`
- **Konfigurationsdatei:** Nicht verwendet
- **Sprachlinks:** Eingeschaltet

---

### 2. Angabe einer spezifischen Template-Datei und eines Ausgabeverzeichnisses

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations
```

**Beschreibung:**
- **Template-Datei:** `path/to/my_template.md`
- **Ausgabeverzeichnis:** `path/to/translations`
- **Andere Parameter:** Standardwerte
- **Sprachlinks:** Eingeschaltet

---

### 3. Festlegen eines benutzerdefinierten Dateipräfixes und Namens für das Hauptdokument

```bash
python translate-md.py -p README_ -m main_README.md
```

**Beschreibung:**
- **Dateipräfix:** `README_`
- **Hauptdokument:** `main_README.md`
- **Andere Parameter:** Standardwerte
- **Sprachlinks:** Eingeschaltet

---

### 4. Verwendung einer Konfigurationsdatei

**Parameter Formatierung:**
In der Konfigurationsdatei müssen die Parameter als Schlüssel-Werte-Paare angegeben werden. Alle Schlüssel (der Schlüssel `config-file` macht nicht wirklich Sinn ;))  entsprechen den langen Namen der Kommandozeilenparameter ohne `--` am Anfang. Beispielsweise:

- `template_md` entspricht `--template-md`
- `output_dir` entspricht `--output-dir`
- `prefix` entspricht `--prefix`
- `main_doc` entspricht `--main-doc`
- `no_language_links` entspricht `--no-language-links`

Angenommen, du hast eine `config.json` mit folgendem Inhalt:

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

**Befehl:**

```bash
python translate-md.py -c path/to/config.json
```

**Beschreibung:**
- **Parameter:** Werden aus der `config.json` übernommen. Alle anderen nicht eingetragenen Parameter verwenden Standardvorgaben.

   > **Hinweis:** Die Vorgabe `target_languages` kann nur über die Konfigurationsdatei verwendet werden, ansonsten wird nur `de` und `en` verwendet.


### 5. Kombination von Kommandozeilenparametern und Konfigurationsdatei

Wenn die Konfigurationsdatei ein Parameter nicht definiert ist, kannst du diese wie üblich mit Kommandozeilenparametern anwenden.

   > **Hinweis:** Die Einstellungen in der Konfigurationsdatei haben Vorrang, das heißt, Kommandozeilenparameter werden ignoriert, falls diese in der Konfigurationsdatei schon eingetragen wurden.

**Befehl:**

```bash
python translate-md.py -c config.json -p DOC_ -n
```

**Beschreibung:**
- **Template-Datei, Ausgabeverzeichnis, Hauptdokument:** Aus der `config.json`
- **Dateipräfix:** Überschreibt den in der `config.json` definierten Wert und setzt auf `DOC_`
- **Sprachlinks:** Deaktiviert (`-n` oder `--no-language-links`)

---

### 6. Verwendung der Option zum Deaktivieren von Sprachlinks

```bash
python translate-md.py -n
```

**Beschreibung:**
- **Sprachlinks:** Deaktiviert
- **Hauptdokument:** Wird nicht erstellt
- **Andere Parameter:** Standardwerte
- **Warnmeldung:** Das Skript gibt eine Warnung aus, dass die Option `-m` ignoriert wird.

---

### 7. Kombinierte Verwendung aller Optionen

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations -p README_ -m main_README.md -c config.json --no-language-links
```

**Beschreibung:**
- **Template-Datei:** `path/to/my_template.md` (aus Kommandozeile)
- **Ausgabeverzeichnis:** `path/to/translations` (aus Kommandozeile)
- **Dateipräfix:** `README_` (aus Kommandozeile)
- **Hauptdokument:** `main_README.md` (aus Kommandozeile, aber wird ignoriert)
- **Konfigurationsdatei:** `config.json` (kann weitere Einstellungen enthalten)
- **Sprachlinks:** Deaktiviert (`--no-language-links`)
- **Warnmeldung:** Das Skript warnt, dass die Option `-m` ignoriert wird.

---

### 8. Anzeigen der Versionsinformation

```bash
python translate-md.py --version
```

**Beschreibung:**
- **Funktion:** Zeigt die Version des Skripts an und beendet die Ausführung.

---

### 9. Hilfe anzeigen

```bash
python translate-md.py --help
```

**Beschreibung:**
- **Funktion:** Zeigt eine Hilfsnachricht mit allen verfügbaren Optionen und deren Beschreibungen an.

---

### 10. Beispiel mit deaktivierten Sprachlinks und Verwendung eines anderen Präfixes

```bash
python translate-md.py -p LANG_ -n
```

**Beschreibung:**
- **Dateipräfix:** `LANG_`
- **Sprachlinks:** Deaktiviert
- **Hauptdokument:** Wird nicht erstellt
- **Andere Parameter:** Standardwerte

---

### 11. Verwendung der Kurzform der Optionen

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations -p DOC_ -m main_README.md -c config.json -n
```

**Beschreibung:**
- **Kurzoptionen:** `-t`, `-o`, `-p`, `-m`, `-c`, `-n`
- **Funktionalität:** Entspricht der kombinierten Verwendung aller langen Optionen.


## Beispiel für GitHub Actions Integration

`Translate-MD` kann auch z.B. in GitHub Actions verwendet werden, um z.B. eine README-Datei automatisch bei bestimmten Events (z.B. nach einem Push in den master-Branch) zu übersetzen.
  
> **Hinweis zu GitHub Actions Berechtigungen**: Damit der GitHub Actions Workflow die nötigen Berechtigungen hat, um Änderungen in das Repository zu pushen, musst du möglicherweise noch ein `Personal Access Token (PAT)` in deinem Account einrichten. Dieses Token wird benötigt, um die Authentifizierung sicherzustellen, besonders wenn du Schreibrechte zum pushen auf deine Repositorys brauchst. Weitere Informationen zur Einrichtung eines `PAT` findest du in der [GitHub Dokumentation zur Token-Konfiguration](https://docs.github.com/en/enterprise-server@3.1/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Hier ist ein Beispiel einer `YAML-Datei`, die unter `.github/workflows/` angelegt und gepusht werden muss, sofern noch nicht vorhanden.

Hier wird angenommen, lokalisierte README.md-Dateien erzeugen zu wollen, die sich im Rootverzeichnis deines Repos befinden.
In diesem Beispiel wird dafür eine Vorlagendatei `template.md` verwendet, die im Rootverzeichnis deines Repositorys bereits gespeichert wurde. Die Ausgabe der Übersetzungen erfolgt ebenfalls in das Rootverzeichnis `.`. Es wird in diesem Fall wird davon ausgegangen, dass man an dieser Vorlage Anpassungen vornimmt und beim Push geprüft wird, ob an dieser Datei Änderungen vorgenommen wurden. Ist dies der Fall, wird dieser Workflow ausgelöst, was im Abschnitt `on` unter `push` festgelegt ist. Es wird der Branch `master` und die Vorlage `template.md` überwacht. Wichtig ist hierbei, dass Schreibrechte aktivert werden, was unter dem Abschnitt `permissions` eingetragen sein muss. Weitere Einträge sorgen dafür, dass die notwendige Umgebung mit einigen Abängigkeiten eingerichtet wird, um dann letztich die Änderungen in das Repo zu pushen.

Am abschließenden Commit wird noch `[ci skip]` angehängt. Dies soll verhindern, dass der Commit den Workflow erneut auslöst, wenn das nicht gewünscht ist. Das könnte unnötige Ressourcen sparen und Schleifen vermeiden. 


  **Hinweis:** Es ist sinnvoll einen Workflow lokal zu testen. Weitere Informationen dazu [hier](https://github.com/nektos/act)!

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

