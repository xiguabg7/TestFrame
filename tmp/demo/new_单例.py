class Polo:
    instance = None
    init_flag = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            print("开始分配内存空间")
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if Polo.init_flag:
            return
        Polo.init_flag = True
        print("开始初始化")


polo = Polo()
polo1 = Polo()
print(id(polo), id(polo1))
