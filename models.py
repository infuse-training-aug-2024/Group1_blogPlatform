import uuid
from typing import List

class Blog:
    def __init__(self, title: str, content: str, author: str, tags: List[str]) -> None:
        """
        Initializes a new blog post with the provided attributes.
        
        :param title: The title of the blog post.
        :param content: The content of the blog post.
        :param author: The author of the blog post.
        :param tags: A list of tags associated with the blog post.
        """
        self.id: uuid.UUID = uuid.uuid4()  
        self.title: str = title            
        self.content: str = content       
        self.author: str = author         
        self.tags: List[str] = tags        
