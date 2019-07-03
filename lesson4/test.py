# dictionary = {'computer': 'may tinh', 'mouse': 'chuot', 'keyboard': 'ban phim'}
# while True:
#     word = input('Enter word: ')
#     if word in dictionary:
#         print("Meaning: ", dictionary[word])
#     else:
#         print('This word is not available')
#     check = input('if you want to exit, enter E: ')
#     if check == 'e' or check == 'E':
#         break
# n = int(input("Enter N = "))
# m = n
# ls = []
# if n == 1:
#     print('Không thể phân tích thành thừa số nguyên tố')
# else:
#     i = 2
#     while i <= m:
#         while m % i == 0:
#             ls.append(i)
#             m = m/i
#         i += 1
# dic = {}
# for v in ls:
#     if v not in dic:
#         dic[v] = 0
#     dic[v] += 1
# print(dic)
# s = ''
# for v in dic:
#     if dic[v]==1:
#         s=s+str(v)+ 'x'
#     else:
#         s=s+'{}^{} x '.format(v,dic[v])
# if len(s)>0:
#     s=s[0:len(s)-1]
# print(s)
# people=[]
# person={
#     'name':'b',
#     'age':'21',
#     'phone':['0964966850','0964628382']
# }
# people.append(person)
# print(people[0]['phone'][1])
# phone='0964966850'
# for v in range()