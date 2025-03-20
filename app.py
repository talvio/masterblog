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
        title = request.form.get('title', "")
        author = request.form.get('author',"")
        content = request.form.get('content', "")
        blog_posts.add_blog(title, author, content)
        return redirect(url_for('index'))

    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)