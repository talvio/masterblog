from flask import Flask, render_template, request, redirect, url_for
import blog_posts

app = Flask(__name__)

@app.route('/')
def index():
    blogs = blog_posts.get_blogs()
    return render_template('index.html', posts=blogs)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        post_id = request.form.get('id', "")
        title = request.form.get('title', "")
        author = request.form.get('author',"")
        content = request.form.get('content', "")
        if post_id == 'new':
            blog_posts.add_blog(title, author, content)
        elif post_id.isdigit():
            blog_posts.update(post_id, title, author, content)

        return redirect(url_for('index'))

    return render_template('add.html',
                           h1_title="Something new to shout at the world!",
                           id="new",
                           title="",
                           author="",
                           content="")

@app.route('/delete/<int:post_id>')
def delete(post_id):
    blog_posts.delete(post_id)
    return redirect(url_for('index'))

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    blog = blog_posts.get_post(post_id)
    if blog is None:
        # Post not found
        return 'Post not found. <a href="/">Click here to go to blog posts.</a>', 404
    if request.method == 'POST':
        add()

    return render_template('add.html',
                            h1_title = "Updating an old yell at the world!",
                            id=post_id,
                            title=blog.get('title', ''),
                            author=blog.get('author', ''),
                            content=blog.get('content', '')
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)