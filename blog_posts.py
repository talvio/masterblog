"""
This module handles blog posts saving them to a json file.
"""
import json

BLOG_FILE = "data/blogs.json"
VALID_REACTIONS = ['like', 'dislike', 'angry', 'yawn', 'shrug', 'brain_explode']


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
    with open(blog_file, 'r', encoding='utf-8') as json_file:
        blogs = json.load(json_file)
    return blogs


def save_blogs(blogs, blog_file=BLOG_FILE):
    """
    Saves blogs to a file
    """
    if blog_file is None:
        blog_file = BLOG_FILE
    with open(blog_file, 'w', encoding='utf-8') as json_file:
        json.dump(blogs, json_file)


def add_blog(title, author, content):
    """
    Add a new blog post
    """
    blogs = get_blogs()
    if len(blogs) == 0:
        new_blog_id = '1'
    else:
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


def update(blog_id, title, author, content, reaction = None):
    """ Update a blog post """
    blogs = get_blogs()
    blog_index = 0
    if len(blogs) == 0:
        return None
    for blog_index, blog in enumerate(blogs):
        if int(blog.get('id')) == int(blog_id):
            break
    if int(blogs[blog_index].get('id')) == int(blog_id):
        blogs[blog_index]['title'] = title \
            if title is not None else blogs[blog_index]['title']
        blogs[blog_index]['author'] = author \
            if author is not None else blogs[blog_index]['author']
        blogs[blog_index]['content'] = content \
            if content is not None else blogs[blog_index]['content']
        if reaction in VALID_REACTIONS:
            blogs[blog_index][reaction] = int(blogs[blog_index].get(reaction,0)) + 1
    save_blogs(blogs)
    return blogs[blog_index].get('id')


def react(blog_id, reaction_type):
    """ Add a new reaction to a blog post """
    return update(blog_id, None, None, None, reaction_type)


def delete(blog_id):
    """ Remove a blog post """
    blogs = get_blogs()
    for blog in blogs:
        if str(blog.get('id')) == str(blog_id):
            print(blogs)
            blogs.remove(blog)
            print(blogs)
            break
    save_blogs(blogs)


def get_post(blog_id):
    """
    Get a blog post with id
    :param post_id: ID of the post
    :return: The specific blog post or None if no ID matches.
    """
    blogs = get_blogs()
    for blog in blogs:
        if int(blog.get('id')) == int(blog_id):
            return blog
    return None
