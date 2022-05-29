import logging

from flask import Blueprint, request, jsonify
from app.post_dao import PostsDAO
from app.comments_dao import CommentsDAO

api_blueprint = Blueprint('api_blueprint', __name__)

post_dao = PostsDAO("data/posts.json")
comments_dao = CommentsDAO("data/comments.json")

logger = logging.getLogger("basic")


@api_blueprint.route('/api/posts/')
def post_all():
    logger.debug("Запрошены все посты через API")
    posts = post_dao.get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_pk>/')
def posts_one(post_pk):
    logger.debug(f"Запрошен пост с pk {post_pk} через API")
    post = post_dao.get_post_by_pk(post_pk)
    return jsonify(post)

