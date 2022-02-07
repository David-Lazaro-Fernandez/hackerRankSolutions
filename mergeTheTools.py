from os import sep


s = 'BCYKGOAWSHXBDZTPUELEFXINZEIISJYVNWFTNHQHPPJSREKNJXRQUZDVDOFVZDRMBYHOGZYXRHRILBVWYMPUOURRIWPJBIVFGFVOGTLXADHOGCMHRBDFWVYGTPQVXNCGUXUBRGYTLGJRKWADZEIVZJEUAURAJTGERCFIKFDVLNPWJPZITKGUVKPVGGXPADVTGCBQIGOTTDREUTPQFVKCFBZNKXEMAAFICIBMOPGKUZOQUDGZYTDFUDUGAZUCBZNFJQSAFAKBBYRWEYXETBMPEGWGHQKISZOBPIDWINXJORHSRFWKGIZMRXSYOEHIEXLTHPQPCPASGIMXPJJVTJHMGBLWHUELTQHAHZRJOTEXDQWSBG'
k = 6
n = len(s)
division = n//k
counter = 1
aux = []
arr= []
s = [char for char in s]
separatedStrings = []
for i in range(n):
  if(counter == k):
    aux.append(s[i])
    separatedStrings.append(aux)
    aux = []
    counter = 1
  else:
    aux.append(s[i])
    counter+=1
    
for i in separatedStrings:
    for j in i:
        try:
            arr.index(j)
        except:
            arr.append(j)
    arr = "".join(arr)
    print(arr)
    arr = []
  
        
