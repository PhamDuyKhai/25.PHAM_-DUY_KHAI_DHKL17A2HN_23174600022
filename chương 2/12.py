import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response)
json_data = response.json()
print(json_data)
print('tổng số bài post:',len(json_data))
for i in json_data:
    print('userId:',i["userId"])
    print('id:',i["id"])
    print('title:',i["title"])
    print('body:',i["body"])
    print('============================')