import json


filename4 = 'likenum6.json'
def rem_num():
    try:
        likenum1=get_old_num()
    except FileNotFoundError:
            likenum1 = get_new_num()
            print(f'we have remmber your favarite num {likenum1}')
    else:

        print(f'is  {likenum1} your favorite num now ?')
        band=input('yes/no')
        if band=='no':
            get_new_num()
        else:
            print(f' {likenum1}  is still your favorite num ')
def get_old_num():
    with open(filename4) as f:
        old_num = json.load(f)
        return old_num

def get_new_num():
    with open(filename4,'w') as f:
        new_num=input('plz input your favorite num :')
        json.dump(new_num,f)
        return new_num

rem_num()