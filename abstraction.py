
# class clas1:
#     def



# from abc import ABC, abstractmethod
# # interface
# class clas1(ABC):
#     @abstractmethod
#     def usernmae(self):
#         # print("i am usernmae")
#         pass
    
#     # @abstractmethod
#     def age(self):
#         print("I am age")
        
# class clas2(clas1):
#     def car(self, a, b, c):
#         z = a + b + c
#         print("The sum is : ", z)
    
#     def usernmae(self):
#         print("done")
        
# obj = clas2()

# obj.car(12, 1, 2)


# Encapsulation : 
    # Access spacifiers : 
    
    # 1) Public mambers
    # 2) Private mambers  __
    # 3) Protected mambers     _
    
    
# class clas1:
#     def __init__(self, a, b):
#         self.num1 = a
#         self.__num2 = b
    
#     def hlo(self):
#         print(self.__num2)
        
# class clas2(clas1):
#     def data(self):
#         print(self.__num2)
        
# obj = clas2(12, 10)

# # print(obj.num1)
# obj.hlo()
        

# 10 + 20










# Polymorphisum : 
    # poly   =  many
    # morphiusm   = forms
    
    # 1) Duck typing
    # 2) Operator overloading
    # 3) Method Overloading
    # 4) Method Overriding
    

# class clas1:
#     def move(self):
#         print(" i am from clas 1")
    
# class clas2:
#     def move(self):
#         print(" i am from clas 2")

# obj1 = clas1()
# obj2 = clas2()


# def duck(a):
#     a.move()

# duck(obj1)




# 2) Operator Loading : 


# a = 20

# a = 100

# print(a)

# class clas1:
#     def __init__(self, a, b):
#         self.num1 = a
#         self.num2 = b
    
#     def sumthis(self):
#         print("ok")
    
#     def __add__(info, data):
#         m1 = info.num1 + data.num1
#         m2 = info.num2 + data.num2
#         sum = clas1(m1, m2)
#         return sum

# obj1 = clas1(10, 20)
# obj2 = clas1(5, 8)

# c = obj1 + obj2

# print(c.num2)
# 10 + 20



# c) Method Overloading : 
# class clas1:
#     def sumthis(self, a, b, c):
#         z = a + b + c
#         print(z)
    
#     def sumthis(self, a, b):
#         z = a + b
#         print(z)

#     def sumthis(self, a):
#         z = a
#         print(z)

# obj = clas1()

# obj.sumthis(10, 12)

# def d(a = 20, b = 10):
#     c = a + b
#     print(c)
    
# d(1, 2)

# class xyz:
#     def ok(self, a = None, b = None, c = None):
#         if a != None and b != None and c != None:
#             zx = a + b + c
#             print("the sum is : ", zx)
        
#         elif a != None and b != None:
#             zx = a + b
#             print("the sum is : ", zx)
        
#         elif a != None:
#             zx = a
#             print("the sum is : ", zx)

# obj = xyz()

# obj.ok(12, 20, 10)


# class clas1:
#     def sumthis(self, a, b, c):
#         z = a + b + c
#         print(z)
    
#     def sumthis(self, a, b):
#         z = a + b
#         print(z)
    
#     def sumthis(self, a):
#         z = a
#         print(z)

# obj = clas1()

# obj.sumthis(12)


# class clas1:
#     def sumthis(self, a = None, b = None, c = None):
#         if a != None and b != None and c != None:
#             z = a + b + c
#             print(z)
        
#         elif a != None and b != None:
#             z = a + b
#             print(z)
        
#         elif a != None:
#             z = a
#             print(z)
            
# obj = clas1()
# obj.sumthis(10, 100)




# Method overriding


class clas1:
    def car(self):
        print("i am car")
        
    def bus(self):
        print("i am bus")
    
class clas2(clas1):
    def train(self):
        print("i am train")
        
    def car(self):
        print("now i am new car")

obj = clas2()
obj.car()






