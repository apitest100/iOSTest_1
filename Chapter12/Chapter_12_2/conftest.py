import pytest


@pytest.fixture(scope="function")
def sutd():
    print("在开始执行setup")
    yield
    print("在结束执行teardown")
