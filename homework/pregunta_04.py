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


def pregunta_04():
    """
    Calcule el promedio de `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: c2, dtype: float64
    """
    df = lsi("files/input","tbl0.tsv")
    result = df.groupby('c1')['c2'].mean().sort_index()
    return result

if __name__ == '__main__':
    print(pregunta_04())
