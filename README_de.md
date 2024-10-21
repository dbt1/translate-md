<!-- LANGUAGE_LINKS_START -->
<span style="color: grey;">🇩🇪 German</span> | [🇬🇧 English](README_en.md)
<!-- LANGUAGE_LINKS_END -->

# Translate-MD: Markdown Übersetzungsskript

<div style="display: flex; align-items: center;">
  <img src="translate-md.png" alt="translate-md" style="width: 64px; margin-right: 10px;">
  <span>Das Translate-MD Skript dient dazu, eine Markdown Dokument-Vorlage, wie z.B. README.md Dateien, in mehrere Sprachen zu übersetzen. Dabei sollen codierte Inhalte wie Codeblöcke, Anker und Überschriften usw. während des Übersetzungsprozesses erhalten bleiben. <br>
  Es verwendet Google Translator, um den Inhalt automatisch zu übersetzen und dabei bestimmte Abschnitte unverändert zu lassen. Zusätzlich implementiert es Sprachlinks in allen übersetzten Dateien, um eine einfache Navigation zwischen verschiedenen Sprachversionen zu ermöglichen.
  </span>
</div>

## Inhaltsverzeichnis

- [Translate-MD: Markdown Übersetzungsskript](#translate-md-markdown-übersetzungsskript)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Funktionen](#funktionen)
  - [Installation](#installation)
    - [Abhängigkeiten installieren](#abhängigkeiten-installieren)
      - [Zusätzliche Hinweise](#zusätzliche-hinweise)
    - [Überprüfung der Abhängigkeiten](#überprüfung-der-abhängigkeiten)
    - [Option 1: Installation und Ausführung in einer virtuellen Umgebung (empfohlen)](#option-1-installation-und-ausführung-in-einer-virtuellen-umgebung-empfohlen)
    - [Option 2: Systemweite Installation](#option-2-systemweite-installation)
  - [Verwendung](#verwendung)
    - [Beispiel](#beispiel)
    - [Beispiel für GitHub Actions Integration](#beispiel-für-github-actions-integration)

## Funktionen

- **Automatische Spracherkennung**: Das Skript erkennt automatisch die Ausgangssprache aus der Vorlage.
- **Mehrsprachige Übersetzung**: Es übersetzt den Inhalt in mehrere Sprachen, die im Script unter `TARGET_LANGUAGES` oder optional über eine json-Konfigurationsdatei bei Bedarf ergänzt werden können.
- **Bewahrt Formatierung**: Codeblöcke, Anker und Überschriften usw. werden identifiziert und separat behandelt, um deren Fuktionalität beizubehalten
- **Sprachnavigationslinks**: Sprachlinks werden in jeder übersetzten Datei hinzugefügt oder aktualisiert, so dass  für den Leser ein einfacher Wechsel zwischen verschiedenen Sprachversionen möglich ist.

## Installation

```bash
git clone https://github.com/dbt1/translate-md.git
```

Du kannst das Übersetzungsskript von einem Ort deiner Wahl ausführen oder direkt wo es sich nach dem Klonen befindet oder auch im selbem Verzeichnis in dem sich die Markdown-Vorlage (Standard: `template.md`) befindet. Wenn das Übersetzungsskript direkt ausgeführt werden soll, muss das Skript ausführbar gemacht werden, indem du die Berechtigung änderst.

   ```bash
   chmod +x dateiname.py
   ```
   
### Abhängigkeiten installieren

Dieses Skript benötigt `googletrans` für die Übersetzung:

Installation: 
  
  ```bash
  pip install googletrans==3.1.0a0
  ```

  **Hinweis:** Version >= 4 scheint instabil zu sein oder Probleme zu verursachen. Daher wird Version `3.1.0a0` empfohlen.

#### Zusätzliche Hinweise

- **Alternative Installation von googletrans vom GitHub-Repository**:

  Falls Probleme auftreten, kannst du `googletrans` direkt von GitHub installieren:

  ```bash
  pip install git+https://github.com/ssut/py-googletrans.git
  ```

### Überprüfung der Abhängigkeiten

  Nach der Installation der Abhängigkeiten kannst du überprüfen, ob die benötigen Module korrekt installiert wurden:

  ```bash
  python3 -c "from googletrans import Translator; print('Installation erfolgreich')"
  ```

### Option 1: Installation und Ausführung in einer virtuellen Umgebung (empfohlen)

1. **Erstellen einer virtuellen Umgebung, Aktivieren und Installieren von `googletrans`**:

   ```bash
   python3 -m venv venv && source venv/bin/activate && pip install googletrans==3.1.0a0 && pip install --upgrade setuptools
   ```
   > **Hinweis:** Die neueste stabile Version von `googletrans` kann Probleme verursachen. Die Version `3.1.0a0` ist in der Regel stabiler und funktioniert besser.

2. **Skript ausführbar machen** (nur für Unix-basierte Systeme, optional):

   ```bash
   chmod +x translate-md.py
   ```

3. **Skript ausführen**:

   ```bash
   python3 translate-md.py
   ```

### Option 2: Systemweite Installation

Wenn du keine virtuelle Umgebung verwenden möchtest, kannst du die erforderlichen Module auch global installieren:

   ```bash
   pip install googletrans==3.1.0a0
   ```

Anschließend kannst du das Skript wie gewohnt ausführen.

## Verwendung

Führe das Skript über die Befehlszeile durch die Angabe der Markdown-Vorlagendatei mit dem Argument `-t` aus. Wenn kein Argument angegeben wird, verwendet das Skript standardmäßig `template.md` aus dem aktuellen Verzeichnis und die Ubersetzungen werden ebenfalls im gleichen Verzeichnis erzeugt. Das Skript kann lokal oder zur automatisierten Übersetzung z.B. über einen Workflow eines Git-Repositorys wie bei GitHub angewendet werden, indem es z.B. entsprechend über Commitvorgänge aufgerufen wird. Über Git-Hooks könnte man es, je nachdem wie es eingebunden wird, auf ähnliche Weise ebenfalls verwenden.

### Beispiel

   ```bash
   python translate-md.py -t template.md
   ```

### Beispiel für GitHub Actions Integration

Das Übersetzungsskript kann auch in GitHub Actions verwendet werden, um z.B. eine README-Datei automatisch bei bestimmten Events (z.B. nach einem Commit in den Main-Branch) zu übersetzen.
  
**Hinweis zu GitHub Actions Berechtigungen**: Damit der GitHub Actions Workflow die nötigen Berechtigungen hat, um Änderungen in das Repository zu pushen, musst du möglicherweise ein `Personal Access Token (PAT)` einrichten. Dieses Token wird benötigt, um die Authentifizierung sicherzustellen, besonders wenn du auf ein Repository pushst. Weitere Informationen zur Einrichtung eines `PAT` findest du in der [GitHub Dokumentation zur Token-Konfiguration](https://docs.github.com/en/enterprise-server@3.1/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Hier ist ein Beispiel einer `YAML-Datei`, die unter `.github/workflows/` angelegt werden muss. Diese Workflow-Verzeichnis muss angelegt und gepusht werden, sofern noch nicht vorhanden.
Hier wird angenommen, eine README.md übersetzen zu wollen, die sich üblicherweise im Rootverzeichnis eines Repos befindet.
In diesem Beispiel wird eine Vorlage angegeben, die unter `./templates/README_de.md` gespeichert wurde. Konkret in diesem Fall wird davon ausgegangen, dass man an nur an dieser Vorlage regelmäßig Anpassungen vornimmt. Wie du vielleicht bemerkst, ist das eigentlich der Name einer Zieldatei, was aber kein Problem ist, da diese Datei sich nicht im gleichen Verzeichnis wie die Zieldatei befindet.

Am abschließenden Commit wird noch `[ci skip]` angehängt. Dies soll verhindern, dass der Commit den Workflow erneut auslöst, wenn das nicht gewünscht ist. Das könnte unnötige Ressourcen sparen und Schleifen vermeiden.: 

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

  **Hinweis:** Es ist sinnvoll einen Workflow lokal zu testen. Weitere Informationen dazu [hier](https://github.com/nektos/act)!
