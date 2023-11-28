from flask import Flask, render_template

app = Flask(__name__)

@app.route('/api/related_words/update_data')
def index():
    print("hallo")


@app.route('//<nome>')
def pagina(nome):
    return render_template('pagina.html', nome=nome)


if __name__ == '__main__':
    app.run(debug=True)
