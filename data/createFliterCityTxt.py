# -*- coding:utf-8 -*-
from xml.etree import ElementTree as ET


def transXML2Txt():
    file = open(outputFile, 'w', encoding="utf-8")
    tree = ET.parse(fliterCityXMLFileName)
    for elem in tree.iter(tag='CountryRegion'):
        file.write(elem.get("Name")+'\n')
        file.write(elem.get("Name").lower() + '\n')
    for elem in tree.iter(tag='City'):
        file.write(elem.get("Name")+'\n')
        file.write(elem.get("Name").lower() + '\n')
    file.close()


if __name__ == "__main__":
    fliterCityXMLFileName = "en_city.xml"
    outputFile = "fliter_city.txt"
    transXML2Txt()
