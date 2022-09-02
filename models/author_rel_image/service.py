# built-in package

# project package
from .author_rel_image import AuthorRelImage
from models import session
from utils.tools import create_id


# third package
from flask import g

class AuthorRelImageModel:

    @classmethod
    def add_author_rel_image(cls, author_id, image_id):
        author_rel_id = create_id()
        author_rel_image = AuthorRelImage()
        author_rel_image.id = author_rel_id
        author_rel_image.author_id = author_id
        author_rel_image.image_id = image_id
        author_rel_image.create_user_id = g.user_id
        session.add(author_rel_image)
        session.commit()
        return author_rel_id
