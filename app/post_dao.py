import json


class PostsDAO:
    """Класс ответственный за работу с постами"""

    def __init__(self, path):
        self.path = path

    def _load(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_posts_all(self):
        """Возвращает посты"""
        return self._load()

    def get_posts_by_user(self, user_name):
        """Возвращает посты определенного пользователя"""
        posts = self.get_posts_all()
        posts_by_user = []
        for post in posts:
            if post["poster_name"] == user_name:
                posts_by_user.append(post)
        return posts_by_user

    def search_for_posts(self, query):
        """Возвращает список постов по ключевому слову"""
        posts = self.get_posts_all()
        matching_posts = []
        query_lower = query.lower()
        for post in posts:
            if query_lower in post['content'].lower():
                matching_posts.append(post)
        return matching_posts

    def get_post_by_pk(self, pk):
        """Возвращает пост по его идентификатору"""
        posts = self.get_posts_all()
        for post in posts:
            if post['pk'] == pk:
                return post
