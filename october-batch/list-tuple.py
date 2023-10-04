# for i in range(10):
#     if i == 5:
#         # break
#         # continue
#         pass
#     print(i)
#     print("hello")
#     print("xyz")
    
    
    
    
# 1) break :  to break loop
# 2) continue : to continue floow of loop
# 3) pass 




# for i in range(10):
#     pass



# assert 10 == 11 , "this is my assert line"


# Spacial data types

# 1) list : ordered, allow duplicasy, mutable
# 2) tuple : ordered, allow duplicasy, imutable
# 3) set : unordered, do not allow duplicasy, mutable
# 4) dictionry : ordered, mutable, do not aloow duplicasy



# 1) list : collcaion of multipal data in a singke cariable

# a = 10
# b = 1000
# []


# lst = [12, 100, "hlo", 10.0, 90, 100, True]

# print(type(lst))

# print(lst[2])

# print(lst[-7])


# slicing : 

# :

# lst = [12, 100, "hlo", 10.0, 90, 100, True]


# [start : end : incremet]

# print(lst[1 : 5 : 2])

# print(lst[ : : -1])



# lst = [12, 100, "hlo", 10.0, 90, 100, True]


# 1) append()
# 2) insert()

# lst.append(1000)
# lst.insert(1, 1000)


# print(lst)



# lst = [12, 100, "hlo", 10.0, 90, 100, True]

# to delete 

# 1) pop()
# 2) remove()

# lst.pop()

# lst.remove(lst[-2])

# lst.clear()
# print(lst)









# tuple : 
# ()


# tpl = (10, 40, 56, 67, 100, 89)

# print(type(tpl))
# print(tpl[3] + tpl[0])

# tpl = (10, 40, 56, 67, 100, 89)

# lst = list(tpl)

# lst.append(1000)

# # print(lst)

# tpl = tuple(lst)

# print(tpl)



# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34


# lst = []

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# lst = []

# for i in range(11):
#     if i == 6:
#         continue
#     lst.append(i)

# print(lst)