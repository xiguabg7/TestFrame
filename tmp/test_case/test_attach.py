import allure
from tmp import *




# attach 附加方法
def test_attach_text():
    allure.attach("文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是个html</body>", attachment_type=allure.attachment_type.HTML)


def test_attach_png():
    allure.attach.file("/Users/Administrator/Documents/87181da0391b3beb0248e4d7d9860e53.jpg",
                       attachment_type=allure.attachment_type.JPG)


