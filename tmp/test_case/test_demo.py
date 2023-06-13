import pytest


@pytest.fixture()
def login():
    print("login接口")


def test_case1(login):
    print("前置登陆")
    pass


def test_case2():
    print("不用前置")
    pass


class TestDemo():
    def setup(self):
        print("setup")

    ###优先执行###
    def setup_method(self):
        print("method")

    def test_one(self):
        print("#####one#####")
        x = 'this'
        pytest.assume(1 == 2)
        assert 'h' in x

    def test_two(self):
        print("#####two#####")
        x = 'this'
        pytest.assume(2 == 2)
        assert 'h' in x


if __name__ == '__main__':
    pytest.main("-v -x test_demo.py")
    # pytest.main(['-v','-s','test_demo.py'])
