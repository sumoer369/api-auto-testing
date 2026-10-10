import pytest
from utils.request_util import RequestUtil


@pytest.fixture(scope="session")
def req():
    return RequestUtil()
