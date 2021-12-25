import json

numbers=[1,2,3,5,44,]
filename='numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)

with open(filename) as f:
    n=json.load(f)
print(n)

username=input('input your name')
filename1='username.json'
with open(filename1,'w') as f:
    json.dump(username,f)
    print(f'we will remember you{username}')


with open(filename1) as f:
    name=json.load(f)
    print(f'hello, {name}')


filename3='likenum.json'
likenum=input('input the num you like best')
with open(filename3,'w') as f:
    json.dump(likenum,f)

with open(filename3) as f:
    num=json.load(f)
print(f'i know your favorite number, it is: {num}')


