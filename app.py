from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Carregar os processos do arquivo JSON
with open('processos.json', 'r', encoding='utf-8') as f:
    processos = json.load(f)

@app.route('/')
def index():
    areas = list(processos.keys())
    return render_template('index.html', areas=areas)

@app.route('/cargos/<area>')
def get_cargos(area):
    cargos = list(processos[area].keys())
    return jsonify(cargos)

@app.route('/processos/<area>/<cargo>')
def get_processos(area, cargo):
    processo_list = list(processos[area][cargo].keys())
    return jsonify(processo_list)

@app.route('/detalhes/<area>/<cargo>/<processo>')
def get_detalhes(area, cargo, processo):
    detalhes = processos[area][cargo][processo]
    return jsonify(detalhes)

if __name__ == '__main__':
    app.run(debug=True)
