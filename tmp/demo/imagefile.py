import os
import platform
import subprocess
import time

from PIL import Image


def resize_picture_filesize(imagefile, targetfile, targetsize, platfrom=None):
    """调整图片文件大小
    :param imagefile: 原图路径
    :param targetfile: 保存图片路径
    :param targetsize: 目标文件大小，单位byte
    :return:
    """
    currentsize = os.path.getsize(imagefile)  # 原图大小
    if currentsize > targetsize:  # 需要缩小
        for quality in range(99, 0, -1):  # 压缩质量递减
            image = Image.open(imagefile)
            image.save(targetfile, optimize=True, quality=quality)
            currentsize = os.path.getsize(targetfile)

    else:  # 需要放大
        system = platform.system()
        tempfile = str(int(time.time()))  # 临时文件路径
        tempsize = str(targetsize - os.path.getsize(imagefile))  # 临时文件大小

        if system == 'Windows':
            subprocess.run(['fsutil', 'file', 'createnew', tempfile, tempsize])  # 创建临时文件
            subprocess.run(['copy/b', '{}/b+{}/b'.format(imagefile, tempfile), targetfile], shell=True)  # 合并生成新图片
        elif system == 'Darwin':
            subprocess.run(['mkfile', '-n', tempsize, tempfile])  # 创建临时文件
            subprocess.run('cat {} {} > {}'.format(imagefile, tempfile, targetfile), shell=True)  # 合并生成新图片
        elif system == 'Linux':
            subprocess.run(['fallocate', '-l', tempsize, tempfile])  # 创建临时文件
            subprocess.run('cat {} {} > {}'.format(imagefile, tempfile, targetfile), shell=True)  # 合并生成新图片
        os.remove(tempfile)


if __name__ == '__main__':
    imagefile = 'imagesource1.jpg'  # 4kb图片
    resize_picture_filesize(imagefile, 'reduce.jpg', 4 * 1024)  # 缩小到2kb
    # resize_picture_filesize(imagefile, 'reduce2.jpg', 80 * 1024 * 1024)  # 放大到80M
