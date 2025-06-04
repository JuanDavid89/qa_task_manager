from flask import Flask, request, Response
from collections import OrderedDict
import json

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Convertir lista de OrderedDicts a JSON con orden preservado
    response = json.dumps(tasks, indent=4)
    return Response(response, mimetype='application/json')

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    if not data:
        return Response(json.dumps({'error': 'JSON inválido o vacío'}, indent=4), mimetype='application/json'), 400

    if 'id' in data:
        return Response(json.dumps({'error': 'No se permite enviar el campo "id"'}, indent=4), mimetype='application/json'), 400

    if 'title' not in data:
        return Response(json.dumps({'error': 'El campo "title" es obligatorio'}, indent=4), mimetype='application/json'), 400

    description = data.get('description', '')

    new_task = OrderedDict([
        ('id', len(tasks) + 1),
        ('title', data['title']),
        ('description', description)
    ])

    tasks.append(new_task)

    response = json.dumps(new_task, indent=4)
    return Response(response, mimetype='application/json'), 201

if __name__ == '__main__':
    app.run(debug=True)
