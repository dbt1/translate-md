<!-- LANGUAGE_LINKS_START -->
[🇩🇪 German](README_de.md) | [🇬🇧 English](README_en.md) | <span style="color: grey;">🇪🇸 Spanish</span> | [🇫🇷 French](README_fr.md) | [🇮🇹 Italian](README_it.md)
<!-- LANGUAGE_LINKS_END -->

# Translate-MD: script de traducción Markdown

<div style="display: flex; align-items: center;">
  <img src="translate-md.png" alt="translate-md" style="width: 64px; margin-right: 10px;">
  <span>Translate-MD es un script de Python y se utiliza para traducir archivos a varios idiomas desde una plantilla de documento de Markdown, como template.md, y para guardarlos en idiomas de destino específicos. El contenido codificado, como bloques de código, anclajes y encabezados, debe conservarse durante el proceso de traducción. <br>
  Utiliza Google Translator para traducir automáticamente el contenido sin modificar ciertas secciones. Además, implementa enlaces de idiomas en todos los archivos traducidos para permitir una fácil navegación entre versiones de diferentes idiomas.
  </span>
</div>

## Tabla de contenido

- [Translate-MD: script de traducción Markdown](#translate-md-script-de-traducción-markdown)
  - [Tabla de contenido](#tabla-de-contenido)
  - [Características](#características)
  - [Instalación](#instalación)
    - [Instalar dependencias](#instalar-dependencias)
    - [Comprobación de dependencia](#comprobación-de-dependencia)
    - [Opción 1: Instalar y ejecutar en un entorno virtual (recomendado)](#opción-1-instalar-y-ejecutar-en-un-entorno-virtual-recomendado)
    - [Opción 2: instalación en todo el sistema](#opción-2-instalación-en-todo-el-sistema)
    - [Instalación alternativa de googletrans desde el repositorio de GitHub (no recomendado)](#instalación-alternativa-de-googletrans-desde-el-repositorio-de-github-no-recomendado)
  - [Uso](#usar)
    - [Resumen de parámetros](#resumen-de-parámetros)
    - [1. Uso estándar con los parámetros predeterminados](#1-uso-estándar-con-los-parámetros-estándar)
    - [2. Especificación de un archivo de plantilla específico y un directorio de salida](#2-especificar-un-archivo-de-plantilla-específico-y-un-directorio-de-salida)
    - [3. Configurar un prefijo de archivo personalizado y un nombre para el documento principal](#3-establezca-un-prefijo-de-archivo-personalizado-y-un-nombre-para-el-documento-principal)
    - [4. Usando un archivo de configuración](#4-usando-un-archivo-de-configuración)
    - [5. Combinación de parámetros de línea de comando y archivo de configuración](#5-combinación-de-parámetros-de-línea-de-comando-y-archivo-de-configuración)
    - [6. Cómo utilizar la opción de desactivación del enlace de voz](#6-usar-la-opción-para-desactivar-los-enlaces-de-voz)
    - [7. Uso combinado de todas las opciones](#7-uso-combinado-de-todas-las-opciones)
    - [8. Ver información de la versión](#8-ver-información-de-la-versión)
    - [9. Mostrar ayuda](#9-mostrar-ayuda)
    - [10. Ejemplo con enlaces de idiomas deshabilitados y usando un prefijo diferente](#10-ejemplo-con-enlaces-de-idiomas-deshabilitados-y-usando-un-prefijo-diferente)
    - [11. Usando la forma corta de opciones](#11-uso-de-la-forma-corta-de-opciones)
  - [Ejemplo de integración de acciones de GitHub](#ejemplo-de-integración-de-github-actions)

## Características

- **Reconocimiento automático de idioma**: `Translate-MD` reconoce automáticamente el idioma de origen de la plantilla.
- **Traducción multilingüe**: `Translate-MD`traduce el contenido a varios idiomas, que se pueden complementar en el script en `TARGET_LANGUAGES` u opcionalmente a través de un archivo de configuración json si es necesario.
- **Conserva el formato**: los bloques de código, los anclajes y los encabezados se identifican y tratan por separado para preservar su funcionalidad.
- **Enlaces de navegación de idiomas**: se agregará o actualizará un archivo principal con enlaces a otras traducciones, así como enlaces dentro de cada archivo traducido, para permitir al lector cambiar fácilmente entre diferentes versiones de idiomas.

## instalación

Utilice `curl` para descargar el script directamente a la ubicación que elija:

```bash
curl -o translate-md.py https://raw.githubusercontent.com/dbt1/translate-md/master/translate-md.py
```

**o**

Utilice `git clone` para clonar toda la fuente en la ubicación que elija:

```bash
git clone https://github.com/dbt1/translate-md.git
```

Puede ejecutar `Translate-MD` desde la ubicación que elija, ya sea directamente donde está después de la clonación o en el mismo directorio donde se encuentra la plantilla Markdown (predeterminada: `template.md`). Si `Translate-MD` se va a ejecutar directamente, el script debe hacerse ejecutable cambiando el permiso según el sistema.

```bash
chmod +x dateiname.py
```

### Instalar dependencias

Si aún no está disponible, `Translate-MD` aún requiere **googletrans 3.1.0a0**:

   > **Nota:** La última versión "estable" de `googletrans` puede causar problemas. La versión `3.1.0a0` suele ser más estable y funciona mejor.

### Comprobación de dependencia

Así puede comprobar si los módulos necesarios se han instalado correctamente:

```bash
python3 -c "from googletrans import Translator; print('Installation erfolgreich')"
```

### Opción 1: instalar y ejecutar en un entorno virtual (recomendado)

Para hacer esto, cambie al directorio desde donde desea ejecutar `Translate-MD`.

Cree un entorno virtual, active e instale `googletrans`:

   ```bash
   python3 -m venv venv && source venv/bin/activate && pip install googletrans==3.1.0a0 && pip install --upgrade setuptools
   ```


### Opción 2: instalación en todo el sistema

Si no quieres utilizar un entorno virtual y tu sistema lo permite, lo que no siempre es el caso con Ubuntu o Debian, por ejemplo, también puedes instalar los módulos necesarios de forma global:

```bash
pip install googletrans==3.1.0a0
```

### Instalación alternativa de googletrans desde el repositorio de GitHub (no recomendado)

  Si tiene problemas, puede intentar instalar `googletrans` directamente desde GitHub:

  ```bash
  pip install git+https://github.com/ssut/py-googletrans.git
  ```

Luego puedes ejecutar `Translate-MD` como de costumbre.

## usar

A continuación se muestran varios ejemplos de cómo puede utilizar el script con todos los parámetros posibles:

---

### Resumen de parámetros

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

Los siguientes ejemplos le ayudarán a utilizar el script de forma flexible y según sus necesidades.

### 1. Uso estándar con los parámetros estándar.

```bash
python translate-md.py
```

**Descripción:**
- **Archivo de plantilla:** `template.md` ya debe existir en el mismo directorio que `translate-md.py`.
- **Directorio de salida:** directorio actual (`.`)
- **Prefijo de archivo:** `DOC_`
- **Documento principal:** `DOC.md`
- **Archivo de configuración:** No utilizado
- **Enlaces de idiomas:** Habilitado

---

### 2. Especificar un archivo de plantilla específico y un directorio de salida

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations
```

**Descripción:**
- **Archivo de plantilla:** `path/to/my_template.md`
- **Directorio de salida:** `path/to/translations`
- **Otros parámetros:** Valores predeterminados
- **Enlaces de idiomas:** Habilitado

---

### 3. Establezca un prefijo de archivo personalizado y un nombre para el documento principal.

```bash
python translate-md.py -p README_ -m main_README.md
```

**Descripción:**
- **Prefijo de archivo:** `README_`
- **Documento principal:** `main_README.md`
- **Otros parámetros:** Valores predeterminados
- **Enlaces de idiomas:** Habilitado

---

### 4. Usando un archivo de configuración

**Formato de parámetros:**
En el archivo de configuración, los parámetros deben especificarse como pares clave-valor. Todas las claves (la clave `config-file` realmente no tiene sentido;)) corresponden a los nombres largos de los parámetros de la línea de comando sin `--` al principio. Por ejemplo:

- `template_md` corresponde a `--template-md`
- `output_dir` corresponde a `--output-dir`
- `prefix` corresponde a `--prefix`
- `main_doc` corresponde a `--main-doc`
- `no_language_links` corresponde a `--no-language-links`

Supongamos que tiene un `config.json` con el siguiente contenido:

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

**Dominio:**

```bash
python translate-md.py -c path/to/config.json
```

**Descripción:**
- **Parámetros:** Se toman del `config.json`. Todos los demás parámetros no ingresados ​​utilizan la configuración predeterminada.

   > **Nota:** El `target_languages` predeterminado solo se puede usar a través del archivo de configuración; de lo contrario, solo se usan `de` y `en`.


### 5. Combinación de parámetros de línea de comando y archivo de configuración

Si el archivo de configuración no tiene un parámetro definido, puede aplicarlo como de costumbre con los parámetros de la línea de comando.

   > **Nota:** Las configuraciones en el archivo de configuración tienen prioridad, lo que significa que los parámetros de la línea de comando se ignoran si ya se ingresaron en el archivo de configuración.

**Dominio:**

```bash
python translate-md.py -c config.json -p DOC_ -n
```

**Descripción:**
- **Archivo de plantilla, directorio de salida, documento principal:** Del `config.json`
- **Prefijo de archivo:** Sobrescribe el valor definido en `config.json` y lo establece en `DOC_`
- **Enlaces de idiomas:** Deshabilitado (`-n` o `--no-language-links`)

---

### 6. Usar la opción para desactivar los enlaces de voz.

```bash
python translate-md.py -n
```

**Descripción:**
- **Enlaces de idiomas:** Deshabilitado
- **Documento principal:** No creado
- **Otros parámetros:** Valores predeterminados
- **Mensaje de advertencia:** El script emite una advertencia de que se ignorará la opción `-m`.

---

### 7. Uso combinado de todas las opciones.

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations -p README_ -m main_README.md -c config.json --no-language-links
```

**Descripción:**
- **Archivo de plantilla:** `path/to/my_template.md` (desde la línea de comando)
- **Directorio de salida:** `path/to/translations` (desde la línea de comando)
- **Prefijo de archivo:** `README_` (desde la línea de comando)
- **Documento principal:** `main_README.md` (desde la línea de comando, pero se ignora)
- **Archivo de configuración:** `config.json` (puede contener configuraciones adicionales)
- **Enlaces de idiomas:** Deshabilitado (`--no-language-links`)
- **Mensaje de advertencia:** El script advierte que la opción `-m` será ignorada.

---

### 8. Ver información de la versión

```bash
python translate-md.py --version
```

**Descripción:**
- **Función:** Muestra la versión del script y detiene la ejecución.

---

### 9. Mostrar ayuda

```bash
python translate-md.py --help
```

**Descripción:**
- **Función:** Muestra un mensaje de ayuda con todas las opciones disponibles y sus descripciones.

---

### 10. Ejemplo con enlaces de idiomas deshabilitados y usando un prefijo diferente

```bash
python translate-md.py -p LANG_ -n
```

**Descripción:**
- **Prefijo de archivo:** `LANG_`
- **Enlaces de idiomas:** Deshabilitado
- **Documento principal:** No creado
- **Otros parámetros:** Valores predeterminados

---

### 11. Uso de la forma corta de opciones.

```bash
python translate-md.py -t path/to/my_template.md -o path/to/translations -p DOC_ -m main_README.md -c config.json -n
```

**Descripción:**
- **Opciones cortas:** `-t`, `-o`, `-p`, `-m`, `-c`, `-n`
- **Funcionalidad:** Equivale a usar todas las opciones largas combinadas.


## Ejemplo de integración de GitHub Actions

`Translate-MD` también se puede usar en GitHub Actions, por ejemplo, para traducir automáticamente un archivo README durante ciertos eventos (por ejemplo, después de enviarlo a la rama maestra).
  
> **Nota sobre los permisos de GitHub Actions**: Para que el flujo de trabajo de GitHub Actions tenga los permisos necesarios para enviar cambios al repositorio, es posible que necesites configurar un `Personal Access Token (PAT)` en tu cuenta. Este token es necesario para garantizar la autenticación, especialmente si necesita permisos de escritura para enviar a sus repositorios. Para obtener más información sobre cómo configurar un `PAT`, consulte la [documentación de configuración del token de GitHub](https://docs.github.com/en/enterprise-server@3.1/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

A continuación se muestra un ejemplo de un `YAML-Datei` que debe crearse y colocarse en `.github/workflows/` si aún no existe.

La suposición aquí es que desea crear archivos README.md localizados que se encuentran en el directorio raíz de su repositorio.
Este ejemplo utiliza un archivo de plantilla `template.md` que ya se ha guardado en el directorio raíz de su repositorio. Las traducciones también se envían al directorio raíz `.`. En este caso, se supone que se realizan ajustes en esta plantilla y que el push verifica si se han realizado cambios en este archivo. Si este es el caso, se activa este flujo de trabajo, que se especifica en la sección `on` bajo `push`. Se monitorean la rama `master` y la plantilla `template.md`. Es importante que estén activados los permisos de escritura, los cuales deben ingresarse en la sección `permissions`. Las entradas adicionales garantizan que el entorno necesario esté configurado con algunas dependencias para, en última instancia, enviar los cambios al repositorio.

`[ci skip]` se agrega a la confirmación final. Esto es para evitar que la confirmación active nuevamente el flujo de trabajo si no es así. Esto podría ahorrar recursos innecesarios y evitar bucles. 


  **Nota:** Tiene sentido probar un flujo de trabajo localmente. ¡Más información sobre esto [aquí](https://github.com/nektos/act)!

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
