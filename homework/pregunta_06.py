"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import glob
import os
import pandas as pd

def lsi(input_directory,filename):
    
    file = glob.glob(f"{input_directory}/*")
    file_path = os.path.join(input_directory, filename)
    dataframe =pd.read_csv(
            file_path,
            delimiter='\t',
        )

    return dataframe

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    df = lsi("files/input","tbl1.tsv")
    resultado = sorted(df.iloc[:,1].str.upper().unique())
    return resultado

if __name__ == '__main__':
    print(pregunta_06())

'''    df = lsi("files/input","tbl1.tsv")
    df = df.iloc[:,1]
    elements =[]
    for element in df:
        if element.upper() not in elements:
            elements.append(element.upper())
        else:
            continue
    elements = list(sorted(elements))
    return elements'''