import pytest


@pytest.fixture(scope="module", autouse="true")
def open():
    print("open bro")
    yield
    print("down")




def test_one():
    print("one")


def test_two():
    print("two")


def test_three():
    print("three")


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_fixture.py"])

# @pytest.mark.parametrize(indirect="true")
