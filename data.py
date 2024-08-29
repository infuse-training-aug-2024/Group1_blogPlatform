import csv
from typing import List, Dict
from models import Blog
from typing import Optional

CSV_FILE_PATH = r'C:\Users\samar\IT\infuse\Group1_blogPlatform\posts.csv'

def _read_csv() -> List[Dict[str, str]]:
    """
    Reads the CSV file and returns a list of dictionaries where each dictionary represents a blog post.
    """
    try:
        with open(CSV_FILE_PATH, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def _write_csv(posts: List[Dict[str, str]]) -> None:
    """
    Writes a list of dictionaries to the CSV file. Each dictionary represents a blog post.
    """
    with open(CSV_FILE_PATH, mode='w', newline='') as file:
        fieldnames = ['id', 'title', 'content', 'author', 'tags']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(posts)

def create_post(blog: Blog) -> None:
    """
    Creates a new blog post and saves it to the CSV file.
    """
    posts = _read_csv()
    posts.append(blog.to_dict())
    _write_csv(posts)

def read_posts() -> List[Blog]:
    """
    Reads all blog posts from the CSV file and returns them as a list of Blog objects.
    """
    posts_dicts = _read_csv()
    return [Blog.from_dict(post_dict) for post_dict in posts_dicts]

def update_post(post_id: str, title: Optional[str] = None, content: Optional[str] = None,
                 author: Optional[str] = None, tags: Optional[str] = None) -> bool:
    """
    Updates an existing blog post identified by post_id.
    """
    tags_list = tags.split(',') if tags else None
    posts = _read_csv()
    updated = False
    for post in posts:
        if post['id'] == post_id:
            if title is not None:
                post['title'] = title
            if content is not None:
                post['content'] = content
            if author is not None:
                post['author'] = author
            if tags_list is not None:
                post['tags'] = ','.join(tags_list)
            updated = True
            break
    if updated:
        _write_csv(posts)
    return updated

# def delete_post(post_id: str) -> bool:
#     """
#     Deletes a blog post identified by post_id.
#     """
#     posts = _read_csv()
#     posts_to_keep = [post for post in posts if post['id'] != post_id]
#     if len(posts_to_keep) < len(posts):
#         _write_csv(posts_to_keep)
#         return True
#     return False
def delete_post(post_id: str) -> bool:
    posts = _read_csv()
    print("Posts before deletion:", posts) 
    posts_to_keep = [post for post in posts if post['id'] != post_id]
    print("Posts after filtering:", posts_to_keep)  
    if len(posts_to_keep) < len(posts):
        _write_csv(posts_to_keep)
        print("Post deleted successfully.") 
        return True
    print("No post found with the given ID.")  
    return False

