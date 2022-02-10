path = "DDUUDDUDUUUD"
valley =  0
seaLvl = 0
for i in path:
    if(i == 'U'):
        if(seaLvl == -1):
            valley += 1
        seaLvl += 1
    else:
        seaLvl -= 1
        
print(valley)