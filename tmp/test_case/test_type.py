def create_full_name(**kwargs):
    # 打印就是一个字典
    print(kwargs)

    name = kwargs.get("name")
    password = kwargs.get("password")

    if name and password:
        print("name is :", name, " and password is :", password)

    if name and not password:
        print("only name is:", name)


# 方式一：通过 key=value 的方式传参
create_full_name(name="小菠萝", password="123456")

dict_ = {"name": "yy"}
# 方式二：传字典，然后加 ** 进行解包
create_full_name(**dict_)