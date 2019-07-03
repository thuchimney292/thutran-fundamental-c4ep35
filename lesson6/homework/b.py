def remove_(s):
    ls=list(s)
    i=0
    while True:
        if ls[i]==' ':
            del ls[i]
        else: break
    s_new=''
    for i in range(len(ls)):
        s_new+=ls[i]
    return s_new
print(remove_('   fndnjr'))