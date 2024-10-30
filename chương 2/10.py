import json as js
import os

duoi_tep = os.path.dirname(os.path.abspath(__file__))
path = duoi_tep + r"\10.json"

with open(path,encoding = "utf-8") as f:
    obj = js.load(f)
    print(obj)
    print( 'Tên công ty:' ,obj['Tên công ty'])
    print('Địa chỉ:',obj['Địa chỉ'])
    print('Tổng số nhân viên:', obj["Tổng số nhân viên"])
    print('-----Tổng số nhân viên-----')
    for i in obj['Thống kê nhân viên']:
        print(f"{i['stt']}.Tên đơn vi: {i['tên đơn vị']}")
        print(f"Số nhân viên: {i['số nhân viên']}")
        print(f"Tỷ lệ %: {i['tỷ lệ %']}")       
    
    f.close