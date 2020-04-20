# -*- coding:utf-8 -*-
from xml.etree import ElementTree as ET


def transXML2Txt():
    file = open(outputFile, 'w', encoding="utf-8")
    tree = ET.parse(eudicXMLFileName)
    for elem in tree.iter(tag='CustomizeListItem'):
        file.write(elem.get("word") + '\n')
    file.close()


if __name__ == "__main__":
    eudicXMLFileName = "udicWord.xml"
    outputFile = "eudic_words.txt"
    transXML2Txt()
