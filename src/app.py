from flask import Flask,jsonify, request, render_template
from flask_mysqldb import MySQL
from config import config



app = Flask(__name__)

conexion= MySQL(app)

#conexion index HTML
@app.route('/')
def inicio():
    return render_template('index.html')



#Mostrar tareas
@app.route('/tareas')
def listar_tareas():
    try:
       cursor=conexion.connection.cursor()
       sql="SELECT id, titulo, completado FROM trabajadores_tareas"
       cursor.execute(sql)
       datos=cursor.fetchall()
       tareas=[]
       for fila in datos:
           tarea={'id':fila[0],'titulo':fila[1], 'completado': fila[2]}
           tareas.append(tarea)
       return jsonify({'tareas':tareas, 'mensaje':"tareas listadas."})
    except Exception as ex:
        return jsonify({'mensaje':"Error"})


@app.route('/tareas/<id>', methods=['GET'])
def leer_tareas(id):
    try:
        cursor= conexion.connection.cursor()
        sql= "SELECT id, titulo, completado FROM trabajadores_tareas WHERE id ='{0}'".format(id)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            tarea={'id':datos[0],'titulo':datos[1], 'completado': datos[2]}
            return jsonify({'tareas':tarea, 'mensaje':"tarea encontrada."})
        else:
            return jsonify({'mensaje':"Error: Tarea no encontrada"})
    except Exception as ex:
        return jsonify({'mensaje':"Error"})
        

#registrar tareas
@app.route('/tareas/', methods=['POST'])

def registrar_tarea():
    try:
        data = request.json

        # Validar que existan todos los campos necesarios
        if not all(k in data for k in ('id', 'titulo', 'completado')):
            return jsonify({'mensaje': "Faltan datos en el cuerpo JSON"}), 400

        cursor = conexion.connection.cursor()
        sql = "INSERT INTO trabajadores_tareas (id, titulo, completado) VALUES (%s, %s, %s)"
        valores = (data['id'], data['titulo'], data['completado'])
        cursor.execute(sql, valores)
        conexion.connection.commit()
        return jsonify({'mensaje': "Tarea registrada correctamente"}), 201

    except Exception as ex:
        # Para depurar mejor, devuelve el error real
        return jsonify({'mensaje': f"Error: {str(ex)}"}), 500

#Eliminar tarea
@app.route('/tareas/<id>', methods=['DELETE'])
def borrar_tarea(id):
    try:
        cursor= conexion.connection.cursor()
        sql= "DELETE FROM trabajadores_tareas WHERE id ='{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje':"Tarea eliminada."})
    except Exception as ex:
        return jsonify({'mensaje':"Error"})
        

#Actualizar tarea
@app.route('/tareas/<id>', methods=['PUT'])

def actualizar_tarea(id):
    try:
        data = request.json

        # Solo validar los campos que deben venir en el JSON (titulo y completado)
        if not all(k in data for k in ('titulo', 'completado')):
            return jsonify({'mensaje': "Faltan datos en el cuerpo JSON"}), 400

        cursor = conexion.connection.cursor()

        # Verificar si la tarea existe antes de actualizar
        cursor.execute("SELECT * FROM trabajadores_tareas WHERE id = %s", (id,))
        tarea = cursor.fetchone()
        if tarea is None:
            return jsonify({'mensaje': "Tarea no encontrada"}), 404

        # Hacer la actualización de forma segura
        sql = "UPDATE trabajadores_tareas SET titulo = %s, completado = %s WHERE id = %s"
        valores = (data['titulo'], data['completado'], id)
        cursor.execute(sql, valores)
        conexion.connection.commit()

        return jsonify({'mensaje': "Tarea actualizada correctamente"}), 200

    except Exception as ex:
        return jsonify({'mensaje': f"Error: {str(ex)}"}), 500


#Validacion pagina no encontrada
def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada<h1>",404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.config.from_object(config['development']) 
    app.debug = True
    app.run()