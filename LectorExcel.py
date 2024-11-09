import pandas as pd

class LectorExcel:
    def __init__(self):
        pass
    def leer_datos_excel(self,ruta_archivo):
        df = pd.read_excel(ruta_archivo, header=None)
        df.columns = ['alumno', 'materiaARendir']
        alumnos_materias = [(row['alumno'], row['materiaARendir']) for _, row in df.iterrows()]
        return alumnos_materias