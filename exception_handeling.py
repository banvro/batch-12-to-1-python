
# Exception Handeling : 

# Errors:

# a = 10

# if b == a
#     print(b)


# types of errors
    # 1) Compile time errror
    # 2) Logical Error 
    # 3) RUn time error



# 1) compile time error :  (sytex error)

# a = 10

# if b == a
#     print(b)

# 2) Logical Errror : 

# a = 30
# b = 0

# print(a/b)


# 3) RUn time error : 

# phone_number = int(input("Please enter your phone number : "))

# print(phone_number)




# strat........

# print("i am strat...")
# a = 30
# b = 0
# try:
#     phone_number = int(input("Please enter your phone number : "))
#     print(phone_number)

#     print(a / b)

# except ZeroDivisionError:
#     print("You cant devide anything by zero")

# except ValueError:
#     print("ENter vaid phon pun we")

# except Exception as e:
#     print(e)

# print("i am running")

# print("i am done")


# Standred foramt of excaptions


# try:
#     age = int(input("Enter your age : "))

# except Exception as e:
#     print(e)

# else:
#     print("My age is : ", age)

# finally:
#     print("I am done..")




try:
    age = int(input("Enter your age : "))
    def car(a, b):
        c = a + b
        print(c)

except Exception as e:
    print("Someting went wrong with your age")

else:
    car(12, 10)
    if age > 18:
        print("You ar eeleigibal for voat")
    
    else:
        print("You are not eligible")

finally:
    print("i am done")