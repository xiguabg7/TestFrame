from typing import Tuple, List, Dict, Set, Union, TypeVar, Any


# a: Tuple[int, ...] = (1, 3)


# 返回一个 Tuple 类型的数据，第一个元素是 List，第二个元素是 Tuple，第三个元素是 Dict，第四个元素可以是字符串或布尔
def add(a: int, string: str, f: float, b: bool or str) -> Tuple[List, Tuple, Dict, bool or str]:
    list1 = list(range(a))
    tup = (string, string, string)
    d = {"a": f}
    b = b
    return list1, tup, d, b


print(add(1, "2", 123, True))
# 自定义别名
vector_list_es = List[float]
vector_dict = Dict[str, List[float]]
vector_list = List[vector_dict]


def scale(scalar: float, vector: vector_list) -> vector_list:
    for item in vector:
        for key, value in item.items():
            item[key] = [scalar * num for num in value]
    print(vector)
    return vector


scale(2.2, [{"a": [1, 2, 3]}, {"b": [4, 5, 6]}])

# NewType
from typing import NewType

UserId = NewType('UserId', int)


def name_by_id(user_id: UserId) -> str:
    print(user_id)


UserId('user')  # Fails type check
num = UserId(5)  # type: int

name_by_id("23")  # Fails type check
name_by_id(UserId(42))  # OK

print(type(UserId("5")))

a: Union[int, str]
a = 1
a = []
aa = TypeVar('aa', int, str)
b: aa = []
b: aa = 123

def off(a: Any) -> int:
    print(a)
off(123)