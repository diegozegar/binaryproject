from flask import Flask, render_template, request
from binarios import calcularBinario

class conection():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/', methods=['POST'])
    def getvalue():
        texto = request.form['contenedorcodigo']
        resultado = calcularBinario(texto)
        print(texto)
        return render_template('index.html',resultado=resultado)

    if __name__ == '__main__':
        app.run(debug=True)