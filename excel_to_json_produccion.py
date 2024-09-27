# -*- coding: utf-8 -*-
import pandas as pd
import json
import re
from datetime import datetime
from pathlib import Path

def read_excel(file_name):
    try:
        #path = f"C:\\Users\\rtascon\\Documents\\Scripts\\create_tickets_tic\\plantilla\\{file_name}.xlsx"
        path = str(Path(__file__).resolve().parent) + f"/plantilla/{file_name}.xlsx"
        #df = pd.read_excel('C:\\Users\\rtascon\\Documents\\Scripts\\API_GLPI\\Codigos_iot.xlsx')
        df = pd.read_excel(path, sheet_name='Tickets')

        json_data = {"codigos":{}, "activos":{}, "ubicaciones":{}, "entidades":{}, "categorias":{}, "grupos":{}, "observadores":{}}

        for index, row in df.iterrows():
            
            aux_entidad = row['Entidad'].replace('\xa0', ' ')
            aux_activo = row['Activo'].replace('\xa0', ' ')
            aux_activo = aux_activo.strip()
            aux_grupo_asignado = row['Grupo asignado'].replace('\xa0', ' ')
            aux_entidad = aux_entidad.split(" > ")[-1]
            aux_grupo_asignado = aux_grupo_asignado.split(" > ")[-1]
            #json_data[row['Codigo']] = {"ubicacion":row['Ubicacion'], "id_ubicacion":row['id ubicacion'], "entidad":aux_entidad, "id_entidad":row['id entities'], "activo":aux_activo, "id_activo":row['id activo'], "categoria":row['Categoria'], "id_categoria" : row['id categoria'], "grupo_asignado" : aux_grupo_asignado, "id_grupo_asignado" : row['id grupo asignado'], "id_observador" : row['id observador']}
            json_data["codigos"][row['Codigo']] = {"id_ubicacion":row['id ubicacion'], "id_entidad":row['id entities'], "id_activo":row['id activo'], "id_categoria" : row['id categoria'], "id_grupo_asignado" : row['id grupo asignado'], "id_observador" : row['id observador'], "id_tipo" : row['id tipo']}
            json_data["ubicaciones"][str(row['id ubicacion'])] = row['Ubicacion']
            json_data["entidades"][str(row['id entities'])] = aux_entidad
            json_data["activos"][str(row['id activo'])] = aux_activo
            json_data["categorias"][str(row['id categoria'])] = row['Categoria']
            json_data["grupos"][str(row['id grupo asignado'])] = aux_grupo_asignado
            json_data["observadores"][str(row['id observador'])] = row['Observador']

        #json_data_new = json.dumps(json_data)
        return json_data
    
    except Exception as e:
        # Imprime el mensaje de error de la excepción
        print("Problema en la funcion read_excel")       
        print(f"Ocurrio un error: {e}")


def save_json_file(metadata, indent):
    try:
        fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = "json\\" + f"datos_{fecha_actual}.json"
        with open(nombre_archivo, "w") as archivo:
            json.dump(metadata, archivo, ensure_ascii=False, separators=(',', ':'))
        print("Archivo JSON generado exitosamente!")
    except:
        print("error al salvar json file")



def main():
    try:
        medatadata = read_excel("plantilla_estandar_tic")
        save_json_file(medatadata, 0)

    except:
        print("Problema en la funcion main")



if __name__ == "__main__":
    main()