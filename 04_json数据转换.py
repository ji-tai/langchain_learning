import json
import sys

#设置一个字典
d = {
    'name':'鸡泰',
    'age':'19',
    'gender':'男'
}

print(d)
print(str(d))#将字典格式转换为字符串
#将字典的格式转换为json
j = json.dumps(d, ensure_ascii=False)#可以将字典格式转换为json或字典数组转换为json格式
print(j)

#将json格式的字符串转换为字典
json_str = '{"name": "鸡泰", "age": "19", "gender": "男"}'
json_array_str = '[{"name": "鸡泰", "age": "19", "gender": "男"},{"name": "无", "age": "18", "gender": "女"}]'
res_dict=json.loads(json_str)
res_array=json.loads(json_array_str)