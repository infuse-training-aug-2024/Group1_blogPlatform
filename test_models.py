import unittest
import uuid
from models import Blog

class TestBlog(unittest.TestCase):

    def test_blog_creation(self):
        blog_id = uuid.uuid4()
        blog = Blog(id=blog_id, title="Test Title", content="Test Content", author="Test Author", tags=["test", "blog"])
        
        self.assertEqual(blog.id, blog_id)
        self.assertEqual(blog.title, "Test Title")
        self.assertEqual(blog.content, "Test Content")
        self.assertEqual(blog.author, "Test Author")
        self.assertEqual(blog.tags, ["test", "blog"])

    def test_blog_to_dict(self):
        blog_id = uuid.uuid4()
        blog = Blog(id=blog_id, title="Test Title", content="Test Content", author="Test Author", tags=["test", "blog"])
        blog_dict = blog.to_dict()
        
        self.assertEqual(blog_dict['id'], str(blog_id))
        self.assertEqual(blog_dict['title'], "Test Title")
        self.assertEqual(blog_dict['content'], "Test Content")
        self.assertEqual(blog_dict['author'], "Test Author")
        self.assertEqual(blog_dict['tags'], "test,blog")

    def test_blog_from_dict(self):
        blog_dict = {
            'id': str(uuid.uuid4()),
            'title': "Test Title",
            'content': "Test Content",
            'author': "Test Author",
            'tags': "test,blog"
        }
        blog = Blog.from_dict(blog_dict)
        
        self.assertEqual(str(blog.id), blog_dict['id'])
        self.assertEqual(blog.title, blog_dict['title'])
        self.assertEqual(blog.content, blog_dict['content'])
        self.assertEqual(blog.author, blog_dict['author'])
        self.assertEqual(blog.tags, blog_dict['tags'].split(','))

if __name__ == '__main__':
    unittest.main()
