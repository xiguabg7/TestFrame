import pytest


@pytest.fixture(autouse="true")
def login():
    print("这是个登陆方法")


def pytest_configure(config):
    mark_list = ["search", "login"]
    for markers in mark_list:
        config.addinivalue_line(
            "markers", markers
        )

# pytest内置函数，重写后，更改方法执行顺序
def pytest_collection_modifyitems(session, config, items):
    for item in items:
        if "add" in item.noeid:
            item.add_marker(pytest.mark.add)
        elif "div" in item.noeid:
            item.add_marker(pytest.mark.div)
    # 倒序执行方法
    # item.reverse()
