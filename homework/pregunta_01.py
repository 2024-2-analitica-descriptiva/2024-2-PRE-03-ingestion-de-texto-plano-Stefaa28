"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    #Lectura del archivo 
    with open('files/input/clusters_report.txt','r', encoding = 'utf-8') as file:
        lineas = file.readlines()

     # Procesar las líneas del archivo omitiendo las primeras cuatro líneas de encabezado
    texto = lineas[4:]
    
    #Definir las columnas en minúsculas, sin espacios y reemplazando por _  
    columnas = [["cluster","cantidad_de_palabras_clave","porcentaje_de_palabras_clave","principales_palabras_clave"]]
    
    # Inicializar listas para almacenar los datos
    lista = []

    p = True
      
    for linea in texto:
        linea.strip()
        linea = linea.split()
        print(linea)
        if len(linea) > 0 and p:
            lista.append(int(linea[0]))
            lista.append(int(linea[1]))
            lista.append(float(linea[2].replace(',','.')))
            lista.append(" ".join(linea[4:]))
            p = False
        
        elif len(linea) > 0:
            lista.append(" ".join(linea))
            
        else:
            p =True
            lista[3] = ' '.join(lista[3:]).replace('.', '')
            columnas.append(lista[:4])
            lista = []    
    return pd.DataFrame(columnas[1:], columns = columnas[0]) 

print(pregunta_01())