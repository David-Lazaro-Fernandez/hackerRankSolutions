

c = [0, 0, 1, 0, 0, 1, 0]
index = 0
jump = 0  
while(index <= len(c)-2):
    if(index == len(c)-2):
        safe = index+1
        index = safe
        jump += 1  
    else:    
        if(c[index+2] == 0):
            safe = index+2
        elif(c[index+1] == 0):
            safe = index+1
        jump += 1  
        index = safe   

                