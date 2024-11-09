from flask import Flask, request, jsonify
import pandas as pd
from Materia import  Materia
from LectorExcel import LectorExcel
from Generador import Generador
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

programacion1 = Materia("Programacion1", 1)
sistemas_operativos = Materia("SistemasOperativos", 1)
matematica1 = Materia("Matematica1", 1)
org_empresarial = Materia("OrganizacionEmpresarial", 1)

# Crear materias del Cuatrimestre 2
programacion2 = Materia("Programacion2", 2)
estadistica = Materia("Estadistica", 2)
bbdd = Materia("BasesDeDatos1", 2)
ingles1 = Materia("Ingles1", 2)

# Crear materias del Cuatrimestre 3
programacion3 = Materia("Programacion3", 3)
bbdd2 = Materia("BasesDeDatos2", 3)
meto_sistemas1 = Materia("MetodologiaSistemas1", 3)
ingles2 = Materia("Ingles2", 3)

# Crear materias del Cuatrimestre 4
programacion4 = Materia("Programacion4", 4)
meto_sistemas2 = Materia("MetodologiaSistemas2", 4)
analisis_datos = Materia("AnalisisDeDatos", 4)
legislacion = Materia("Legislacion", 4)
software = Materia("Software", 4)

# Asignar correlativas del Cuatrimestre 2
programacion2.agregar_correlativa(programacion1)
programacion2.agregar_correlativa(sistemas_operativos)
estadistica.agregar_correlativa(matematica1)
bbdd.agregar_correlativa(programacion1)
bbdd.agregar_correlativa(matematica1)

# Asignar correlativas del Cuatrimestre 3
programacion3.agregar_correlativa(programacion2)
programacion3.agregar_correlativa(bbdd)
bbdd2.agregar_correlativa(bbdd)
meto_sistemas1.agregar_correlativa(programacion2)
meto_sistemas1.agregar_correlativa(bbdd)
ingles2.agregar_correlativa(ingles1)

# Asignar correlativas del Cuatrimestre 4
programacion4.agregar_correlativa(programacion3)
programacion4.agregar_correlativa(bbdd2)
programacion4.agregar_correlativa(meto_sistemas1)
meto_sistemas2.agregar_correlativa(meto_sistemas1)
analisis_datos.agregar_correlativa(bbdd2)
legislacion.agregar_correlativa(bbdd)
software.agregar_correlativa(programacion3)
software.agregar_correlativa(bbdd2)

# Lista de todas las materias
materias = [
    programacion1, sistemas_operativos, matematica1, org_empresarial,
    programacion2, estadistica, bbdd, ingles1,
    programacion3, bbdd2, meto_sistemas1, ingles2,
    programacion4, meto_sistemas2, analisis_datos, legislacion, software
]

@app.route('/procesar', methods=['POST'])
def procesar_excel():
    if 'file' not in request.files:
        return jsonify({"error": "No se envió un archivo"}), 400

    file = request.files['file']
    try:
        
        #df = pd.read_excel(file)
        lector = LectorExcel()
        #archivo = os.path.join(os.getcwd(), '2\joja.xlsx')
        alumnos_materias = lector.leer_datos_excel(file)
        
        generador = Generador()
        mejores_asignaciones, min_conflictos = generador.generar_asignaciones_y_evaluar(materias, alumnos_materias)
        print(mejores_asignaciones[:3])
        return jsonify({"asignaciones": mejores_asignaciones[:3]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
