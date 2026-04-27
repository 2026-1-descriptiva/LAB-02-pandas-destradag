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

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    dftbl0 = lsi("files/input","tbl0.tsv")
    dftbl2 = lsi("files/input","tbl2.tsv")
    df = pd.merge(dftbl0,dftbl2, on='c0')
    df = df.groupby('c1')['c5b'].sum().sort_index()
    return df

if __name__ == '__main__':
    print(pregunta_13())    