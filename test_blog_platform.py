import pytest
import uuid
from models import Blog
from post import Post
from typer.testing import CliRunner
from app import app

runner = CliRunner()

# Test data
sample_blog = Blog(
    id=uuid.uuid4(),
    title="Sample Title",
    content="Sample Content",
    author="Author Name",
    tags=["test", "blog"]
)

def test_create_blog_post():
    """
    Test creating a blog post.
    """
    result = runner.invoke(app, ['create', 'Sample Title', 'Sample Content', 'Author Name', 'test,blog'])
    assert result.exit_code == 0
    assert "Post created successfully." in result.output

def test_view_blog_posts():
    """
    Test viewing all blog posts.
    """
    result = runner.invoke(app, ['view'])
    assert result.exit_code == 0
    result = runner.invoke(app, ["view"])
    assert result.exit_code == 0
    assert "ID:" in result.output
    assert "Title:" in result.output
    assert "Content:" in result.output
    assert "Author:" in result.output
    assert "Tags:" in result.output

    

def test_update_blog_post():
    """
    Test updating an existing blog post.
    """
    # Creating a post to update
    runner.invoke(app, ['create', 'Title to Update', 'Content to Update', 'Author', 'tag1,tag2'])

    # Fetching the post ID
    posts = Post.read_posts()
    post_id = posts[-1].id

    # Updating the post
    result = runner.invoke(app, ['update', str(post_id), '--title', 'Updated Title'])
    assert result.exit_code == 0
    assert "Post updated successfully." in result.output

    # Verifying the update
    posts = Post.read_posts()
    assert posts[-1].title == "Updated Title"

def test_delete_blog_post():
    """
    Test deleting a blog post.
    """
    # Creating a post to delete
    runner.invoke(app, ['create', 'Title to Delete', 'Content to Delete', 'Author', 'tag1,tag2'])

    # Fetching the post ID
    posts = Post.read_posts()
    post_id = posts[-1].id

    # Deleting the post
    result = runner.invoke(app, ['delete', str(post_id)])
    assert result.exit_code == 0
    assert "Post deleted successfully." in result.output

    # Verifying the deletion
    posts = Post.read_posts()
    assert all(post_id != post.id for post in posts)

def test_search_blog_by_tag():
    """
    Test searching for blog posts by tag.
    """
    # Creating a post to search
    runner.invoke(app, ['create', 'Title to Search', 'Content to Search', 'Author', 'searchtag'])

    result = runner.invoke(app, ['search-by-tag', 'searchtag'])
    assert result.exit_code == 0
    assert "Title to Search" in result.output
    assert "Content to Search" in result.output
    assert "Author" in result.output
    assert "searchtag" in result.output

def test_blog_model_to_dict():
    """
    Test the Blog model's to_dict method.
    """
    blog_dict = sample_blog.to_dict()
    assert blog_dict['title'] == "Sample Title"
    assert blog_dict['author'] == "Author Name"
    assert blog_dict['tags'] == "test,blog"

def test_blog_model_from_dict():
    """
    Test the Blog model's from_dict method.
    """
    blog_dict = sample_blog.to_dict()
    blog_obj = Blog.from_dict(blog_dict)
    assert blog_obj.title == "Sample Title"
    assert blog_obj.author == "Author Name"
    assert blog_obj.tags == ["test", "blog"]
