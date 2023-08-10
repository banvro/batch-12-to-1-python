# functios : code optimization


# decleartion of function
# def xyz():
#     print("hello")
#     print("xyz")
    
    
# # call a function

# xyz()

# xyz()

# xyz()


# x = 10
# b = 20

# c = x + b

# print(c)


# peratameters
# arguments


# perameters
# def sum(a, b):
#     c = a + b
#     print("the sum is : ", c)

# arguments
# num1 = int(input("ENter first number : "))
# num2 = int(input("ENter second number : "))

# sum(num1, num2)

# sum(100, 200)

# sum(1, 2)


# arbitrary arguments
    # *args


    
# a = [1, 3, 4, 6, 10]

# # totl = 0

# for i in a:
#     totl = 0 + i
    
#     print(totl)




# def calcu(*args):
#     totl = 0
    
#     for i in args:
#         totl = totl + i
        
#         print(totl)
    

# calcu(1, 1, 10)

# [], (),


# lst = [i for i in range(9)]

# print(lst)


# wish = int(input("ENter number of elemnts you wish to operation : "))


# inpu = [int(input("ENter number : ")) for i in range(wish)]

# print(inpu)



# %%%%%%%%% calculatro *********

# wish = 4

# input == >>>>

# enter what yu wish to do....
# 1) Adation
# 2) Multiplication
# 3) Devsion
# 4) Substrtion


# choice = 1

# if choice == 1:
#     summ(inputs)

# elif....

# a = 10

# a = 100

# print(a)




def sumthis(*args):
    total = 0
    for i in args:
        total = total + i
    print(total)
    
def sub(*args):
    total = 0
    for i in args:
        total = total - i
    print(total)


def multi(*args):
    total = 1
    for i in args:
        total = total * i
    print(total)
    
def devsion(*args):
    total = 0
    for i in args:
        total = total / i
    print(total)
    
print("**************My Calculator**********")

wish = int(input("Enter number of elements : "))

userin = [int(input(f"Enter number {i + 1} : ")) for i in range(wish)]

print("""
    Enter what you wish to do...
    1) Adation
    2) Substraction
    3) Multiplication
    4) Devsion
""")

choice = int(input("Enter whta you want to do : "))

if choice == 1:
    sumthis(*userin)

elif choice == 2:
    sub(*userin)
    
elif choice == 3:
    multi(*userin)  
  
elif choice == 4:
    devsion(*userin) 
    
else:
    print("Spmeting went wrong..")
    
    
    
    


