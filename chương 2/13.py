import requests
link = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
json_data = link.json()

q = 0
for i in json_data:
    q+=1
    print('postId:',i['postId'])
    print('id:',i["id"])
    print('name:',i["name"])
    print('email:',i['email'])
    print('body:',i["body"])
    print('=======================')
    if q == 3:
        break