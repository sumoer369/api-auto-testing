from utils.request_util import RequestUtil


class PostApi:
    def __init__(self):
        self.req = RequestUtil()

    def get_post(self, post_id):
        """获取指定文章"""
        return self.req.get(f"/posts/{post_id}")

    def get_all_posts(self):
        """获取所有文章"""
        return self.req.get("/posts")

    def create_post(self, data):
        """创建文章"""
        return self.req.post("/posts", json=data)

    def update_post(self, post_id, data):
        """更新文章"""
        return self.req.put(f"/posts/{post_id}", json=data)

    def delete_post(self, post_id):
        """删除文章"""
        return self.req.delete(f"/posts/{post_id}")
