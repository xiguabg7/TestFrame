def str_to_int(string):
    """
    字符串转整数
    :param string: 字符串 str unicode
    :return: 整数 int
    """
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers_str = map(str, numbers)
    if not isinstance(string, (str, unicode)):
        # raise  Exception(u"请输入字符串")
        return u"请输入字符串"
    if string.startswith("-"):
        status = -1
        string = string[1:]
    elif string.startswith("+"):
        status = 1
        string = string[1:]
    else:
        status = 1
    for i in string:
        if i not in numbers_str:
            # raise Exception(u"请输入正确的整数")
            return (u"请输入正确的整数")
    result = 0
    length = len(string)
    if not length:
        # raise Exception(u"请输入有效数字")
        return "请输入有效数字"
    for i, value in enumerate(string):
        result += numbers[numbers_str.index(value)] * 10 ** (length - i - 1)
    return result * status


if __name__ == "__main__":
    print
    str_to_int("1234")
    print
    str_to_int("01234")
    print
    str_to_int("#!@#1234")
    print
    str_to_int("asd")
    print
    str_to_int("-1234")
    print
    str_to_int("+1234")
    print
    str_to_int(u"+1234")
    print
    str_to_int(u"+")
    print
    str_to_int(u"-0")
    print
    str_to_int("1234.1234")
    print
    str_to_int(1234)
    print
    str_to_int(1234.1234)
    print
    str_to_int("9" * 10086)
