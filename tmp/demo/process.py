from random import randint
from time import time, sleep
from multiprocessing import Process
from threading import Thread

#
# def download_task(filename):
#     print("start download %s" % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print("%s download sucess,cost %d seconds" % (filename, time_to_download))


# # 单进程
# def main():
#     start = time()
#     download_task("满江红")
#     download_task("流浪地球2")
#     end = time()
#     print("seconds count %.2f" % (end - start))

# # 多进程
# def main():
#     start = time()
#     p1 = Process(target=download_task, args=("满江红",))
#     p1.start()
#     p2 = Process(target=download_task, args=("流浪地球2",))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print("seconds count %.2f" % (end - start))
#
#
# if __name__ == '__main__':
#     main()

class download_task(Thread):
    def __init__(self,filename):
        super().__init__()
        self.filename = filename

    def run(self) -> None:
        print("start download %s" % self.filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print("%s download sucess,cost %d seconds" % (self.filename, time_to_download))

def main1():
    start = time()
    p1 = download_task("满江红")
    p1.start()
    p2 = download_task("流浪地球2")
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print("seconds count %.2f" % (end - start))

if __name__ == "__main__":
    main1()