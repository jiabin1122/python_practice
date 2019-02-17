"""
华为机试 8/108
合并表记录
数据表记录包含表索引和数值，请对表索引相同的值进行合并，即相同的索引的数值进行求和运算
输出按照key值升序进行输出
"""
list_demo = [('b',2),('a',3),('a',1)]

num0 = list_demo[0][0]
dict_temp = {num0:0}
dict_result = {}

for item in list_demo:
    if item[0] in dict_temp:
        dict_temp.update({item[0] : dict_temp[item[0]] + item[1]})
    else:
        dict_temp.update({item[0]: item[1]})

keys = list(dict_temp.keys())
keys.sort()
for item in keys:
    dict_result.update({item : dict_temp[item]})
print(dict_result)

