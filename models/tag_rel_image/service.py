# built-in package

# project package
from .tag_rel_image import TagRelImage
from models import session
from utils.tools import create_id


# third package
from flask import g


class TagRelImageModel:

    @classmethod
    def add_tag_rel_image(cls, tag_id, image_id):
        rel_id = create_id()
        tag_rel_image = TagRelImage()
        tag_rel_image.create_user_id = g.user_id
        tag_rel_image.id = rel_id
        tag_rel_image.tag_id = tag_id
        tag_rel_image.image_id = image_id
        session.add(tag_rel_image)
        session.commit()
        return rel_id
