"""
author: stitch
date： 2022-01-02
readme: 这是一个解析json文件并比较的脚本,解决CIE 工作中需要check 版本变更情况
debug：
    1.

"""
import os
import json


def readfile(jsonpath):
    # 打开文件
    with open(os.path.join(jsonpath), "r", encoding='utf-8') as f:
        # 转化成python类
        cmp_info = json.load(f)
        return cmp_info


def load_compare_version(service_data, filepath):
    """
    遍历读取service对应version到新的dict中，准备进行对比
    :return: dict{servicename:serviceversion}
    """
    dictlist = {}
    for serviceVersion in service_data:
        # print(type(serviceVersion))
        # print(serviceVersion)
        service = serviceVersion["name"]
        serviceversion = serviceVersion['version']
        servicename = str(service).split('/')[len(str(service).split('/'))-1]
        dictlist[servicename] = serviceversion
    filename = str(filepath).split('\\')[len(str(filepath).split("\\")) -2]

    print(f"*********start fomat {filename}*********")
    print(dictlist)
    return dictlist


def compare(old_file, new_file):
    # 部分服务包不需要关注，增加服务包白名单
    whitelist = ["iMAPCommonII"]
    old_dict = readfile(old_file)
    new_dict = readfile(new_file)
    # result = json_tools.diff(old_list_dict, new_list_dict)
    old_result = load_compare_version(old_dict, old_file)
    new_result = load_compare_version(new_dict, new_file)
    # 遍历两个dict 进行version 字段比较
    for key in old_result:
        if key in whitelist:
            continue
        else:
            if old_result[key] == new_result[key]:
                print("%s服务版本号一致" % key)
            else:
                print("%s 服务版本号不一致，请关注" % key)


def compareload(old_file, new_file, file3=None):
    """
    不同场景需要比较不同的版本，部分场景只涉及Euler和Arm，部分场景设计Euler,Arm,或者更多
    :return:
    """
    # 仅比较Euler和Arm
    if file3 is None:
        compare(old_file, new_file)
    # 需要比较Euler,Arm,SUSE12
    else:
        compare(old_file, new_file)
        compare(old_file, file3)


if __name__ == "__main__":
    oldfile = r"D:\Documents\myGithub\CIEngineer\Stitch-ToolsBox\Tool-box\fomat_file\testfile\test.json"
    newfile = r"D:\Documents\myGithub\CIEngineer\Stitch-ToolsBox\Tool-box\fomat_file\testfile\testII.json"
    compareload(oldfile, newfile)
