""" Flask based blog site exercise """
from flask import Flask, render_template, request, redirect, url_for
import blog_posts

app = Flask(__name__)

@app.route('/')
def index():
    """ Home page showing all the blog posts"""
    blogs = blog_posts.get_blogs()
    return render_template('index.html', posts=blogs)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """ Add a new blog post """
    if request.method == 'POST':
        title = request.form.get('title', "")
        author = request.form.get('author',"")
        content = request.form.get('content', "")
        blog_posts.add_blog(title, author, content)
        return redirect(url_for('index'))

    return render_template('add.html',
                           h1_title="Something new to shout at the world!",
                           id="new",
                           title="",
                           author="",
                           content="")


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """ Delete a blog post """
    blog_posts.delete(post_id)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """ Update a blog post"""
    blog = blog_posts.get_post(post_id)
    if blog is None:
        return 'Post not found. <a href="/">Click here to go to blog posts.</a>', 404
    if request.method == 'POST':
        title = request.form.get('title', "")
        author = request.form.get('author',"")
        content = request.form.get('content', "")
        blog_posts.update(post_id, title, author, content)
        return redirect(url_for('index'))

    return render_template('update.html',
                            h1_title = "Updating an old yell at the world!",
                            post=blog
                           )


@app.route('/react/<reaction_type>/<int:post_id>')
def react(reaction_type, post_id):
    """ React to a blog post with like, dislike, etc """
    if blog_posts.react(post_id, reaction_type) is None:
        return ('Quit playing around with my URLs. '
                '<a href="/">Click here to go to blog posts.</a>', 404)
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(_):
    """ Page not found error"""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
