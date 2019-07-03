def remove_dollar_sign(s):
    ls=list(s)
    for i in range(len(ls)-1,-1,-1):
        if ls[i]=="$":
            del ls[i]
    s_new=''
    for i in range(len(ls)):
        s_new+=ls[i]
    return s_new
s=input('Enter your string you want to remove $ sign : ')
print(remove_dollar_sign(s))