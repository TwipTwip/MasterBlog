from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    with open("blog_posts.json", "r") as blogs:
        blog_posts = json.load(blogs)
        blog_posts = list(blog_posts)
        return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        counter = 0
        with open("blog_posts.json", "r") as new_num:
            numbers = json.load(new_num)
            numbers = list(numbers)
        for number in numbers:
            counter += 1
            number["id"] = counter
        with open("blog_posts.json", "w") as unique:
            json.dump(numbers, unique)
        id = counter + 1
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")
        blog = {"id": id, "title": title, "author": author, "content": content}
        with open("blog_posts.json", "r") as info:
            blogs = json.load(info)
            blogs = list(blogs)
            blogs.append(blog)
        with open("blog_posts.json", "w") as upt_blog:
            json.dump(blogs, upt_blog)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=["POST"])
def delete(post_id):
    with open("blog_posts.json", "r") as del_read:
        blogs = json.load(del_read)
        blogs = list(blogs)
    kept_blogs = []
    for blog in blogs:
        if blog['id'] == post_id:
            continue
        else:
            kept_blogs.append(blog)
    with open("blog_posts.json", "w") as rewrite:
        json.dump(kept_blogs, rewrite)
    return redirect((url_for('index')))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    with open("blog_posts.json", "r") as info:
        blogs = json.load(info)
        blogs = list(blogs)
    post = {}
    for blog in blogs:
        if blog['id'] == post_id:
            post = {"id": blog['id'],
                    "title": blog['title'],
                    "author": blog['author'],
                    "content": blog['content']}
    info.close()
    if post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
        # Update the post in the JSON file
        # Redirect back to index
        post['content'] = request.form.get("content")
        post['author'] = request.form.get("author")
        post['title'] = request.form.get("title")
        with open("blog_posts.json", "r") as update_content:
            blog_info = json.load(update_content)
            blog_info = list(blog_info)
            for blog in blog_info:
                if blog['id'] == post['id']:
                    blog['id'] = post['id']
                    blog['title'] = post['title']
                    blog['author'] = post['author']
                    blog['content'] = post['content']
        with open("blog_posts.json", "w") as new_content:
            json.dump(blog_info, new_content)
        return redirect((url_for("index")))

    # Else, it's a GET request
    # So display the update.html page
    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run()

# """This is incase the json file messes up"""
# blog_posts = [{'id': 1, 'author': 'John Doe', 'title': 'First Post', 'content': 'This is my first post.'},
#               {'id': 2, 'author': 'Jane Doe', 'title': 'Second Post', 'content': 'This is another post.'}]
# with open("blog_posts.json", "w") as write:
#     json.dump(blog_posts, write)
