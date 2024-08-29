import uuid
from typing import List

class Blog:
    def __init__(self, id: uuid.UUID, title: str, content: str, author: str, tags: List[str]) -> None:
        """
        Initializes a new blog post with the provided attributes.
        """
        self.id: uuid.UUID = id  
        self.title: str = title
        self.content: str = content
        self.author: str = author
        self.tags: List[str] = tags

    @classmethod
    def from_dict(cls, data: dict) -> 'Blog':
        """
        Creates a Blog object from a dictionary.
        """
        return cls(
            id=uuid.UUID(data['id']),  
            title=data['title'],
            content=data['content'],
            author=data['author'],
            tags=data['tags'].split(', ')  
        )

    def to_dict(self) -> dict:
        """
        Converts the Blog object into a dictionary.
        """
        return {
            'id': str(self.id),  
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'tags': ', '.join(self.tags)  
        }
