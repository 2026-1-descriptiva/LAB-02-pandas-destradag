"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import os
import pandas as pd
import glob

def load_specific_inpunt(input_directory,filename):
    
    file = glob.glob(f"{input_directory}/*")
    #file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(input_directory, filename)
    dataframe =pd.read_csv(
            file_path,
            delimiter='\t',
        )

    return dataframe

def pregunta_01():

    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40 """

    table = load_specific_inpunt("files/input/",'tbl0.tsv')
    files, cols = table.shape
    return(files)


if __name__ == '__main__':
    print(pregunta_01())

