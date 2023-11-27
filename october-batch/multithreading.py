import threading

def car():
    for i in range(1, 100):
        print("yessss")
    
def bus():
    for i in range(1, 100):
        print("noooooooooooo")

# car()
# bus()

th1 = threading.Thread(target = car)
th2 = threading.Thread(target = bus)

th1.start()
th2.start()

print("hloooo")

print("mportant code")

print("gooooo")


th1.join()
th2.join()
print("done")



# a = 10
# b = 20

# c= a + b
# d = c + 100

# print(d)