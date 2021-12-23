import time
from random import randint,choice
class Die:
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        print(f'{randint(1,self.sides)}')

di=Die(6)
di.roll_die()
bi=Die(19)
bi.roll_die()



class Toss:

    def __init__(self,args):
        self.args=args
        self.num=4
        self.nums=[]
    def toll_num(self):
        for n in range(self.num):
            jg=choice(args)
            self.nums.append(jg)
        print(f"current jgs is {self.nums}")
    def set_nums(self):
        self.nums=[]
args=[1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
ts=Toss(args)
times=0
while True:
    ts.toll_num()
    times+=1
    if ts.nums==[1,2,'a','b']:
        print(f'after {times} times,you win')
        break
    ts.set_nums()

time.sleep(1)
#用函数试试
def run_toll(args):
    jgs=[]
    time=0
    while True:
        for a in range(4):
            jg=choice(args)
            jgs.append(jg)
        time+=1
        print(jgs)
        if jgs==[1,2,'a','b']:

            print(f'you win by {time} times')
            break
        jgs=[]
run_toll(args)





