# 通讯录
persons = []


# 添加联系人
def create_person():
    name = input("输入姓名")
    address = input("输入地址")
    phone = input("输入电话")
    if name and address and phone:
        person = {"name": name,
                  "address": address,
                  "phone": phone}
    persons.append(person)


# 列出联系人
def list_person():
    for person in persons:
        print(person)


# 查出联系人
def query_person():
    name = input("输入姓名")
    for person in persons:
        if name == person["name"]:
            print(person)


# 删除联系人
def delete_person():
    name = input("输入姓名")
    for person in persons:
        if name == person["name"]:
            persons.remove(person)


# 主函数
def main():
    while True:
        input_str = input("1. create person\n"
                          "2. list all persons\n"
                          "3. query person\n"
                          "4. delete person\n"
                          "5. quit\n"
                          "Enter a number(1-5): ")
        if input_str == "1":
            create_person()
        elif input_str == "2":
            list_person()
        elif input_str == "3":
            query_person()
        elif input_str == "4":
            delete_person()
        elif input_str == "5":
            break
        else:
            print("选择无效")


main()