from flask import Flask, render_template
import blog_posts

app = Flask(__name__)

@app.route('/')
def index():
    blogs = blog_posts.get_blogs()
    return render_template('index.html', posts=blogs)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)