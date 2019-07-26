#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu", 
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
#Make sure to return the result as a float even if the total
#is a round number (e.g. for burrito with no meat or
#guacamole, return 5.0 instead of 5).


#Write your code here!
class Burrito:

    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, corn=False):
        self.meat = self.set_meat(meat)
        self.to_go = self.set_to_go(to_go)
        self.rice = self.set_rice(rice)
        self.beans = self.set_beans(beans)
        self.extra_meat = extra_meat
        self.guacamole = guacamole
        self.cheese = cheese
        self.pico = pico
        self.corn = corn

    def set_meat(self, meat):
        valid = ["chicken", "pork", "steak", "tofu", False]
        if meat in valid:
            self.meat = meat
        else:
            self.meat = False
        return self.meat
    
    def set_to_go(self, to_go):
        valid = [True, False]
        if to_go in valid:
            self.to_go = to_go
        else:
            self.to_go = False
        return self.to_go
            
    def set_rice(self, rice):
        valid = ["brown", "white", False]
        if rice in valid:
            self.rice = rice
        else:
            self.rice = False
        return self.rice
            
    def set_beans(self, beans):
        valid = ["black", "pinto", False]
        if beans in valid:
            self.beans = beans
        else:
            self.beans = False
        return self.beans
            
    def set_extra_meat(self, extra_meat):
        valid = [True, False]
        if extra_meat in valid:
            self.extra_meat = extra_meat
        else:
            self.extra_meat = False
        return self.extra_meat
            
    def set_guacamole(self, guacamole):
        valid = [True, False]
        if guacamole in valid:
            self.guacamole = guacamole
        else:
            self.guacamole = False
        return self.guacamole
            
    def set_cheese(self, cheese):
        valid = [True, False]
        if cheese in valid:
            self.cheese = cheese
        else:
            self.cheese = False
        return self.cheese
    
    def set_pico(self, pico):
        valid = [True, False]
        if pico in valid:
            self.pico = pico
        else:
            self.pico = False
        return self.pico

    def set_corn(self, corn):
        valid = [True, False]
        if corn in valid:
            self.corn = corn
        else:
            self.corn = False
        return self.corn

    def get_meat(self):
        return self.meat

    def get_to_go(self):
        return self.to_go

    def get_rice(self):
        return self.rice

    def get_beans(self):
        return self.beans

    def get_extra_meat(self):
        return self.extra_meat

    def get_guacamole(self):
        return self.guacamole
    
    def get_cheese(self):
        return self.cheese

    def get_pico(self):
        return self.pico

    def get_corn(self):
        return self.corn

    def get_cost(self):
        cost = 5.0
        if self.meat in ['chicken', 'pork', 'tofu']:
            cost += 1.0
        if self.meat == 'steak':
            cost += 1.5
        if self.extra_meat == True and self.meat != False:
            cost += 1.0
        if self.guacamole == True:
            cost += 0.75
        return cost

#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs.
#
#If your function works correctly, this will originally
#print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())
