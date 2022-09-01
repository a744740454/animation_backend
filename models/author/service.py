# built-in package

# project package
from .author import AuthorInfo
from models import session
from utils.tools import create_id

# third package
from flask import g


class AuthorModel:
    @classmethod
    def query_author_by_id(cls, author_id):
        author = session.query(AuthorInfo).filter(
            AuthorInfo.id == author_id
        ).first()
        return author

    @classmethod
    def query_author_by_name(cls, author_name):
        author = session.query(AuthorInfo).filter(
            AuthorInfo.id == author_name
        ).first()
        return author

    @classmethod
    def insert_author(cls, author_name):
        author_id = create_id()
        author = AuthorInfo()
        # author.id = create_id()
        author.author_name = author_name
        author.create_user_id = g.user_id
        session.add(author)
        session.commit()
        return author_id
