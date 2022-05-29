import pytest

from app.comments_dao import CommentsDAO


class TestCommentsDAO:

    @pytest.fixture
    def comments_dao(self):
        return CommentsDAO("data/comments.json")

    @pytest.fixture
    def keys_excepted(self):
        return {"post_pk", "commenter_name", "comment", "pk"}

    # Получение комментариев к посту
    def test_get_comments_by_post_pk_check_type(self, comments_dao):
        comments = comments_dao.get_comments_by_post_pk(1)
        assert type(comments) == list, "Результат должен быть списком"
        assert type(comments[0]) == dict, "Результат должен быть словарем"

    def test_get_comments_by_post_pk_keys_excepted(self, comments_dao, keys_excepted):
        comment = comments_dao.get_comments_by_post_pk(1)[0]
        comment_keys = set(comment.keys())
        assert comment_keys == keys_excepted, "Список ключей не соответствует"

    parameters_for_posts_and_comments = [
        (1, {1, 2, 3, 4}),
        (2, {5, 6, 7, 8}),
        (3, {9, 10, 11, 12}),
        (4, {13, 14, 15, 16}),
        (5, {17, 18}),
        (6, {19}),
        (7, {20}),
        (0, set())
    ]

    @pytest.mark.parametrize("post_pk, correct_comments_pk", parameters_for_posts_and_comments)
    def test_get_comments_by_post_pk_check_match(self, comments_dao, post_pk, correct_comments_pk):
        comments = comments_dao.get_comments_by_post_pk(post_pk)
        comment_pks = set([comment["pk"] for comment in comments])
        assert comment_pks == correct_comments_pk, f"Не совпадает количество комментов для поста {post_pk}"