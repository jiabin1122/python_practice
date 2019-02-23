"""
字符串分隔
连续输入字符串，请按长度为8拆分拆分每个字符串后输出到新的字符串数组
长度不是8整数倍的字符串请在后面补数字0
空字符串不予处理
"""

def line_cut(line):
    if len(line) == 0:
        print("字符串长度为0")
    else:
        if len(line) % 8 != 0:
            num = 8 - len(line) % 8
            line += '0' * num
        i = 0
        result_list = []
        while(i < len(line)):
            result_list.append(line[i : i+8])
            i += 8
        print(result_list)

if __name__ == '__main__':
    line = input('please input line...')
    line_cut(line)