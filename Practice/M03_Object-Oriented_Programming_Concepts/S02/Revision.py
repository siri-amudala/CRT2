# 1. SINGLE INHERITANCE
class Father:
    def father_property(self):
        print("Father: I have a house")


class Son(Father):      
    def son_property(self):
        print("Son: I have a bike")


print("1. SINGLE INHERITANCE")
s = Son()
s.father_property()     
s.son_property()        


# 2. MULTILEVEL INHERITANCE
class Grandparent:
    def land(self):
        print("Grandparent: I have land")


class Father2(Grandparent):
    def house(self):
        print("Father: I have a house")


class Son2(Father2):
    def bike(self):
        print("Son: I have a bike")


print("\n2. MULTILEVEL INHERITANCE")
s2 = Son2()

s2.land()       
s2.house()      
s2.bike()       


# 3. HIERARCHICAL INHERITANCE
class Father3:
    def house(self):
        print("Father: I have a house")


class Son3(Father3):
    def bike(self):
        print("Son: I have a bike")


class Daughter(Father3):
    def car(self):
        print("Daughter: I have a car")


print("\n3. HIERARCHICAL INHERITANCE")

son = Son3()
daughter = Daughter()

son.house()         
son.bike()

daughter.house()    
daughter.car()


# 4. MULTIPLE INHERITANCE
class Father4:
    def father_property(self):
        print("Father: I have a house")


class Mother:
    def mother_property(self):
        print("Mother: I have jewelry")


class Son4(Father4, Mother):     
    def son_property(self):
        print("Son: I have a laptop")


print("\n4. MULTIPLE INHERITANCE")

son4 = Son4()

son4.father_property()   
son4.mother_property()   
son4.son_property()      

# 5. HYBRID INHERITANCE

class Grandparent5:
    def land(self):
        print("Grandparent: I have land")


class Father5(Grandparent5):
    def house(self):
        print("Father: I have a house")


class Son5(Father5):
    def bike(self):
        print("Son: I have a bike")


class Mother5:
    def jewelry(self):
        print("Mother: I have jewelry")

class Grandson(Son5, Mother5):
    def mobile(self):
        print("Grandson: I have a mobile")


print("\n5. HYBRID INHERITANCE")

grandson = Grandson()

grandson.land()       
grandson.house()      
grandson.bike()       
grandson.jewelry()    
grandson.mobile()     


a=10
b=19.5
c="Ram"
d=[1,2,3,4,5,6]
e=(1,2,3,4,5,6)
f={1,2,3,4,5,6}
g=("name":"siri")
print(isinstance(a,int))
print(isinstance(b,float))
print(isinstance(c,str))
print(isinstance(d,list))
print(isinstance(e,tuple))
print(isinstance(f,set))
print(isinstance(g,dict))
