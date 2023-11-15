# Function : 
#     1) partial funcation : 

# from functools import partial

# def xyz(a, b):
#     c = a * b  # 3 * 3  3 x 3 x 3
#     print(c)
    
# xyz(3, 2)


# xy = partial(xyz, b = 2)

# xy(4)


# lambda funcation (anonymous funcation)


# def xyz(a, b):
#     c = a + b
#     print(c)

# # xyz(10, 20)

# # lambda arguments : expression

# x = lambda a, b : a + b

# print(x(2, 3))

# 1) map()
# 2) filter()
# 3) redce()


# 1) map() 

# map(funcation, itrater)

# lst = [2, 4, 5, 2, 3, 4, 5, 6, 10]

# zx = map(lambda x : x + 20, lst)

# # for i in lst
# print(list(zx))




# a = 92492834928

# for i in lst:
#     print(i)




# 2) filter()

# filter(funcation, itrater)

# lst = [2, 3, 5, 4, 6, 7, 7, 1, 3, 4, 5, 1, 3, 12, 23, 3, 5, 7, 8, 9]


# qw = filter(lambda i : i % 2 != 0, lst)

# print(list(qw))


# reduce(fubcaiton , itrater):

from functools import reduce


lst = [2, 3, 5, 4, 6, 7, 7, 1, 3, 4, 5, 1, 12]

x = reduce(lambda a, b : a + b, lst)

print(x)



[2 x 1 = 2, 2 x 2 = 4, 2 x 3 = 6, ....., 2 x 9 = 18, 2 x 10 = 20]