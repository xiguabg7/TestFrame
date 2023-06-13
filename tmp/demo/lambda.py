# 重复性代码解决方法
list = [1, -1, 2, -2, 3, -3]


# def print_positive(list):
#     for item in list:
#         if item > 0:
#             print(item)
#
#
# def print_negative(list):
#     for item in list:
#         if item < 0:
#             print(item)

# print_positive(list)
# print_negative(list)

# 抽判断条件
# def positive(x):
#     return x > 0
#
#
# def negative(x):
#     return x < 0


def test(list, fun):
    for item in list:
        if fun(item):
            print(item)


# test(list, positive)
# test(list, negative)
test(list, lambda x: x > 0)
test(list, lambda x: x < 0)

# map中应用lambda表达式
list1 = [1, -1, 2]

list2 = map(lambda x: x + 5, list1)
for item in list2:
    print(item)