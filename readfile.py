with open('learing_python.txt') as file_1:
    print(file_1)
    #print(file_1.readlines())
    lines=file_1.readlines()
str11=''
for line in lines:
    str11+=line.replace('PYTHON','C')

print(str11)

