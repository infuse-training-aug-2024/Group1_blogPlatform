import typer
from models import Blog
from post import Post
from typing import Optional
import uuid

app = typer.Typer()

@app.command()
def create(title: str, content: str, author: str, tags: str):
    """
    Creates a new blog post and saves it to the CSV file.
    """
    try:
        tags_list = tags.split(',')
        new_id = uuid.uuid4()
        new_post = Blog(new_id, title, content, author, tags_list)
        Post.create_post(new_post)
        typer.echo("Post created successfully.")
    except Exception as e:
        typer.echo(f"Error creating post: {e}")

@app.command()
def view():
    """
    Views all blog posts from the CSV file.
    """
    try:
        posts = Post.read_posts()
        for post in posts:
            typer.echo(f"ID: {post.id}\nTitle: {post.title}\nContent: {post.content}\nAuthor: {post.author}\nTags: {', '.join(post.tags)}\n")
    except Exception as e:
        typer.echo(f"Error viewing posts: {e}")


@app.command()
def update(post_id: str, title: Optional[str] = None, content: Optional[str] = None,
           author: Optional[str] = None, tags: Optional[str] = None):
    """
    Updates an existing blog post identified by post_id.
    """
    try:
        updated = Post.update_post(post_id, title, content, author, tags)
        if updated:
            typer.echo("Post updated successfully.")
        else:
            typer.echo("Post not found.")
    except Exception as e:
        typer.echo("Error updating posts: {e}")

@app.command()
def delete(post_id: str):
    """
    Deletes a blog post identified by post_id.
    """
    try:
        deleted = Post.delete_post(post_id)
        if deleted:
            typer.echo("Post deleted successfully.")
        else:
            typer.echo("Post not found.")
    except Exception as e:
        typer.echo(f"Error deleting posts: {e}")

@app.command()
def search_by_tag(tag: str):
    """
    Searches for blog posts by a given tag.
    """
    try:
        posts = Post.read_posts()
        matching_posts = [post for post in posts if tag in post.tags]

        if not matching_posts:
            typer.echo(f"No posts found with tag: {tag}")
        else:
            for post in matching_posts:
                typer.echo(f"ID: {post.id}\nTitle: {post.title}\nContent: {post.content}\nAuthor: {post.author}\nTags: {','.join(post.tags)}\n")
    except Exception as e:
        typer.echo(f"Error searching the posts by tag: {e}")

if __name__ == "__main__":
    app()
