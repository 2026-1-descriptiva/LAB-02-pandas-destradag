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

def pregunta_07():
    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: c2, dtype: int64
    """
    df = lsi("files/input","tbl0.tsv")
    resultado = df.groupby('c1')['c2'].sum().sort_index()
    return resultado

if __name__ == '__main__':
    print(pregunta_07())