from .tag import Tag
from models import session
from utils.tools import create_id


class TagModel:
    @classmethod
    def query_tag_by_id(cls, tag_id):
        tag = session.query(Tag).filter(
            Tag.id == tag_id
        ).first()
        return tag

    @classmethod
    def query_tag_by_name(cls, tag_name):
        tag = session.query(Tag).filter(
            Tag.name == tag_name
        ).first()
        return tag

    @classmethod
    def insert_tag(cls, tag_name):
        """
        创建标签
        """
        tag = Tag()
        tag_id = create_id()
        tag.id = tag_id
        tag.name = tag_name
        session.add(tag)

        session.commit()
        return tag_id

    @classmethod
    def query_tags_by_names(cls, tag_name):
        tags = session.query(Tag).filter(
            Tag.name.in_(tag_name)
        ).all()
        return tags
