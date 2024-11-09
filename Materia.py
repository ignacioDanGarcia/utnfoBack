from ortools.sat.python import cp_model

class Materia:
    def __init__(self, nombre, cuatrimestre):
        self.nombre = nombre
        self.cuatrimestre = cuatrimestre
        self.correlativas = []

    def agregar_correlativa(self, materia):
        self.correlativas.append(materia)

    def __repr__(self):
        correlativas_nombres = [materia.nombre for materia in self.correlativas]
        return f"Materia(nombre='{self.nombre}', cuatrimestre={self.cuatrimestre}, correlativas={correlativas_nombres})"


