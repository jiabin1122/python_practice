"""
计算字符个数
接受一个由字母和数字组成的字符串，和一个字符
输出字符串中含有该字符的个数，不区分大小写
"""

def words_count(line, word):
    line.lower()
    word.lower()
    print(len([item for item in line if item == word]))

def words_count2(line, word):
    line.lower()
    word.lower()
    print(len(line.split(word)) - 1)


if __name__ == '__main__':
    line = input('please input lin...')
    word = input('please input single word...')
    words_count(line, word)