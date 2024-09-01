import unittest
from typer.testing import CliRunner
from unittest.mock import patch
import uuid
from app import app
from models import Blog

runner = CliRunner()

class TestApp(unittest.TestCase):

    @patch('app.Post.create_post')
    def test_create_command(self, mock_create_post):
        result = runner.invoke(app, ['create', 'Test Title', 'Test Content', 'Test Author', 'test,blog'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Post created successfully.", result.output)

    @patch('app.Post.read_posts')
    def test_view_command(self, mock_read_posts):
        blog_id = uuid.uuid4()
        mock_read_posts.return_value = [
            Blog(str(blog_id), 'Test Title', 'Test Content', 'Test Author', ['test', 'blog'])
        ]
        result = runner.invoke(app, ['view'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Test Title', result.output)
        self.assertIn('Test Content', result.output)
        self.assertIn('Test Author', result.output)

    @patch('app.Post.update_post', return_value=True)
    def test_update_command(self, mock_update_post):
        blog_id = uuid.uuid4()
        result = runner.invoke(app, ['update', str(blog_id), '--title', 'Updated Title'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Post updated successfully.", result.output)

    @patch('app.Post.delete_post', return_value=True)
    def test_delete_command(self, mock_delete_post):
        blog_id = uuid.uuid4()
        result = runner.invoke(app, ['delete', str(blog_id)])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Post deleted successfully.", result.output)

if __name__ == '__main__':
    unittest.main()
