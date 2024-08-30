import csv
import typer
from typing import List, Dict, Optional
from models import Blog
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(current_dir, 'posts.csv')

class Post:

    @staticmethod
    def _read_csv() -> List[Dict[str, str]]:
        """
        Reads the CSV file and returns a list of dictionaries where each dictionary represents a blog post.
        """
        try:
            with open(CSV_FILE_PATH, mode='r') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            typer.echo("Error: csv file not found")
            return []
        except Exception as e:
            typer.echo("Error while opening the file: {e}")

    @staticmethod
    def _write_csv(posts: List[Dict[str, str]]) -> None:
        """
        Writes a list of dictionaries to the CSV file. Each dictionary represents a blog post.
        """
        try:
            with open(CSV_FILE_PATH, mode='w', newline='') as file:
                fieldnames = ['id', 'title', 'content', 'author', 'tags']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(posts)
        except Exception as e:
            typer.echo(f"Error writing to csv file: {e}")

    @staticmethod
    def create_post(blog: Blog) -> None:
        """
        Creates a new blog post and saves it to the CSV file.
        """
        try:
            posts = Post._read_csv()
            posts.append(blog.to_dict())
            Post._write_csv(posts)
        except Exception as e:
            typer.echo("Error creating a post: {e}")

    @staticmethod
    def read_posts() -> List[Blog]:
        """
        Reads all blog posts from the CSV file and returns them as a list of Blog objects.
        """
        try:
            posts_dicts = Post._read_csv()
            return [Blog.from_dict(post_dict) for post_dict in posts_dicts]
        except Exception as e:
            typer.echo(f"Error reading a post: {e}")

    @staticmethod
    def update_post(post_id: str, title: Optional[str] = None, content: Optional[str] = None,
                    author: Optional[str] = None, tags: Optional[str] = None) -> bool:
        """
        Updates an existing blog post identified by post_id.
        """
        try:
            tags_list = tags.split(',') if tags else None
            posts = Post._read_csv()
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
                Post._write_csv(posts)
            return updated
        except Exception as e:
            typer.echo(f"Error occured while updating post: {e}")


    def delete_post(post_id: str) -> bool:
        try:
            posts = Post._read_csv()
            # print("Posts before deletion:", posts) 
            posts_to_keep = [post for post in posts if post['id'] != post_id]
            # print("Posts after filtering:", posts_to_keep)  
            if len(posts_to_keep) < len(posts):
                Post._write_csv(posts_to_keep)
                # print("Post deleted successfully.") 
                return True
            print("No post found with the given ID.")  
            return False
        except Exception as e:
            typer.echo("Error while deleting post: {e}")

