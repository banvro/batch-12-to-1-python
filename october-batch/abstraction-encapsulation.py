# OOps:
#     Class
#     object
#     self
#     constructer
#     methods
#     attributes
#     Inharitance:
#         single inheritance
#         multiple inheritance
#         multilevel inheritance
#         heriarichical inheritnce
#         Hybrid inheritance
        
#     Abstraction:
#         abstract class
#         abstract method
#         interfaces


# Abstraction : (data hiding)

# abc = abstract base class

# from abc import ABC, abstractmethod

# class cls1(ABC):
#     @abstractmethod
#     def car(self):
#         pass
    
#     @abstractmethod
#     def bus(self):
#         pass

# class cls2(cls1):
#     def train(self):
#         print("this is a train")
    
#     def car(self):
#         print("this is a var")
    
#     def bus(self):
#         print("this is bus")

# obj = cls2()
# obj.car()





# 1) Encpsulation
# 2) Polymorhisum





# 1) Encpsulation:
#     when you bindup multiple things in a  single unit is called encapsulation.


# Access Spacifires:
#     1) Public mambers
#     2) Protected mambers _
#     3) Private mambers __


# class myclass:
#     def _init_(self):
#         self.__name = "moris"
#         self.age = 20
    
#     def info(self):
#         print("this is info", self.__name)

# class newcls(myclass):
#     def data(self):
#         print("this is data")
        
        
# obj = myclass()

# obj.info()

# print(obj.__name)







# class h:
#     def _init_(self, a, b):
#         self.name = a
#         self.age = b
    
#     def car(self):
#         print("this is car", self.name)

# obj = h("hlo", 10)

# obj.car()
