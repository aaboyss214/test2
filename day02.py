# def squanes(n):
#     return n*n
even_numbers = [i for i in range(51) if i %2 ==0]
#
# print(even_numbers)
# print(tuple(map(squanes,even_numbers)))
z = lambda x : pow(x,2)
print(list(map(z,even_numbers)))
