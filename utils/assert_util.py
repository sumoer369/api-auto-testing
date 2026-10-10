def assert_status_code(response, expected_code):
    """断言HTTP状态码"""
    assert response.status_code == expected_code, \
        f"状态码断言失败：预期 {expected_code}，实际 {response.status_code}"


def assert_field_value(response, field, expected_value):
    """断言响应体中某个字段的值"""
    actual = response.json().get(field)
    assert actual == expected_value, \
        f"字段 {field} 断言失败：预期 {expected_value}，实际 {actual}"


def assert_field_exists(response, field):
    """断言响应体中存在某个字段"""
    assert field in response.json(), f"响应体中不存在字段 {field}"
