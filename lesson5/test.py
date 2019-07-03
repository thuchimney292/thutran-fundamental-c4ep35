# # s = 0
# # n = int(input('Enter n= '))
# # for i in range(n):
# #     k = int(input('Enter number '+str(i+1)+' = '))
# #     s = s+k
# # print('Sum = ', str(s))
# # s = 0
# # m = int(input('Enter m= '))
# # for i in range(m):
# #     k = int(input('Enter number '+str(i+1)+' = '))
# #     s = s+k
# # print('Sum = ', str(s))
# # print('Average = ', str(s/m))

# def sum_(n):
#     sum = 0
#     for i in range(n):
#         sum += float(input('Enter number '+str(i+1)+' = '))
#     return sum

# n = int(input('Enter n= '))
# print('sum = ' + str(sum_(n)))
# m = int(input('Enter m= '))
# print('Average = '+str(sum_(m)/m))
# def evaluate(a,b,c):
#     if c=='+':
#         return a+b
#     elif c=='-':
#         return a-b
#     elif c=='*':
#         return a*b
#     elif c=='/':
#         return a/b
# print(evaluate(1,3,'+'))
# from ... import * (if all)
from math import *
def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, round(sqrt(n))+1):
            if n % i == 0:
                return False
    return True
n = int(input('Enter N: '))
for i in range(1000,10000)
print(is_prime(n))
