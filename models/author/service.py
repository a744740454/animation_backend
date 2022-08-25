from .author import AuthorInfo
from models import session


class AuthorModel:
    @classmethod
    def query_author_by_id(cls, author_id):
        author = session.query(AuthorInfo).filter(
            AuthorInfo.id == author_id
        ).first()
        return author
