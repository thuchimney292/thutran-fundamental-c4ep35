def get_even_list(l):
    for i in range(len(l)-1,-1,-1):
        if l[i] % 2 == 1:
            del l[i]
    return l
print(get_even_list([4,7,-2,9,7,0]))