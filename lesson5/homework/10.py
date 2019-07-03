def get_even_list(l):
    for i in range(len(l)-1,-1,-1):
        if l[i] % 2 == 1:
            del l[i]
    return l
even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
   print("Your function is correct")
else:
   print("Ooops, bugs detected")

