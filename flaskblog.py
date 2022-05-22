from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'autor' : 'supri',
        'title' : 'blog post 1',
        'content' : 'first post content',
        'date_posted' : ' 22 Mei 2022'
    },
    {
        'autor' : 'Haidar',
        'title' : 'blog post 2',
        'content' : 'first post content',
        'date_posted' : ' 23 Mei 2022'
    }
]

@app.route('/')
def hello():
    return render_template("home.html", posts = posts)

@app.route('/about')
def about():
    return render_template("about.html", title = 'About')

if __name__ == "__main__":
    app.run(debug=True)