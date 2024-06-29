# -*- coding: utf-8 -*-

import re
import docx


# 获取docx 文件内容
def read_line_from_docx(file_path):
    document = docx.Document(file_path)
    all_paragraphs = document.paragraphs
    paragraphs_text = []
    for paragraph in all_paragraphs:
        paragraphs_text.append(paragraph.text)
    return paragraphs_text


# 在文件内容中解析所有key对应的值
def find_key_in_str(keyword, pg_text):
    match = re.search(rf"{keyword}(\w+)[\u4e00-\u9fa5,.]", pg_text)
    if match:
        return match.group(1)
    else:
        return None


# 创建一组字典，将查询出的结果写入字典中
def create_last_arr_list(keyword_list, file_path):
    global all_value
    my_dict = {}
    parag_text = read_line_from_docx(file_path)
    for keyWord in keyword_list:
        for pag_text in parag_text:
            all_value = find_key_in_str(keyWord, pag_text)
            if all_value is not None:
                my_dict[keyWord] = all_value
                break
            else:
                my_dict[keyWord] = "未解析到内容"
    return my_dict


# 将汇总完成的字典写入表格

# 解析目录下所有文件列表，并返回文件路径

# 获取待查找关键字文件，解析其内容
def read_txt(txt_path):
    file = open(txt_path, "r", encoding="utf-8")
    file_contents = file.readline()
    data = file_contents
    key_list = data.split(";")
    return key_list


if __name__ == "__main__":
    # 录入需要查找的字段，用;隔开，需要在模板文件中唯一
    read_keyword_list = read_txt("keyword.txt")
    # 需要解析的文件目录
    path = "raw_file_dir"
    text = read_line_from_docx(path)   # 打印解析出来的字符串信息，用于开发验证
    print(text)

    # 测试主函数
    a = create_last_arr_list(read_keyword_list, path)
    print(a)
