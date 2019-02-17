"""
华为机试 9/108
提取不重复整数
输入一个int型整数，按照从右向左的阅读顺序
返回一个不含重复数字的新整数
"""

def new_num(num):
    list_result = []
    [list_result.append(num[len(num)-i-1]) for i in range(len(num)) if num[len(num)-i-1] not in list_result ]
    print(list_result)
    print(''.join(list_result))

def new_num1(num):
    list_result = []
    num = list(num)
    num.reverse()
    [list_result.append(num[i]) for i in range(len(num)) if num[i] not in list_result ]
    print(''.join(list_result))

if __name__ == '__main__':
    num = input('please input num...')
    new_num1(num)