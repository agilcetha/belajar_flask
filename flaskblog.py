from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "Content 1",
        "date_posted": "May, 28 2022"
    },
    {
        "author": "Corey Schafer",
        "title": "Blog Post 2",
        "content": "Content 2",
        "date_posted": "May, 27 2022"   
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About page")


if __name__ == '__main__':
    app.run(debug=True)