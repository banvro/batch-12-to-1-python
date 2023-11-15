# # Inheritance : 
    
# class userdetail:
#     def _init_(self, a, b):
#         self.name = a
#         self.age = b

#     def saveinfo(self):
#         print(f"username = {self.name} and user age is = {self.age}")

# obj = userdetail("moris", 20)
# obj.saveinfo()
# obj2 = userdetail("kriss", 21)
# obj3 = userdetail("hlo", 90)

# # super() => 

# class newclass(userdetail):
#     def _init_(self, a, b, c):
#         super()._init_(a, b)
#         self.number = c
    
#     def saveinfo(self):
#         print(f"username = {self.name} and user age is = {self.age} and number = {self.number}")
        
# obj = newclass("new record", 23, 29836493)
# obj.saveinfo()


# Types of interitance:
#     1) Single Interitance  :  
#         1 parent have 1 child
        
#     2) Multiple Interitance :
#         1 child have multiple parent
        
#     3) Multilevel Inheritnace:
#         child -> parent -> grandparent
        
#     4) Hierarichal Inheritance :
#         1 parent have multiple child
        
#     5) Hybrid Inheritance:
#         combination of 2 or more then 2 inheritnace


# 2) Multiple inheritnace:
# class cls1:
#     def mthd1(self):
#         print("this is method 1")
    
#     def mthd2(self):
#         print("this is method 2")

# class cls2:
#     def mthd3(self):
#         print("this is method 3")
    
# class cls3(cls1, cls2):
#     def mthd4(self):
#         print("this si method 4")

# obj = cls3()

# obj.mthd3()


# 3) Multilevel inheritnace:

# class grandparent:
#     def mthd1(self):
#         print("this is method 1")
    
#     def mthd2(self):
#         print("this is method 2")

# class parent(grandparent):
#     def mthd3(self):
#         print("this is method 3")
    
# class child(parent):
#     def mthd4(self):
#         print("this si method 4")

# obj = child()
# obj.mthd3()


# 4) Hirerachical inheritance:

# class cls1:
#     def mthd1(self):
#         print("this is method 1")
    
#     def mthd2(self):
#         print("this is method 2")

# class cls2(cls1):
#     def mthd3(self):
#         print("this is method 3")
    
# class cls3(cls1):
#     def mthd4(self):
#         print("this si method 4")

# obj = cls3()



# 5) Hybrid inheritance:

# class cls1:
#     def mthd1(self):
#         print("this is method 1")
    
#     def mthd2(self):
#         print("this is method 2")

# class cls2(cls1):
#     def mthd3(self):
#         print("this is method 3")
    
# class cls3(cls1):
#     def mthd4(self):
#         print("this si method 4")
        
# class cls4(cls2, cls3):
#     def mthd5(self):
#         print("this is method 4")

# obj = cls4()
# obj.mthd3()