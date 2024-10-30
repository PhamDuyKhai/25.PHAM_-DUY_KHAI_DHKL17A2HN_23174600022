import json
obj_json = '{"name":"A","age":35,"company":"Đất Việt"}'
obj_py = json.loads(obj_json)
print(obj_py)