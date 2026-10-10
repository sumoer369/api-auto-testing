import pytest
import yaml
import allure
from api.post_api import PostApi
from utils.assert_util import assert_status_code, assert_field_value


def load_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


GET_CASES = load_yaml("data/posts_data.yaml")["get_cases"]
CREATE_CASES = load_yaml("data/posts_data.yaml")["create_cases"]


@allure.feature("文章接口测试")
class TestPosts:

    @allure.story("GET 获取文章")
    @pytest.mark.parametrize("case", GET_CASES)
    def test_get_post(self, case):
        """测试 GET 请求：获取指定文章详情，断言状态码和 userId 字段"""
        api = PostApi()
        response = api.get_post(case["post_id"])
        assert_status_code(response, case["expected_status"])

        if "expected_user_id" in case:
            assert_field_value(response, "userId", case["expected_user_id"])

    @allure.story("POST 创建文章")
    @pytest.mark.parametrize("case", CREATE_CASES)
    def test_create_post(self, case):
        """测试 POST 请求：创建文章，断言状态码和返回的标题"""
        api = PostApi()
        response = api.create_post(case["payload"])
        assert_status_code(response, case["expected_status"])

        if "expected_title" in case:
            assert_field_value(response, "title", case["expected_title"])

    @allure.story("PUT 更新文章")
    def test_update_post(self):
        """测试 PUT 请求：更新文章，断言状态码和更新后的标题"""
        api = PostApi()
        response = api.update_post(1, {"title": "更新后的标题", "userId": 1})
        assert_status_code(response, 200)
        assert_field_value(response, "title", "更新后的标题")

    @allure.story("DELETE 删除文章")
    def test_delete_post(self):
        """测试 DELETE 请求：删除文章，断言状态码为 200"""
        api = PostApi()
        response = api.delete_post(1)
        assert_status_code(response, 200)