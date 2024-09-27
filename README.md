# Proyecto: Conversión de Excel a JSON para Zabbix

Este repositorio contiene un script en Python que convierte un archivo Excel (plantilla_estandar_tic.xls) en un archivo JSON que luego puede ser utilizado en Zabbix para crear tickets automáticos en GLPI. A continuación, se detallan las instrucciones para activar el entorno virtual, copiar la plantilla Excel y ejecutar el script para generar el archivo JSON.

## Requisitos Previos

- Python 3.x
- Virtualenv
- Zabbix (para importar el JSON generado)

## Instrucciones de Uso

1. **Clonar el repositorio**

    ```bash
    git clone git@github.com:rtascon/gia_tickets_tic.git
    cd gia_tickets_tic
    ```

2. **Activar un entorno virtual**

    Descomprimir el archivo venv_glpi.rar

    - **En Linux / MacOS**

        ```bash
        source venv_glpi/bin/activate
        ```

    - **En Windows**

        ```bash
        venv_glpi\Scripts\activate
        ```

3. **Copiar la plantilla Excel**

    Asegúrate de copiar el archivo Excel `plantilla_estandar_tic.xlsx` en el directorio `plantilla/` dentro del repositorio.

4. **Ejecutar el script**

    Para convertir el archivo Excel en JSON, ejecuta el siguiente comando:

    ```bash
    python3 excel_to_json_produccion.py
    ```

    Esto generará un archivo JSON en el directorio `json/`.

5. **Verificar la salida**

    El archivo JSON generado estará en el directorio `json/` con el nombre que definas en el script.

6. **Copiar el contenido en Zabbix**

    1. Abre la interfaz de Zabbix y navega hasta la sección de **Media Types**.
    2. Edita el "Media Type" correspondiente a GIA TIC.
    3. Copia el contenido del archivo JSON generado y pégalo en el campo correspondiente del "Media Type".

