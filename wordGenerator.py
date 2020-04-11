from xml.etree import ElementTree as ET
import openpyxl
import os.path
import re
from googletrans import Translator
# from translate import Translator


def write_xml(file_name, ret):
    file_name = file_name+".xlsx"
    if os.path.isfile(file_name):
        wb = openpyxl.load_workbook(file_name)
    else:
        wb = openpyxl.Workbook()
    ws = wb.active
    i = 1
    # trans_list = []

    trans = ""
    trans_result = ""
    translator = Translator(service_urls=["translate.google.cn"])
    for (key, value) in ret.items():
        ws.cell(i, 1, key)
        ws.cell(i, 2, value)
        trans = trans+key+". "
        if(i % 200 == 0):  # google translator一次只允许翻译5000个字符，一般单词少于20个字符
            trans_result = trans_result + \
                translator.translate(trans, dest='zh-CN').text
            trans = ""
        i = i+1

    if trans != "":
        trans_result = trans_result + \
            translator.translate(trans, dest='zh-CN').text

    # 翻译后变成中文逗号，不用空格分隔，避免上下文联系，，，，实际上更复杂，试验后发现使用句号上下文联系最少，如果使用特殊符号，google翻译会自动清楚，怪google太智能 orz
    trans_result_list = trans_result.split("。")

    i = 1
    for temp in trans_result_list:
        ws.cell(i, 3, temp)
        i = i+1

    wb.save(filename=(file_name))


def auto_generate_word(source_file, delete_file, is_use_eudic):
    text = dict()
    file = open("data/"+source_file, "r")
    file_text = file.read()
    file_text = file_text.lower()

    file_text = re.sub('-[\n\t]+', '', file_text)
    word_list = re.findall('[a-zA-Z\-\'][a-zA-Z\-\'][a-zA-Z\-\']+',
                           file_text)  # 至少3个字符的才能入选，一个单词和两个单词太简单，而且容易导致翻译依赖
    for word in word_list:
        if word not in text:
            text[word] = 1
        else:
            text[word] += 1

    file2 = open("data/"+delete_file, "r")
    delete_text = file2.read()
    delete_word_list = re.findall('[a-zA-Z\-\']+', delete_text)
    delete_text = set()
    for delete_word in delete_word_list:
        delete_text.add(delete_word)

    ret = dict()
    if is_use_eudic:
        tree = ET.parse("data/udicWord.xml")
        dic = set()
        for elem in tree.iter(tag='CustomizeListItem'):
            dic.add(elem.get("word"))

        dic = (dic-delete_text)
        for (key, value) in text.items():
            if key in dic:
                ret[key] = value
    else:
        for (key, value) in text.items():
            if key not in delete_text:
                ret[key] = value

    file.close()
    file2.close()
    return ret


def main():
    # need set
    ##############################
    is_use_eudic = False
    # source_file = "17.txt"
    source_file = "大空头字幕.srt"
    delete_file = "delete.txt"
    ##############################
    ret = auto_generate_word(source_file, delete_file, is_use_eudic)

    write_xml("word_lists", ret)


if __name__ == "__main__":
    main()
