from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    front = request.form['front']
    back = request.form['back']

    # Pasar los datos del frente y reverso a la plantilla
    return render_template('result.html', anki_card={'front': front, 'back': back})

if __name__ == '__main__':
    app.run(debug=True)
