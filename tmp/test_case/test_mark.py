import pytest
import sys


# @pytest.mark.parametrize("test_input, expected", [("1+2", 3), ("1+3", 4)])
# def test_eval(test_input, expected):
#     # eval 将字符串str当成有效表达式来求值，并返回结果
#     assert eval(test_input) == expected
#
#
# # 参数组合
# @pytest.mark.parametrize("x", [1, 2, 3])
# @pytest.mark.parametrize("y", [1, 2, 3])
# def test_too(x, y):
#     print(f"x:{x},y:{y}")


test_user_data = ["ton", "jenny"]


@pytest.fixture(scope="module")
def login_u(request):
    user = request.param
    print(f"\n准备登陆，登陆用户{user}")
    return user


@pytest.mark.skipif(sys.platform == "darwin", reason="不执行")
# @pytest.mark.skip("暂不执行")
# @pytest.mark.xfail("有遗留问题，暂抛出 xpass ")
@pytest.mark.parametrize("login_u", test_user_data, indirect=True)
def test_login(login_u):
    a = login_u
    print(f"login user {a}")
    assert a != ""


if __name__ == "__main__":
    pytest.main()
