# Erros : 
#     1) Compile time error
#     2) Logical Error
#     3) Run Time Error
    
    
# 1) Compile time error : ( Syntex Error)

# a = 10
# b 2
# c = a + b

# print(c)



# if 10 == 10:
#     print("hellooooo")


# 2) Logical Errors:


# a = 10
# b = 0

# c = a / b

# prnt(c)



# Run time Error : 

# age = int(input("Enter your Age : "))





# a = 10
# b = 20

# c = a + b
# print(c)

# age = int(input("Enetr your age : "))

# print("age")

# print("imporent code")

# print("okkkk")

# print("done")


# Handling error 


# try:
#     # doutable code

# except Exception:
#     # handle Error

# else:
#     # execute only if try block have no error

# finally:
#     # execute......

a = 10
b = 8

try:
    c = a/b
    while True:
              
        age = int(input("Enter your age : "))


except ZeroDivisionError:
    print("you never devide anything with zero")

except ValueError:
    print("Enter somehtig valid")

except Exception:
    print("you never devide anything with zero")

else:
    print("user age is : ", age)

finally:
    print("exception handleing odne")

print("hlooooo")

print("inowejevf")
print("okkkkkkk")















