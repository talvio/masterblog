import json

BLOG_FILE = "data/blogs.json"

def get_blogs(blog_file=BLOG_FILE):
    """
    Returns the saved blogs from a file
    :param blogs_file: The file where blogs are saved
    :return: Nested data structure as it is stored in json file. In this case like this:
    [
        {'id': 1, 'author': 'John Doe', 'title': 'First Post', 'content': 'This is my first post.'},
        {'id': 2, 'author': 'Jane Doe', 'title': 'Second Post', 'content': 'This is another post.'},
    ]
    """
    if blog_file is None:
        blog_file = BLOG_FILE
    with open(blog_file, 'r') as json_file:
        blogs = json.load(json_file)
    return blogs

def save_blogs(blogs, blog_file=BLOG_FILE):
    """
    Saves blogs to a file
    """
    if blog_file is None:
        blog_file = BLOG_FILE
    with open(blog_file, 'w') as json_file:
        json.dump(blogs, json_file)

def add_blog(title, author, content):
    """
    Add a new blog post
    """
    blogs = get_blogs()
    new_blog_id = str(max(int(blog.get('id', 0)) + 1 for blog in blogs ))
    blogs.append(
        {
            'id': new_blog_id,
            'title': title,
            'author': author,
            'content': content,
        }
    )
    save_blogs(blogs)
    return new_blog_id

