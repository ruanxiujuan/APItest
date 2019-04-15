# json字符串  字典
# json格式规范
# 1. {}
# 2. "key": "zhangsan"/123.00/true/false/null
# 3. "a": 1, "b": 2
# 4. 不支持备注
#
# 区别:
# 1. json字符串格式,字典是字典格式
# 2. json只能用"", 字典可以用"", ''
# 3. json中true/false/null, 字典中True, False/None
# 4. json不支持备注, 字典支持

# 相互转换
# 1. 字典转json字符串
import json
d = {'b': '张三', "a": 1, "d": False, "c": None}
json_str1 = json.dumps(d)
json_str2 = json.dumps(d, indent=2, ensure_ascii=False, sort_keys=True)
print(json_str1, json_str2)
# print(type(json_str))

#  json->字典
# 字符串方便传输 不方便取值
res_text = '{"task": "记得买菜"}'
res_dict = json.loads(res_text)
print(type(res_text), type(res_dict))
print(res_dict["task"])