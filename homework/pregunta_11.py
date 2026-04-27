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

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    df = lsi("files/input","tbl1.tsv")
    df = df.groupby('c0')['c4'].apply(lambda x: ",".join(map(str,sorted(x))))
    df = df.to_frame()
    df = df.reset_index()
    return df

if __name__ == '__main__':
    print(pregunta_11())

