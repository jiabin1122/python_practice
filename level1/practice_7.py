"""
7.取近似值
接受一个正浮点数
输出该数值的近似整数值
如果小数点后数值大于等于5，向上取整；小于5，则向下取整
"""

def print_num(num):
    k,f = num.split('.')
    if int(f[0]) >= 5:
        return int(k) + 1
    else:
        return int(k)

if __name__ == '__main__':
    num = input('please input float...')
    print(print_num(num))
