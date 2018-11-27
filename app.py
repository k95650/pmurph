from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Kyle VanZandt',
        'title': 'Blog Post 1',
        'content': 'This is made using python so suck only reworte the whole website 4 times so far',
        'date_posted': '11/26/2018', 
    },
    {
        'author': 'Kyle VanZandt',
        'title': 'Blog Post 2',
        'content': 'Testing',
        'date_posted': '11/27/2018', 
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/videos')
def videos():
    return render_template('videos.html')

if __name__ == '__main__':
    app.run(debug=True)