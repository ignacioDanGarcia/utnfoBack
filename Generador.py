from EvaluadorConflictos import EvaluadorConflictos
from Planificador import asignar_examenes
class Generador:
    def __init__(self):
        self.evaluador = EvaluadorConflictos()
    def generar_asignaciones_y_evaluar(self,materias, alumnos_materias, n_iteraciones=2000):
        mejores_asignaciones = []
        min_conflictos = float('inf')
        
        for _ in range(n_iteraciones):
            asignacion = asignar_examenes(materias)
            conflictos = self.evaluador.evaluar_conflictos(asignacion, alumnos_materias)
            
            # Si esta asignación tiene menos conflictos, la guardamos
            if conflictos < min_conflictos:
                mejores_asignaciones = [asignacion]
                min_conflictos = conflictos
            elif conflictos == min_conflictos:
                mejores_asignaciones.append(asignacion)
        
        # Devolvemos las asignaciones con el menor número de conflictos
        return mejores_asignaciones, min_conflictos