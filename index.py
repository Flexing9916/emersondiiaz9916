from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Inicio')
def Inicio():
    return render_template('inicio.html')

@app.route('/Nosotros')
def Nosotros():
    return render_template('nosotros.html')

@app.route('/Sesion')
def Sesion():
    return render_template('sesion.html')

if __name__ == '__main__':
    app.run(port=5020)