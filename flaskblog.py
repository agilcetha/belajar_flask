from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hallo, cuy!"

@app.route('/about')
def hello():
    return "about,!"

if __name__ == "__main__":
    app.run(debug=True)