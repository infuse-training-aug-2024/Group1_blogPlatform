import typer
from models import Blog
from data import create_post, read_posts, update_post, delete_post
from typing import Optional
import uuid

app = typer.Typer()

@app.command()
def create(title: str, content: str, author: str, tags: str):
    """
    Creates a new blog post and saves it to the CSV file.
    """
    tags_list = tags.split(',')
    new_id = uuid.uuid4()
    new_post = Blog(new_id, title, content, author, tags_list)
    create_post(new_post)
    typer.echo("Post created successfully.")

@app.command()
def view():
    """
    Views all blog posts from the CSV file.
    """
    posts = read_posts()
    for post in posts:
        typer.echo(f"ID: {post.id}\nTitle: {post.title}\nContent: {post.content}\nAuthor: {post.author}\nTags: {', '.join(post.tags)}\n")

@app.command()
def update(post_id: str, title: Optional[str] = None, content: Optional[str] = None,
           author: Optional[str] = None, tags: Optional[str] = None):
    """
    Updates an existing blog post identified by post_id.
    """
    updated = update_post(post_id, title, content, author, tags)
    if updated:
        typer.echo("Post updated successfully.")
    else:
        typer.echo("Post not found.")

@app.command()
def delete(post_id: str):
    """
    Deletes a blog post identified by post_id.
    """
    deleted = delete_post(post_id)
    if deleted:
        typer.echo("Post deleted successfully.")
    else:
        typer.echo("Post not found.")

if __name__ == "__main__":
    app()
