import os
from pathlib import Path

# from time import sleep
#
# path = os.getcwd()
# print(path)
# a = os.path.abspath(path)
#
# os.listdir(path)
# f = os.open(path + "test_os.txt",flags=os.O_CREAT | os.O_RDWR)
# os.write(f, bytes("123",encoding="utf-8"))
# print(os.read(f, 12))
# os.close(f)
# os.rename(path + "test_os.txt",path +"test_os1.txt")
# # sleep(5)
# # os.remove(path + "test_os1.txt")
#
# # for root, dirname, filenames in os.walk(path):
# #     logzeros.debug(root)
# #     logzeros.debug(dirname)
# #     logzeros.debug(filenames)
#
# os.popen("mkfile -n 5k temp.jpg")

print(os.getcwd())
print(Path.cwd())
print(os.path.dirname(os.path.dirname(os.getcwd())))
print(Path.cwd().parent.parent)
print(os.path.join(os.path.dirname(os.getcwd()), "test_basics", "args.py"))
print(Path.cwd().parent.joinpath(*["test_basics", "args.py"]))
# os.makedirs(os.path.join("pro","ject"),exist_ok=True)
os.rename("test.py",os.path.join("pro","test.py"))
Path("pro/ject").mkdir(parents=True,exist_ok=True)
Path("test.py").rename("pro/test.py")
