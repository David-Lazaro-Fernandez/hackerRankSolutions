
magazine = ['David', 'Jack', 'Rose']
letter = ['David', 'Tom', 'Jack']
flag= True
d = {}
for i in magazine:
    d.setdefault(i,0)
    d[i] += 1
for i in letter:
    if i in d:  
        d[i] -= 1
    else:
        flag = False    

if(flag == True and all([x>=0 for x in d.values()])):
    print('Yes')
else:
    print('No')        
    