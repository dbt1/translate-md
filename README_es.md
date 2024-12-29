<!-- LANGUAGE_LINKS_START -->
[🇩🇪 German](README_de.md) | [🇬🇧 English](README_en.md) | <span style="color: grey;">🇪🇸 Spanish</span> | [🇫🇷 French](README_fr.md) | [🇮🇹 Italian](README_it.md)
<!-- LANGUAGE_LINKS_END -->

# Translate-MD - Script de traducción Markdown

<div style="display: flex; align-items: center;">
  <img src="translate-md.png" alt="translate-md" style="width: 64px; margin-right: 10px;">
  <span>Translate-MD ist ein Python-Script und dient dazu, aus einer Markdown-Dokumentvorlage, wie z.B. template.md, Dateien in mehrere Sprachen zu übersetzen und in vorgegebene Zielsprachen zu speichern. Dabei sollen codierte Inhalte wie Codeblöcke, Anker und Überschriften während des Übersetzungsprozesses erhalten bleiben.
  Es verwendet Google Translator, um den Inhalt automatisch zu übersetzen und dabei bestimmte Abschnitte unverändert zu lassen. Zusätzlich implementiert es Sprachlinks in allen übersetzten Dateien, um eine einfache Navigation zwischen verschiedenen Sprachversionen zu ermöglichen.
  </span>
</div>

## Tabla de contenido

- [Translate-MD: Markdown Übersetzungsskript](#translate-md-markdown-übersetzungsskript)
  - [Inhaltsverzeichnis](#tabla-de-contenido)
  - [Funktionen](#características)
  - [Installation](#instalación)
    - [Abhängigkeiten installieren](#instalar-dependencias)
    - [Überprüfung der Abhängigkeiten](#comprobación-de-dependencia)
    - [Option 1: Installation und Ausführung in einer virtuellen Umgebung (empfohlen)](#opción-1-instalar-y-ejecutar-en-un-entorno-virtual-recomendado)
    - [Option 2: Systemweite Installation](#opción-2-instalación-en-todo-el-sistema)
    - [Alternative Installation von googletrans vom GitHub-Repository (nicht empfohlen)](#instalación-alternativa-de-googletrans-desde-el-repositorio-de-github-no-recomendado)
  - [Verwendung](#usar)
    - [Zusammenfassung der Parameter](#resumen-de-parámetros)
    - [1. Standardverwendung mit den Standardparametern](#1-uso-estándar-con-los-parámetros-estándar)
    - [2. Angabe einer spezifischen Template-Datei und eines Ausgabeverzeichnisses](#2-especificar-un-archivo-de-plantilla-específico-y-un-directorio-de-salida)
    - [3. Festlegen eines benutzerdefinierten Dateipräfixes und Namens für das Hauptdokument](#3-establezca-un-prefijo-de-archivo-personalizado-y-un-nombre-para-el-documento-principal)
    - [4. Verwendung einer Konfigurationsdatei](#4-usando-un-archivo-de-configuración)
    - [5. Kombination von Kommandozeilenparametern und Konfigurationsdatei](#5-combinación-de-parámetros-de-línea-de-comando-y-archivo-de-configuración)
    - [6. Verwendung der Option zum Deaktivieren von Sprachlinks](#6-usar-la-opción-para-desactivar-los-enlaces-de-voz)
    - [7. Kombinierte Verwendung aller Optionen](#7-uso-combinado-de-todas-las-opciones)
    - [8. Anzeigen der Versionsinformation](#8-ver-información-de-la-versión)
    - [9. Hilfe anzeigen](#9-mostrar-ayuda)
    - [10. Beispiel mit deaktivierten Sprachlinks und Verwendung eines anderen Präfixes](#10-ejemplo-con-enlaces-de-idiomas-deshabilitados-y-usando-un-prefijo-diferente)
    - [11. Verwendung der Kurzform der Optionen](#11-uso-de-la-forma-corta-de-opciones)
  - [Beispiel für GitHub Actions Integration](#ejemplo-de-integración-de-github-actions)

## Características

- **Automatische Spracherkennung**: `Translate-MD`erkennt automatisch die Ausgangssprache aus der Vorlage.
- **Mehrsprachige Übersetzung**: `Translate-MD`übersetzt den Inhalt in mehrere Sprachen, die im Skript unter `TARGET_LANGUAGES` oder optional über eine json-Konfigurationsdatei bei Bedarf ergänzt werden können.
- **Bewahrt Formatierung**: Codeblöcke, Anker und Überschriften werden identifiziert und separat behandelt, um deren Funktionalität beizubehalten.
- **Sprachnavigationslinks**: Es wird eine Hauptdatei mit Links zu anderen Übersetzungen als auch Links in jeder übersetzten Datei hinzugefügt oder aktualisiert, damit für den Leser ein einfacher Wechsel zwischen verschiedenen Sprachversionen möglich ist.

## instalación

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

### Instalar dependencias

Falls nicht bereits vorhanden, benötigt `Translate-MD` noch **googletrans 3.1.0a0**:

   > **Hinweis:** Die neueste "stabile" Version von `googletrans` kann Probleme verursachen. Die Version `3.1.0a0` ist in der Regel stabiler und funktioniert besser.

### Comprobación de dependencia

So kannst du überprüfen, ob die benötigten Module korrekt installiert wurden:

```bash
python3 -c "from googletrans import Translator; print('Installation erfolgreich')"
```

### Opción 1: instalar y ejecutar en un entorno virtual (recomendado)

Wechsle dafür in das Verzeichnis, von wo du `Translate-MD` ausführen willst!

Erstelle einer virtuellen Umgebung, Aktiviere und Installiere `googletrans`:

   ```bash
   python3 -m venv venv && source venv/bin/activate && pip install googletrans==3.1.0a0 && pip install --upgrade setuptools
   ```


### Opción 2: instalación en todo el sistema

Wenn du keine virtuelle Umgebung verwenden möchtest und dein System dies zulässt, was z.B. bei Ubuntu oder Debian nicht immer der Fall ist, kannst du die erforderlichen Module auch global installieren:

```bash
pip install googletrans==3.1.0a0
```

### Instalación alternativa de googletrans desde el repositorio de GitHub (no recomendado)

  Falls Probleme auftreten, kannst du versuchen `googletrans` direkt von GitHub installieren:

  ```bash
  pip install git+https://github.com/ssut/py-googletrans.git
  ```

Anschließend kannst du `Translate-MD` wie gewohnt ausführen.

## usar

Die folgende Beispiele sollten dir helfen, das Skript flexibel und entsprechend deinen Anforderungen zu verwenden.

---

### Resumen de parámetros

| Kurzform | Langform              | Beschreibung                                                                           | Standardwert                           |
|----------|-----------------------|-----------------------------------------------------------------------------------------|----------------------------------------|
| `-t`     | `--template-md`       | Pfad zur Template-Datei Standard:                                                       | `template.md` (im aktuellen Verzeichnis) |
| `-o`     | `--output-dir`        | Verzeichnis, in dem die übersetzten Dateien gespeichert werden sollen                   | `.` (aktuelles Verzeichnis)            |
| `-p`     | `--prefix`            | Präfix für die Namen der übersetzten Dateien                                             | `DOC_`                                 |
| `-m`     | `--main-doc`          | Name der Hauptdokument-Datei                                                              | `DOC.md`                               |
| `-c`     | `--config-file`       | Pfad zur Konfigurationsdatei (optional)                                                  | `None`                                 |
| `-n`     | `--no-language-links` | Verhindert das Einfügen von Sprachlinks und überspringt die Erstellung der Hauptdokument-Datei | `False` (Sprachlinks aktiviert)        |
| `-s`     | `--source-lang`       | Quellsprache (optional)                                                                 | `None` (automatisch)        |
| `-v`     | `--version`           | Zeigt die Version des Skripts an und beendet die Ausführung                            |                                        |
| `-h`     | `--help`              | Zeigt die Hilfsnachricht mit allen verfügbaren Optionen an                              |                                        |

---

### 1. Uso estándar con los parámetros estándar.

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

### 2. Especificar un archivo de plantilla específico y un directorio de salida

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations
```

**Beschreibung:**
- **Template-Datei:** `path/to/my_template.md`
- **Ausgabeverzeichnis:** `path/to/translations`
- **Andere Parameter:** Standardwerte
- **Sprachlinks:** Eingeschaltet

---

### 3. Establezca un prefijo de archivo personalizado y un nombre para el documento principal.

```bash
python translate-md.py -p README_ -m main_README.md
```

**Beschreibung:**
- **Dateipräfix:** `README_`
- **Hauptdokument:** `main_README.md`
- **Andere Parameter:** Standardwerte
- **Sprachlinks:** Eingeschaltet

---

### 4. Usando un archivo de configuración

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


### 5. Combinación de parámetros de línea de comando y archivo de configuración

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

### 6. Usar la opción para desactivar los enlaces de voz.

```bash
python translate-md.py -n
```

**Beschreibung:**
- **Sprachlinks:** Deaktiviert
- **Hauptdokument:** Wird nicht erstellt
- **Andere Parameter:** Standardwerte
- **Warnmeldung:** Das Skript gibt eine Warnung aus, dass die Option `-m` ignoriert wird.

---

### 7. Uso combinado de todas las opciones.

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

### 8. Ver información de la versión

```bash
python translate-md.py --version
```

**Beschreibung:**
- **Funktion:** Zeigt die Version des Skripts an und beendet die Ausführung.

---

### 9. Mostrar ayuda

```bash
python translate-md.py --help
```

**Beschreibung:**
- **Funktion:** Zeigt eine Hilfsnachricht mit allen verfügbaren Optionen und deren Beschreibungen an.

---

### 10. Ejemplo con enlaces de idiomas deshabilitados y usando un prefijo diferente

```bash
python translate-md.py -p LANG_ -n
```

**Beschreibung:**
- **Dateipräfix:** `LANG_`
- **Sprachlinks:** Deaktiviert
- **Hauptdokument:** Wird nicht erstellt
- **Andere Parameter:** Standardwerte

---

### 11. Uso de la forma corta de opciones.

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations -p DOC_ -m main_README.md -c config.json -n
```

**Beschreibung:**
- **Kurzoptionen:** `-t`, `-o`, `-p`, `-m`, `-c`, `-n`
- **Funktionalität:** Entspricht der kombinierten Verwendung aller langen Optionen.


## Ejemplo de integración de GitHub Actions

`Translate-MD` kann auch z.B. in GitHub Actions verwendet werden, um z.B. eine README-Datei automatisch bei bestimmten Events (z.B. nach einem Push in den master-Branch) zu übersetzen.
  
> **Hinweis zu GitHub Actions Berechtigungen**: Damit der GitHub Actions Workflow die nötigen Berechtigungen hat, um Änderungen in das Repository zu pushen, musst du möglicherweise noch ein `Personal Access Token (PAT)` in deinem Account einrichten. Dieses Token wird benötigt, um die Authentifizierung sicherzustellen, besonders wenn du Schreibrechte zum pushen auf deine Repositorys brauchst. Weitere Informationen zur Einrichtung eines `PAT` findest du in der [GitHub Dokumentation zur Token-Konfiguration](https://docs.github.com/en/enterprise-server@3.1/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Hier ist ein Beispiel einer `YAML-Datei`. Kopiere den Inhalt von hier und füge ihn in eine Datei ei. Nenne sie z.B. `translate.yaml`, die unter `.github/workflows/` gespeichert wird und gepusht werden muss, sofern noch nicht vorhanden.
Der Aufbau ist generisch, damit der Workflow prinzipiell in jedem Repository verwendet werden kann, sofern die folgenden Voraussetzungen erfüllt sind:

  - **Vorlage**: `readme-template.md` muss im Root Verzeichnis des Repositorys vorhanden sein und als Ausgangspunkt für die Übersetzung dienen.
  - **Skript**:  `translate-md.py` muss mit den Übergabeparametern und dem Pfad zur Vorlage (`--template-md readme-template.md`) kompatibel sein und die restlichen Parameter entsprechend verarbeiten.
  - **Quellsprache**: Die im Workflow definierte `SOURCE_LANG`-Umgebungsvariable muss der Quellsprache im Template entsprechen, damit die Übersetzung wie gewünscht funktioniert.
  - **Konsistenz bei den Namen**: Der Workflow bezieht sich auf `readme-template.md` und generiert Dateien mit dem Präfix `README_`. Wenn ein anderer Name oder Präfix erforderlich ist, kann dies direkt in der `Translate README`-Schritt-Konfiguration angepasst werden.

 > **Hinweis:** Bereits vorhandene README's bzw. Dateien, die mit dem festgelegten Namensbereich übereinstimmen, werden überschrieben! Notfalls bitte sichern! Es ist daher sinnvoll einen Workflow lokal zu testen. Weitere Informationen dazu [hier](https://github.com/nektos/act)!

Hier wird angenommen, lokalisierte README.md-Dateien erzeugen zu wollen, die sich im Rootverzeichnis deines Repos befinden.
In diesem Beispiel wird dafür eine Vorlagendatei `readme-template.md` verwendet, die im Rootverzeichnis deines Repositorys bereits vorhanden ist. Die Ausgabe der Übersetzungen erfolgt ebenfalls in das Rootverzeichnis `.`. Beim Push in das Remote-Repository wird im `master`-Branch geprüft, ob an `readme-template.md` Änderungen vorgenommen wurden. Ist dies der Fall, wird dieser Workflow ausgelöst, was im Abschnitt `on` unter `push` festgelegt ist. Es wird also der Branch `master` und die Vorlagendatei überwacht. Wichtig ist hierbei, dass Schreibrechte aktivert werden, was unter dem Abschnitt `permissions` eingetragen ist. Weitere Einträge sorgen dafür, dass die notwendige Umgebung mit einigen Abängigkeiten eingerichtet wird, um dann letztich die Änderungen in das Repo zu pushen.

```yaml
name: Translate README

on:
  push:
    branches:
      - master
    paths:
      - 'readme-template.md'

permissions:
  contents: write

jobs:
  translate:
    runs-on: ubuntu-latest

    env:
      PYTHON_VERSION: 3.x
      GIT_USER_EMAIL: "actions@github.com"
      GIT_USER_NAME: "GitHub Actions"
      TRANSLATE_SCRIPT_NAME: "translate-md.py"
      TRANSLATE_SCRIPT_URL: "https://raw.githubusercontent.com/dbt1/translate-md/master"
      #TRANSLATE_SCRIPT_URL: "https://raw.githubusercontent.com/dbt1/translate-md/v1.2.0"
      SOURCE_LANG: "de"
      #SOURCE_LANG: "en"
      TEMPLATE_FILE: "readme-template.md"

    steps:
    - name: Checkout code
      uses: actions/checkout@v3
      with:
        token: ${{ secrets.GITHUB_TOKEN }}

    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ env.PYTHON_VERSION }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install --upgrade googletrans==3.1.0a0
        curl -o ${{ env.TRANSLATE_SCRIPT_NAME }} ${{ env.TRANSLATE_SCRIPT_URL }}/${{ env.TRANSLATE_SCRIPT_NAME }}
        chmod 755 ${{ env.TRANSLATE_SCRIPT_NAME }}

    - name: Translate README
      run: |
        python ${{ env.TRANSLATE_SCRIPT_NAME }} --template-md ${{ env.TEMPLATE_FILE }} --output-dir . --prefix README_ --main-doc README.md -s ${{ env.SOURCE_LANG }}

    - name: Commit and push translated README
      run: |
        git config --global user.email "${{ env.GIT_USER_EMAIL }}"
        git config --global user.name "${{ env.GIT_USER_NAME }}"
        git add README*.md
        if ! git diff --cached --quiet; then
          git commit -m "readme: Automatically translated README"
          git push
        else
          echo "No changes to commit"
        fi
```

