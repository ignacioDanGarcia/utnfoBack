class EvaluadorConflictos:
    def __init__(self):
        pass

    def evaluar_conflictos(self, asignacion, alumnos_materias):
        conflictos = 0
        
        # Procesamos cada alumno y su materia
        for alumno, materia in alumnos_materias:
            # Buscar en qué día está asignada la materia del alumno
            dia_materia = None
            for dia, materias in asignacion.items():
                if materia in materias:
                    dia_materia = dia
                    break
            
            # Si encontramos que la materia está asignada, verificamos los demás registros del alumno
            if dia_materia is not None:
                # Buscar otras materias que ese alumno tiene
                otras_materias = [materia_b for alumno_b, materia_b in alumnos_materias if alumno_b == alumno and materia_b != materia]
                
                # Verificamos si alguna de esas otras materias está asignada en el mismo día
                for otra_materia in otras_materias:
                    for dia, materias in asignacion.items():
                        if otra_materia in materias and dia == dia_materia:
                            conflictos += 1

        return round(conflictos / 2)
