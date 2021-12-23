class Restaurant:
    '''first class test'''
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_save =0

    def describe_restaurant(self):
        print(f'this restaurant name is: {self.restaurant_name},and cuisine type is  {self.cuisine_type} ')
    def open_restaurant(self):
        print(f'{self.restaurant_name} is now opening')
    def set_number_save(self,pps):
        self.number_save=pps
    def increment_number_saved(self,addpp):
        self.number_save+=addpp


my_restaurant=Restaurant('xcq','big')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print(my_restaurant.restaurant_name)
print(f'have {my_restaurant.number_save} people total')
my_restaurant.set_number_save(200)
print(my_restaurant.number_save)
my_restaurant.increment_number_saved(100)
print(my_restaurant.number_save)






class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.attempts=0
    def describe_user(self):
        print(f'full {self.first_name} {self.last_name}')
    def greet_user(self):
        print(f'hello,{self.first_name} {self.last_name}')
    def increment_login_attempts(self):
        self.attempts+=1
    def reset_login_attempts(self):
        self.attempts=0


me=User('xcq','hh')

me.describe_user()
me.increment_login_attempts()
me.increment_login_attempts()
print(me.attempts)
me.reset_login_attempts()
print(me.attempts)

#类的继承和重写
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['apple','banana','melon']
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)
my_ice=IceCreamStand('xcq','30')
my_ice.show_flavors()


class Priveleges:
    def __init__(self,priveleges):
        self.priveleges=priveleges
    def show_privileges(self):

        for privilege in self.priveleges:
            print(privilege)

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)

    priveleges=Priveleges(['can add post','can delete post','can ban user'])





a=Admin('xue','chaoqiang')
a.priveleges.show_privileges()




