from re import T


triplet = {}
comb = {}
arr = [1 ,1 ,1 ,1, 1]
ratio = 1
counter = 0
for i in range(len(arr)-2):
    primer = {index:e for index,e in enumerate(arr) if((e==arr[i]*ratio) and index>i)}
    segundo = [index for index, e in enumerate (arr) if(e==arr[i]*ratio*ratio and index > i)]
    
    for key in list(primer.keys()):
        comb[key] = segundo
    triplet[i] = comb
    comb = {}    

for i in range(len(triplet)):
    for j in triplet[i]:
        print(j)

    
   
    
    