from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Solo mostramos el formulario
    return render_template('index.html')

if __name__ == '__main__':
    # Ejecuta el servidor
    app.run(debug=True)