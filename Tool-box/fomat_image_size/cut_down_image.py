"""
author: stitch_xi
date： 2021-07-05
readme: 这是一个基于python的图形化目录压缩工具，可以压缩指定目录下的所有图片，目前指定规格为200K
debug：
    1.目录套目录支持不是很好  2021-7-5

"""

import os
import shutil
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageFile


class AppLication_UI(object):
    window = Tk()
    path = StringVar()

    def __init__(self):
        self.window.title("图片路径选择")
        Label(self.window, text="目标路径").grid(row=0, column=0)
        Entry(self.window, textvariable=self.path).grid(row=0, column=1)
        Button(self.window, text="目标路径", command=self.choice_file).grid(row=0, column=2)
        Button(self.window, text="确认", command=self.min_file).grid(row=0, column=3)
        Button(self.window, text="退出", command=self.window.quit).grid(row=0, column=4)
        self.window.mainloop()

    def choice_file(self):
        filename = filedialog.askdirectory(title="选择文件")
        self.path.set(filename)


class AppLication(AppLication_UI):
    def __init__(self):
        AppLication_UI.__init__(self)

    def compressImage(self, srcPath):
        dstPath = os.path.join(srcPath, "../newpath")

        for filename in os.listdir(srcPath):
            # 如果不存在目的目录则创建一个，保持层级结构
            if not os.path.exists(dstPath):
                os.makedirs(dstPath)

            # 拼接完整的文件或文件夹路径
            oldfile = os.path.join(srcPath, filename)
            newfile = os.path.join(dstPath, filename)
            shutil.copyfile(oldfile, newfile)

            # 如果是文件就处理
            if os.path.isfile(newfile):
                print("*****开始压缩%s*****" % newfile)
                self.compress_image(newfile)
                print("*****压缩完成%s*****" % newfile)

            # 如果是文件夹就递归
            elif os.path.isdir(oldfile):
                self.compressImage(oldfile)

    def compress_image(self, outfile, mb=200, quality=90, k=0.95):
        """不改变图片尺寸压缩到指定大小
        :param k:
        :param outfile: 压缩文件保存地址
        :param mb: 压缩目标，KB
        :param quality: 初始压缩比率
        :return: 压缩文件地址，压缩文件大小
        """

        o_size = os.path.getsize(outfile) // 1024
        print(o_size, mb)
        if o_size <= mb:
            return outfile

        ImageFile.LOAD_TRUNCATED_IMAGES = True
        while o_size > mb:
            im = Image.open(outfile)
            x, y = im.size
            out = im.resize((int(x * k), int(y * k)), Image.ANTIALIAS)
            try:
                out.save(outfile, quality=quality)
            except Exception as e:
                print(e)
                break
            o_size = os.path.getsize(outfile) // 1024
        return outfile

    def min_file(self):
        path = self.path.get()
        self.compressImage(path)


if __name__ == "__main__":
    a = AppLication()
