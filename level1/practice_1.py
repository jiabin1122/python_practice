"""
字符串最后1个单词长度，单词以空格隔开
"""

def last_word_len(line):
    print(len(line.split()[-1]))


if __name__ == '__main__':
    line = input('please input line...')
    last_word_len(line)