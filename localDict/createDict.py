# -*- coding:utf-8 -*-
import re
from xml.etree import ElementTree as ET
import bs4
from bs4 import BeautifulSoup
import os


def create():

    file = open("柯林斯双语词典.txt", 'r', encoding="utf-8")
    line_list = file.read().split("\\n\n")
    file.close()
    ret = ""

    # print(line_list[-5:-1])
    for line in line_list:
        soup = BeautifulSoup(line, features="lxml")
        # print(soup.prettify())
        try:
            word = soup.body.p.font.string
        except:
            save_file(ret)

        print(word)
        # if word=='a':
        #     print(soup.prettify())

        # spans = soup.body.div.div.div.div.div.find_all('span')
        spans_num = soup.body.find_all('span', 'num')
        # spans_st = soup.body.find_all('span','st')
        spans_trans = soup.body.find_all('span', 'text_blue')

        trans_ret = ""

        num_tranl=0
        for i in range(0, len(spans_num)):
            # trans_ret=trans_ret+spans_num[i].string+spans_st[i].string+spans_trans[i].string+"; "
            # if spans_trans[i].text != None:
            transl=spans_trans[i].text

            if transl=="" or re.search('[a-z]', transl):
                i+=1
                continue
            num_tranl+=1
            trans_ret = trans_ret + str(num_tranl)+'.' + transl + "; "
            i+=1

        print(str(num_tranl)+"::"+trans_ret)
        if trans_ret=="":
            ret = ret + word + '#### '+ str(num_tranl)+'::' + '\n'
        else:
            ret = ret + word + '####'+ str(num_tranl)+'::'+ trans_ret + '\n'

        save_file(ret)


def save_file(ret):
    file = open("local_dict.txt", 'w', encoding="utf-8")
    file.write(ret)
    file.close()


if __name__ == "__main__":
    if os.path.isfile("local_dict.txt"):
        print("local_dict.txt is existed")
    else:
        create()
