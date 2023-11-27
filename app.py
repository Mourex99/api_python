from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Harry Potter - e a Camara Secreta',
        'autor': 'J. K. Rowling'
    },
    {
        'id': 2,
        'titulo': 'Codigo limpo',
        'autor': 'Robert Cecil Martin'
    },
    {
        'id': 3,
        'titulo': 'O Programador Pragmatico',
        'autor': 'Andy Hunt e Dave Thomas'
    },
]

#Consultar todos
@app.route('/livros' ,methods=['GET'])
def obter_livros():
    return jsonify(livros)
# Consultar(id)
# Editar
# Criar
# Excluir
app.run(port=5000,host='localhost',debug=True)