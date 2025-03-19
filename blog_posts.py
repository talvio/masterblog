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
        blog_file = self.blog_file
    with open(blog_file, 'r') as json_file:
        blogs = json.load(json_file)
    return blogs