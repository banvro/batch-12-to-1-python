x = input("Enter first number : ")
num1sav = open("num1.txt", "w")
num1sav.write(x)
num1sav.close()

y = input("Enter second number : ")
num2sav = open("num2.txt", "w")
num2sav.write(y)
num2sav.close()

z1 = open("num1.txt", "r")
myval1 = z1.read()
z1.close()

z2 = open("num2.txt", "r")
myval2 = z2.read()
z2.close()

zx = int(myval1) + int(myval2)

fil = open("result.txt", "w")
fil.write(str(zx))
fil.close()