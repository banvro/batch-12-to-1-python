# Recursion : when a function calling itself and fall in a infite loop.

# factorial:

# 4 => 4 x 3 x 2 x 1
# 3 => 3 x 2 x 1


# def fabnoci(n):
#     if n < 1:
#         return 1
#     return n * fabnoci(n-1)

# zx = fabnoci(5)

# print(zx)



# 0, 1, 1, 2, 3, 5, 8, 13




def fabnoci(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return fabnoci(n - 1) + fabnoci(n - 2)
for i in range(0, 10):
    zx = fabnoci(i)
    print(zx)

# z = fabnoci(6)
# print(z)

# 0, 1, 1, 2, 3, 5, 8