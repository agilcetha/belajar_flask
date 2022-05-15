from flask import Flask

app = Flask (__name__)

@app.route("/")
def home():
    return "<h1>Home AHSAN</h1>"

@app.route("/about")
def about():
    return "<h1>About  AHSAN</h1>"

if __name__ == "__main__":
    app.run(debug=True) # penulisan debug=True tidak usah spasi