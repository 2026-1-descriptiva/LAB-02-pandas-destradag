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
    #file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(input_directory, filename)
    dataframe =pd.read_csv(
            file_path,
            delimiter='\t',
        )

    return dataframe

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    df = lsi("files/input","tbl0.tsv")
    result = df.iloc[:,1].value_counts().sort_index()
    return(result)

if __name__ == '__main__':
    print(pregunta_03())


'''    df = lsi("files/input","tbl0.tsv")
    letters = df.iloc[:,1]
    letters_count= {}
    for letter in letters:
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] =1
    letters_count = dict(sorted(letters_count.items()))
    letters_count = pd.Series(letters_count)

    return(letters_count)'''