from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    with open("blog_posts.json", "r") as blogs:
        blog_posts = json.loads(blogs.read())
        blog_posts = list(blog_posts)
        return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():


if __name__ == '__main__':
    app.run()


"""This is incase the json file messes up"""
# blog_posts = [{'id': 1, 'author': 'John Doe', 'title': 'First Post', 'content': 'This is my first post.'},
#               {'id': 2, 'author': 'Jane Doe', 'title': 'Second Post',
#                'content': 'This is another post.'}, ]
