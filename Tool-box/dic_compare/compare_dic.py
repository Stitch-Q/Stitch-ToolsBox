"""
author: stitch_xi
date： 2021-08-08
readme: 一个文件夹中文件大小对比工具，暂时支持zip文件，目标是支持可选文件类型
date: 2021-08-12
readme: 增加了可选文件类型功能，优化文件信息获取逻辑，取消了工作目录，标准化输出文件名称，隐藏掉版本，目录等冗余信息
date: 2021-08-17
readme: 整合需要比较的文件信息到munpy对象，并写入xlsx文件保存
debug：
    1.仅限于比较不同版本信息，不会强校验文件名称
    2.仅根据windows适配
"""
import os
import numpy as np
import pandas as pd


# 查找目录下所有文件的绝对路径
def find_all_file(path, src):
    pathlist = []
    for root, dirs, files in os.walk(path):
        # print('root_dir:', root)  # 当前目录路径
        # print('sub_dirs:', dirs)  # 当前路径下所有子目录
        for file in files:
            filepath = os.path.join(root, file) # 获取目录下所有文件的绝对路径
            print(filepath)
            pathlist.append(filepath)
    pathlist = find_file(pathlist, src) # 筛选只包含指定后缀的文件
    # pathlist = np.unique([j for i in pathlist for j in i])
    # pathlist = find_file(pathlist, ".zip")
    return pathlist


# 处理文件列表：
# x=np.append(x,[[1,2,3,4]],axis=0)#添加整行元素，axis=1添加整列元素
def find_file(pathlist, findsrc):
    date_list = []
    pathlist = list(pathlist)
    for filelist in pathlist:
        list1 = []
        if str(filelist).find(findsrc) == -1 or str(filelist).find(".src") != -1: # 按照指定参数查找文件，规避掉签名等冗余文件
            pathlist.remove(filelist)
            continue
        else:
            filesize = file_date(filelist) # 获取文件大小信息
            filename = find_filename(filelist) # 获取文件名称
            list1.append(filename)
            list1.append(filesize)
        date_list.append(list1) # 将数据写入xlsx
    return date_list


# 获取需要比较的目录的信息
def addfile_date(path, src):
    list2 = []
    newpathlist = find_all_file(path, src)
    for filepath in newpathlist:
        list2.append(filepath)
    return list2


# 合并数据
def lastdate(path1, path2, src):
    # 获取两组数据
    baseline_data = find_all_file(path1, src)
    newversion_data = addfile_date(path2, src)
    # 将两个二维数组合并
    nb_baseline_data = np.array(baseline_data)
    nb_baseline_data = np.append(nb_baseline_data, newversion_data, axis=1) # 按列合并二维数组
    # 整理并清除冗余数据
    dataset = np.delete(nb_baseline_data, -2, axis=1) # 删除掉倒数第二列的文件名称信息
    write_excel(dataset, path1)
    return dataset

# 获取工作目录下的文件信息
def file_date(path):
    fileinfo = os.stat(path)
    filesize = fileinfo.st_size/float(1024*1024) # 单位为M
    filesize = round(filesize, 2)
    return filesize


# 获取标准文件名称：
def find_filename(path):
    filename = path.split("-")[0]  # 过滤版本号以及后缀影响
    filename = filename.split("\\")[-1] # 过滤绝对路径下的文件名
    return filename

# 将获取到的文件信息写入到xls中
def write_excel(data, path):  # 将获取到的文件信息写入到xls中 numpy ====> xlsx
    pkg_version = path.split("\\")[-1] # 通过\\分割获取文件夹名称
    P_data = pd.DataFrame(data)
    # 格式化数据
    write = pd.ExcelWriter(r"D:\testfile\$s目录比较结果.xlsx" %pkg_version)
    # 创建xlsx文件
    P_data.to_excel(write, "对比结果")  #header=[表头] # 指定sheet页名称，以及表头（可选）
    write.save()

    write.close()
    pass


# 处理excel文件中的数据
def process_date():
    pass


if __name__ == '__main__':
    workpath = r"D:\testfile"
    pathlist = find_all_file(workpath, ".zip")
    print(pathlist)