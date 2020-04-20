# -*- coding:utf-8 -*-


def exchange():
    for fileName in fliterNameFile:
        file = open(fileName, 'r', encoding="utf-8")
        txt_string = file.read()
        word_list = txt_string.split("\n")
        file.close()

        file = open(fileName, 'a', encoding="utf-8")
        result = ""
        for word in word_list:
            # result = result + word + '\n'
            result = result + word.lower() + '\n'
            # print(word)
        file.write(result)
        file.close()


if __name__ == "__main__":
    fliterNameFile = ["fliter_first_name.txt", "fliter_second_name.txt"]
    exchange()
