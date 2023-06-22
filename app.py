from flask import Flask, render_template, request, redirect, url_for
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
    if request.method == 'POST':
        counter = 0
        with open("blog_posts.json", "r") as new_num:
            numbers = json.loads(new_num.read())
            numbers = list(numbers)
        for number in numbers:
            counter += 1
            number["id"] = counter
        with open("blog_posts.json", "w") as unique:
            unique.write(json.dumps(numbers))
        id = counter + 1
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")
        blog = {"id": id, "title": title, "author": author, "content": content}
        with open("blog_posts.json", "r") as info:
            blogs = json.loads(info.read())
            blogs = list(blogs)
            blogs.append(blog)
        with open("blog_posts.json", "w") as add:
            add.write(json.dumps(blogs))
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run()

# """This is incase the json file messes up"""
# blog_posts = [{'id': 1, 'author': 'John Doe', 'title': 'First Post', 'content': 'This is my first post.'},
#               {'id': 2, 'author': 'Jane Doe', 'title': 'Second Post', 'content': 'This is another post.'}]
# with open("blog_posts.json", "w") as write:
#     write.write(json.dumps(blog_posts))
