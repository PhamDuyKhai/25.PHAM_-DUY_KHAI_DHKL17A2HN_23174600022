import json
obj_python = {'name':'Khải','age':20}
obj_json = json.dumps(obj_python, ensure_ascii = False)
print(obj_json)