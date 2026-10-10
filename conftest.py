import sys
import os
import pytest
from utils.request_util import RequestUtil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(scope="session")
def req():
    return RequestUtil()


def pytest_html_report_title(report):
    report.title = "JSONPlaceholder 接口自动化测试报告"