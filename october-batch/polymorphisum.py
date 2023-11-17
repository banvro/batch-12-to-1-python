# polymorphism : 
    # 1) poly : many
    # 2) morphism : forms
    
    # when one thing have multiple forms.
    
# types of polymorphism:
#     1) compile time polymorphism
#         1) method overloading
#         2) operator overloading
        
#     2) run time polymorphism
#         1) method overriding


    # 2) operator overloading
    
# 10 + 20

# operands : 10, 20

# operator : +
    
    
# +
    
    
    # print(20 + "kjasbd")

    
# class mycls:
#     def _init_(self, a, b):
#         self.num1 = a
#         self.num2 = b
    
#     def bus(self):
#         print("this is BUS")
    
#     def _add_(self, other):
#         x = self.num1 + other.num1
#         y = self.num2 + other.num2
        
#         sum = mycls(x, y)
#         return sum

# obj = mycls(20, 30)
    
# obj1 = mycls(10, 40)
    
# c = obj + obj1

# print(c.num2)
    
    
# a = 10

# a = 200

# print(a)
    
    
    
    
# 1) method overloading: 

# class mycls:
#     def sumthis(self, a, b, c):
#         zx = a + b + c
#         print(zx)
    
#     def sumthis(self, a, b):
#         zx = a + b
#         print(zx)
    
#     def sumthis(self, a):
#         zx = a
#         print(zx)
    
# obj = mycls()
# obj.sumthis(12, 10)

# &
# |
# !


class myself:
    def sumthis(self, x = None, y = None, z = None):
        if x != None and y != None and z != None:
            zx = x + y + z
            print(zx)
        
        elif x != None and y != None:
            zx = x + y
            print(zx)
        
        elif x != None:
            print(x)
        
        else:
            print("enter somehtng")
            
obj = myself()
obj.sumthis(10, 20, 30)
