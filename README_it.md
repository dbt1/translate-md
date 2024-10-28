<!-- LANGUAGE_LINKS_START -->
[🇩🇪 German](README_de.md) | [🇬🇧 English](README_en.md) | [🇪🇸 Spanish](README_es.md) | [🇫🇷 French](README_fr.md) | <span style="color: grey;">🇮🇹 Italian</span>
<!-- LANGUAGE_LINKS_END -->

# Translate-MD: script di traduzione Markdown

<div style="display: flex; align-items: center;">
  <img src="translate-md.png" alt="translate-md" style="width: 64px; margin-right: 10px;">
  <span>Translate-MD è uno script Python e viene utilizzato per tradurre file in diverse lingue da un modello di documento Markdown, come template.md, e per salvarli nelle lingue di destinazione specificate. I contenuti codificati come blocchi di codice, ancoraggi e intestazioni dovrebbero essere conservati durante il processo di traduzione. <br>
  Utilizza Google Translator per tradurre automaticamente il contenuto lasciando invariate alcune sezioni. Inoltre, implementa collegamenti linguistici in tutti i file tradotti per consentire una facile navigazione tra versioni linguistiche diverse.
  </span>
</div>

## Sommario

- [Translate-MD: script di traduzione Markdown](#translate-md-script-di-traduzione-markdown)
  - [Sommario](#sommario)
  - [Funzioni](#caratteristiche)
  - [Installazione](#installazione)
    - [Installa dipendenze](#installa-le-dipendenze)
    - [Controllo delle dipendenze](#controllo-delle-dipendenze)
    - [Opzione 1: installazione ed esecuzione in un ambiente virtuale (consigliato)](#opzione-1-installazione-ed-esecuzione-in-un-ambiente-virtuale-consigliato)
    - [Opzione 2: installazione a livello di sistema](#opzione-2-installazione-a-livello-di-sistema)
    - [Installazione alternativa di googletrans dal repository GitHub (non consigliata)](#installazione-alternativa-di-googletrans-dal-repository-github-non-consigliata)
  - [Utilizzo](#utilizzo)
    - [Riepilogo dei parametri](#riepilogo-dei-parametri)
    - [1. Utilizzo standard con i parametri predefiniti](#1-utilizzo-standard-con-parametri-standard)
    - [2. Specificare un file modello specifico e una directory di output](#2-specificando-un-file-modello-specifico-e-una-directory-di-output)
    - [3. Impostazione di un prefisso e di un nome file personalizzati per il documento principale](#3-impostare-un-prefisso-e-un-nome-file-personalizzati-per-il-documento-principale)
    - [4. Utilizzando un file di configurazione](#4-utilizzando-un-file-di-configurazione)
    - [5. Combinazione di parametri della riga di comando e file di configurazione](#5-combinazione-di-parametri-della-riga-di-comando-e-file-di-configurazione)
    - [6. Come utilizzare l'opzione di disattivazione del collegamento vocale](#6-utilizzando-lopzione-per-disabilitare-i-collegamenti-vocali)
    - [7. Uso combinato di tutte le opzioni](#7-utilizzo-combinato-di-tutte-le-opzioni)
    - [8. Visualizza informazioni sulla versione](#8-visualizza-le-informazioni-sulla-versione)
    - [9. Mostra aiuto](#9-mostra-aiuto)
    - [10. Esempio con collegamenti linguistici disabilitati e utilizzo di un prefisso diverso](#10-esempio-con-collegamenti-linguistici-disabilitati-e-utilizzo-di-un-prefisso-diverso)
    - [11. Utilizzando la forma breve delle opzioni](#11-utilizzo-della-forma-abbreviata-delle-opzioni)
  - [Esempio di integrazione delle azioni GitHub](#esempio-di-integrazione-di-github-actions)

## Caratteristiche

- **Riconoscimento automatico della lingua**: `Translate-MD`riconosce automaticamente la lingua di partenza dal modello.
- **Traduzione multilingue**: `Translate-MD`traduce il contenuto in diverse lingue, che possono essere integrate nello script sotto `TARGET_LANGUAGES` o facoltativamente tramite un file di configurazione json, se necessario.
- **Preserva la formattazione**: blocchi di codice, ancoraggi e intestazioni vengono identificati e trattati separatamente per preservarne la funzionalità.
- **Link di navigazione in lingua**: verrà aggiunto o aggiornato un file principale con collegamenti ad altre traduzioni, nonché collegamenti all'interno di ciascun file tradotto per consentire al lettore di passare facilmente da una versione all'altra della lingua.

## installazione

Utilizza `curl` per scaricare lo script direttamente in una posizione a tua scelta:

```bash
curl -o translate-md.py https://raw.githubusercontent.com/dbt1/translate-md/master/translate-md.py
```

**O**

Utilizza `git clone` per clonare l'intera fonte in una posizione a tua scelta:

```bash
git clone https://github.com/dbt1/translate-md.git
```

Puoi eseguire `Translate-MD` da una posizione a tua scelta, direttamente dove si trova dopo la clonazione o nella stessa directory in cui si trova il modello Markdown (predefinito: `template.md`). Se `Translate-MD` deve essere eseguito direttamente, lo script deve essere reso eseguibile modificando i permessi a seconda del sistema.

```bash
chmod +x dateiname.py
```

### Installa le dipendenze

Se non è già disponibile, `Translate-MD` richiede ancora **googletrans 3.1.0a0**:

   > **Nota:** l'ultima versione "stabile" di `googletrans` potrebbe causare problemi. La versione `3.1.0a0` è solitamente più stabile e funziona meglio.

### Controllo delle dipendenze

Ecco come puoi verificare se i moduli richiesti sono stati installati correttamente:

```bash
python3 -c "from googletrans import Translator; print('Installation erfolgreich')"
```

### Opzione 1: installazione ed esecuzione in un ambiente virtuale (consigliato)

Per fare ciò, passa alla directory da cui desideri eseguire `Translate-MD`!

Crea un ambiente virtuale, attiva e installa `googletrans`:

   ```bash
   python3 -m venv venv && source venv/bin/activate && pip install googletrans==3.1.0a0 && pip install --upgrade setuptools
   ```


### Opzione 2: installazione a livello di sistema

Se non desideri utilizzare un ambiente virtuale e il tuo sistema lo consente, cosa che non è sempre il caso, ad esempio, di Ubuntu o Debian, puoi anche installare i moduli richiesti a livello globale:

```bash
pip install googletrans==3.1.0a0
```

### Installazione alternativa di googletrans dal repository GitHub (non consigliata)

  Se riscontri problemi, puoi provare a installare `googletrans` direttamente da GitHub:

  ```bash
  pip install git+https://github.com/ssut/py-googletrans.git
  ```

Potrai quindi eseguire `Translate-MD` come al solito.

## utilizzo

Ecco alcuni esempi di come è possibile utilizzare lo script con tutti i parametri possibili:

---

### Riepilogo dei parametri

@TABELLA_0@
---

I seguenti esempi dovrebbero aiutarti a utilizzare lo script in modo flessibile e in base alle tue esigenze.

### 1. Utilizzo standard con parametri standard

```bash
python translate-md.py
```

**Descrizione:**
- **File modello:** `template.md` deve già esistere nella stessa directory di `translate-md.py`!
- **Directory di output:** directory corrente (`.`)
- **Prefisso file:** `DOC_`
- **Documento principale:** `DOC.md`
- **File di configurazione:** Non utilizzato
- **Collegamenti lingua:** Abilitato

---

### 2. Specificando un file modello specifico e una directory di output

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations
```

**Descrizione:**
- **File modello:** `path/to/my_template.md`
- **Directory di output:** `path/to/translations`
- **Altri parametri:** Valori predefiniti
- **Collegamenti lingua:** Abilitato

---

### 3. Impostare un prefisso e un nome file personalizzati per il documento principale

```bash
python translate-md.py -p README_ -m main_README.md
```

**Descrizione:**
- **Prefisso file:** `README_`
- **Documento principale:** `main_README.md`
- **Altri parametri:** Valori predefiniti
- **Collegamenti lingua:** Abilitato

---

### 4. Utilizzando un file di configurazione

**Formattazione parametri:**
Nel file di configurazione, i parametri devono essere specificati come coppie chiave-valore. Tutte le chiavi (la chiave `config-file` non ha molto senso ;)) corrispondono ai nomi lunghi dei parametri della riga di comando senza `--` all'inizio. Per esempio:

- `template_md` corrisponde a `--template-md`
- `output_dir` corrisponde a `--output-dir`
- `prefix` corrisponde a `--prefix`
- `main_doc` corrisponde a `--main-doc`
- `no_language_links` corrisponde a `--no-language-links`

Supponiamo di avere un `config.json` con il seguente contenuto:

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

**Comando:**

```bash
python translate-md.py -c path/to/config.json
```

**Descrizione:**
- **Parametri:** Sono presi da `config.json`. Tutti gli altri parametri non immessi utilizzano le impostazioni predefinite.

   > **Nota:** Il valore predefinito `target_languages` può essere utilizzato solo tramite il file di configurazione, altrimenti vengono utilizzati solo `de` e `en`.


### 5. Combinazione di parametri della riga di comando e file di configurazione

Se nel file di configurazione non è definito un parametro, è possibile applicarlo come al solito con i parametri della riga di comando.

   > **Nota:** le impostazioni nel file di configurazione hanno la precedenza, il che significa che i parametri della riga di comando vengono ignorati se sono già stati immessi nel file di configurazione.

**Comando:**

```bash
python translate-md.py -c config.json -p DOC_ -n
```

**Descrizione:**
- **File modello, directory di output, documento principale:** Da `config.json`
- **Prefisso file:** Sovrascrive il valore definito in `config.json` e imposta su `DOC_`
- **Link lingua:** Disabilitato (`-n` o `--no-language-links`)

---

### 6. Utilizzando l'opzione per disabilitare i collegamenti vocali

```bash
python translate-md.py -n
```

**Descrizione:**
- **Collegamenti lingua:** Disabilitato
- **Documento principale:** Non creato
- **Altri parametri:** Valori predefiniti
- **Messaggio di avviso:** Lo script emette un avviso che l'opzione `-m` verrà ignorata.

---

### 7. Utilizzo combinato di tutte le opzioni

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations -p README_ -m main_README.md -c config.json --no-language-links
```

**Descrizione:**
- **File modello:** `path/to/my_template.md` (dalla riga di comando)
- **Directory di output:** `path/to/translations` (dalla riga di comando)
- **Prefisso file:** `README_` (da riga di comando)
- **Documento principale:** `main_README.md` (dalla riga di comando, ma viene ignorato)
- **File di configurazione:** `config.json` (può contenere impostazioni aggiuntive)
- **Link lingua:** Disabilitato (`--no-language-links`)
- **Messaggio di avviso:** Lo script avverte che l'opzione `-m` verrà ignorata.

---

### 8. Visualizza le informazioni sulla versione

```bash
python translate-md.py --version
```

**Descrizione:**
- **Funzione:** Visualizza la versione dello script e interrompe l'esecuzione.

---

### 9. Mostra aiuto

```bash
python translate-md.py --help
```

**Descrizione:**
- **Funzione:** Visualizza un messaggio di aiuto con tutte le opzioni disponibili e le relative descrizioni.

---

### 10. Esempio con collegamenti linguistici disabilitati e utilizzo di un prefisso diverso

```bash
python translate-md.py -p LANG_ -n
```

**Descrizione:**
- **Prefisso file:** `LANG_`
- **Collegamenti lingua:** Disabilitato
- **Documento principale:** Non creato
- **Altri parametri:** Valori predefiniti

---

### 11. Utilizzo della forma abbreviata delle opzioni

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations -p DOC_ -m main_README.md -c config.json -n
```

**Descrizione:**
- **Opzioni brevi:** `-t`, `-o`, `-p`, `-m`, `-c`, `-n`
- **Funzionalità:** Equivalente all'utilizzo combinato di tutte le opzioni lunghe.


## Esempio di integrazione di GitHub Actions

`Translate-MD` può essere utilizzato anche in GitHub Actions, ad esempio, per tradurre automaticamente un file README durante determinati eventi (ad esempio dopo un push al ramo principale).
  
> **Nota sulle autorizzazioni di GitHub Actions**: affinché il flusso di lavoro di GitHub Actions disponga delle autorizzazioni necessarie per inviare modifiche al repository, potrebbe essere necessario impostare un `Personal Access Token (PAT)` nel tuo account. Questo token è necessario per garantire l'autenticazione, soprattutto se hai bisogno delle autorizzazioni di scrittura per eseguire il push nei tuoi repository. Per ulteriori informazioni sulla configurazione di un `PAT`, consulta la [documentazione sulla configurazione del token GitHub](https://docs.github.com/en/enterprise-server@3.1/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Ecco un esempio di un `YAML-Datei` che deve essere creato e inserito in `.github/workflows/` se non esiste già.

Il presupposto qui è che tu voglia creare file README.md localizzati che si trovano nella directory root del tuo repository.
Questo esempio utilizza un file modello `template.md` che è già stato salvato nella directory principale del tuo repository. Le traduzioni vengono inviate anche alla directory root `.`. In questo caso si presuppone che vengano apportate modifiche a questo modello e che il push controlli se sono state apportate modifiche a questo file. In tal caso viene attivato il flusso di lavoro specificato nella sezione `on` sotto `push`. Il ramo `master` e il modello `template.md` vengono monitorati. È importante che siano attivati ​​i permessi di scrittura, che dovranno essere inseriti nella sezione `permissions`. Ulteriori voci assicurano che l'ambiente necessario sia configurato con alcune dipendenze per poter infine inserire le modifiche nel repository.

`[ci skip]` viene aggiunto al commit finale. Questo per evitare che il commit attivi nuovamente il flusso di lavoro se non è desiderato. Ciò potrebbe risparmiare risorse non necessarie ed evitare loop. 


  **Nota:** è opportuno testare un flusso di lavoro localmente. Ulteriori informazioni su questo [qui](https://github.com/nektos/act)!

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
