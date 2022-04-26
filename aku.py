from flask import Flask

app = Flask (__name__)

@app.route("/")
def hello():
    return "halaman opo iki"

if __name__ == "__main__":
    app.run(debug=True) # penulisan debug=True tidak usah spasi