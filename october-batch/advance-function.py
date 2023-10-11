# python 

# lambda arguments : expression
# abc= lambda a:a*a
# print(abc(5))

# 1) map()
# 2) filter()
# 3) reduce()


# 1) map() function


# lst = [1, 3, 4, 5, 3, 7, 5, 4, 3, 2, 5, 10]


# map(function, itrater)

# zx = map(lambda i : i ** 2, lst)

# print(list(zx))


# lst = ("a", "b", "c", "d")

# qw = map(lambda a: a * 10, lst)

# print(list(qw))



# filter()  

# l = [12, 3, 2, 4, 7, 3, 7, 5, 8, 12, 8, 90, 77]


# filter(funcation, itrater)

# qw = filter(lambda j : j % 2 != 0, l)

# print(tuple(qw))


# reduce() funcation :

from functools import reduce

lst = [2, 3, 4, 5, 1, 6, 7, 1, 2, 3, 1, 2]

# reduce(lambda funcation, itrater)

# er = reduce(lambda a, b : a + b, lst)

# print(er)

# def xyz(*a):
#     b = 0
#     for i in a:
#         b = b + i
#     print(b)

# xyz(*lst)


lst = [2, 3, 4, 5, 1]


zx = map(lambda a : str(a) + "abcbca" + str(a), lst)

print(list(zx))

# output 
# ['2abcbca2', '3abcbca3', '4abcbca4', '5abcbca5', '1abcbca1']


# print(2 * "aa")

lst = [1, 2, 3, 4, 5, 6 ,7 ,8, 9, 10]

["2 x 1 = 2", "2 x 2 = 4",  .......]









        


