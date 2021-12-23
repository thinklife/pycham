def make_shirt(size='BIG',t_font='I LOVE YOU'):
    print(f"this t-shirt size:{size},font:{t_font}")

make_shirt()


def decribe_city(city_name,country='china'):
    print(f"{city_name} is in {country}")
decribe_city('wuhan')


def get_formatted_name(first_name,last_nmae,middle_name=''):
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_nmae}"
    else:
        full_name=f"{first_name} {last_nmae}"
    return full_name
xcq=get_formatted_name('xue','chao',"qiang").title()
print(xcq)


def build_person(first_name,last_name,age=None):
    person={'first_name':first_name,'last_name':last_name}
    if age:
        person['age']=age
    return person
xcq=build_person('xue','chaoqiang')
print(xcq)



while True:
    print('can you tell me your name ? ')
    f_name=input("first name: ")
    if f_name=='q':
        break
    l_nmae=input("last_name: ")
    you=get_formatted_name(f_name,l_nmae).title()
    print(f"hello,{you}")
    print('you can input q to stop it ')

