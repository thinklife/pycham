filename='learing_python.txt'
with open(filename,'a') as file_object:
    file_object.write('i love programming\n')
    file_object.write('because i love it')



filename1='guest2.txt'
name=input('plz enter your name')

with open(filename1,'w') as file_2:
    file_2.write(name)


filename3='guest_book1.txt'
log1=''
while True:
    name = input('plz input your name :(input q to quit)')
    print(f'hello, {name}')
    name_visit=f'{name} have visited \n'
    log1+=name_visit
    if name == 'q':
        break

with open(filename3,'a') as file_3:
    file_3.write(log1)


name1='whylike_file1.txt'
while True:
    reason=input('why do you like programming : (input q to quit)')
    print(reason)
    if reason=='q':
        break
    with open(name1,'a') as file_4:
        file_4.write(reason+'\n')
with open(name1,'r') as file_5:
    lines=file_5.readlines()
    for line in lines:
        print(line)
