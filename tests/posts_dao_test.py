import pytest
from app.post_dao import PostsDAO


class TestPostDAO:

    @pytest.fixture
    def posts_dao(self):
        return PostsDAO("data/posts.json")

    @pytest.fixture
    def keys_excepted(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    # Получение всех постов
    def test_get_posts_all_check_type(self, posts_dao):
        posts = posts_dao.get_posts_all()
        assert type(posts) == list, "Список постов должен быть списком"
        assert type(posts[0]) == dict, "Каждый пост должен быть словарем"

    def test_get_posts_all_has_keys(self, posts_dao, keys_excepted):
        posts = posts_dao.get_posts_all()
        first_post = posts[0]
        first_post_keys = set(first_post.keys())
        assert first_post_keys == keys_excepted, "Полученные ключи неверны"

    # Получение одного поста
    def test_get_one_check_type(self, posts_dao):
        posts = posts_dao.get_post_by_pk(1)
        assert type(posts) == dict, "Пост должен быть словарем"

    def test_get_one_has_keys(self, posts_dao, keys_excepted):
        post = posts_dao.get_post_by_pk(1)
        post_keys = set(post.keys())
        assert post_keys == keys_excepted, "Полученные ключи неверны"

    parameters_get_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]

    @pytest.mark.parametrize("post_pk", parameters_get_by_pk)
    def test_get_one_check_type_has_correct_pk(self, posts_dao, post_pk):
        post = posts_dao.get_post_by_pk(post_pk)
        assert post["pk"] == post_pk, "Номер полученного поста не соответствует запрашиваемому номеру"

    # Получение по пользователю
    parameters_by_user = [
        ("leo", [1, 5]),
        ("johnny", [2, 6]),
        ("hank", [3, 7]),
        ("larry", [4, 8])
    ]

    @pytest.mark.parametrize("user_name, correct_pks", parameters_by_user)
    def test_get_posts_by_user(self, posts_dao, user_name, correct_pks):
        posts = posts_dao.get_posts_by_user(user_name)
        pks = []
        for post in posts:
            pks.append(post["pk"])
        assert pks == correct_pks, f"Неверный список постов пользователя {user_name}"

    # Поиск постов
    parameters_search = [
        ("тарелка", [1]),
        ("вышел", [2]),
        ("елки", [3]),
        ("проснулся", [4]),
        ("пурр", [5]),
        ("лампочка", [6]),
        ("закат", [7]),
        ("острова", [8])
    ]

    @pytest.mark.parametrize("query, correct_pks", parameters_search)
    def test_search_for_post(self, posts_dao, query, correct_pks):
        posts = posts_dao.search_for_posts(query)
        pks = []
        for post in posts:
            pks.append(post["pk"])
        assert pks == correct_pks, f"Неверный поиск по запросу {query}"


