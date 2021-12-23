try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")

filename='alice11111.txt'

#计算书本的字数的函数
def count_words(filename):
    try:
        with open(filename,encoding='utf-8') as f:
            content=f.read()
    except FileNotFoundError:
        #print(f'you can not file this txt: {filename}')
        pass
    else:
        words=content.split()
        print(f'{filename} content is: {words}')
        print(f'and the num of words is {len(words)}')
count_words('alice.txt')
lists=['alice.txt','guest1.txt','hh.txt','guest_book1.txt','dont_exit.txt']
for list in lists:
    count_words(list)


#加法运算
def sum_of_two():
    while True:
        print('plz input two numbers :')

        try:
            v1=input('firstone :')
            if v1 == 'q':
                break
            vl1 = int(v1)
            v2=input('secondone :')
            if v2 == 'q':
                break
            vl2 = int(v2)

        except ValueError:


            print('plz input the right number')
        else:
            answer = vl1 + vl2
            print(answer)
#sum_of_two()

with open('alice.txt',encoding='utf-8') as f:
    content=f.read().lower()
    words=content.count('run')
    print(words)


