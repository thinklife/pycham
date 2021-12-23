def greet_users(names):
    for name in names:
        greet=f"hello,{name}".title()
        print(greet)
greet_users(['xcq','wjg','ddd'])


unprinted_designs=['phone case','robot pendant','dodecahedron']
completed_models=[]
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f'{current_design} is print')
        completed_models.append(current_design)
def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)


def show_msg(lists):
    for l in lists:
        print(l)
lists=['a','b','d']



def send_msg(lists,sent_msg):
    for l in lists:
        print(l)
    while lists:

        msg=lists.pop()
        sent_msg.append(msg)
    for m in sent_msg:
        print(m)

send_msg(lists,[])
show_msg(lists)

def make_pizza(*toppings):
    print(toppings)
make_pizza('mushroom','cheese')



def add_toppings(*args):
    if args:
        for a in args:
            print(f'you have add {a}')
    else:
        print('you did\'t add something')
add_toppings('apple','cheese','banana')

add_toppings()


def car_info(manuf,type,**args):
    args['manuf']=manuf
    args['type']=type
    return args
car=car_info('feitian','e0--3',size=33,price=20000)
print(car)




