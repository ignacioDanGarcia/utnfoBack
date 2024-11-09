from ortools.sat.python import cp_model

def asignar_examenes(materias, dias_totales=10):
    model = cp_model.CpModel()
    dia_asignado = []
    for i in range(len(materias)):
        dia_asignado.append([model.NewBoolVar(f"materia_{i}_dia_{d}") for d in range(dias_totales)])

    # Restricción 1: No más de 4 exámenes por día
    for dia in range(dias_totales):
        model.Add(sum(dia_asignado[i][dia] for i in range(len(materias))) <= 4)

    # Restricción 2: No más de una materia del mismo cuatrimestre por día
    for dia in range(dias_totales):
        for cuatrimestre in range(1, 5):
            model.Add(sum(dia_asignado[i][dia] for i in range(len(materias)) if materias[i].cuatrimestre == cuatrimestre) <= 1)

    # Restricción 3: Cada materia debe ser asignada a exactamente un día
    for i in range(len(materias)):
        model.Add(sum(dia_asignado[i][dia] for dia in range(dias_totales)) == 1)

    # Restricción 4: Las correlativas deben estar asignadas a días anteriores
    for i, materia in enumerate(materias):
        for correlativa in materia.correlativas:
            correlativa_index = materias.index(correlativa)
            for dia in range(dias_totales):
                model.Add(dia_asignado[i][dia] <= sum(dia_asignado[correlativa_index][d] for d in range(dia)))
    
    # Resolver el modelo
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Verificar si se ha encontrado una solución
    asignacion = {}
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        for i, materia in enumerate(materias):
            for dia in range(dias_totales):
                if solver.Value(dia_asignado[i][dia]) == 1:
                    if dia not in asignacion:
                        asignacion[dia] = []
                    asignacion[dia].append(materia.nombre)
    return asignacion