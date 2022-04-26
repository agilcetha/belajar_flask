from flask import Flask

app = Flask (__name__)

@app.route("/helo")
def hello():
    return "halaman opo iki"

if __name__ == "__main__":
    app.run(debug = True)