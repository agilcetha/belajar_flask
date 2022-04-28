from flask import Flask

app = Flask (__name__)

@app.route("/")
def hello():
    return "<h1>Hello RAHMAD</h1>"

if __name__ == "__main__":
    app.run(debug=True) # penulisan debug=True tidak usah spasi