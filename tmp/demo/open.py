# while True
#     print("TEST")
#
# Exception
class met:
    pass
with open("/Users/nigo/Documents/TestFrame/test.txt","r+",encoding="utf-8") as f:
    # f.write("789")
    # f.writelines("456")
    # print(f.read())

    # line = f.readline()
    # while line:
    #     # 打印当前指针位置
    #     print("文件指针：",f.tell())
    #     print("行内容：",line)
    #     line = f.readline()
    print("读取多行#####")
    print(f.readlines())