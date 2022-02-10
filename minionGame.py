string = "BAANANAS"
stuart = 0
kevin = 0
vowels = ['A', 'E', 'I', 'O', 'U']
vow = []
cons = []
word = ""
words = []
wordsArray = []
string = [char for char in string]
for letter in string:
    try:
        vowels.index(letter)
        try:
            vow.index(letter)
        except:
            vow.append(letter)    
    except:
        try:
            cons.index(letter)
        except:
            cons.append(letter)
for letter in  cons:
    index = string.index(letter)
    for i in range(index,len(string)):
        word += string[i]
        words.append(word)
    wordsArray.append(words)
    word = ""    
    words = []    

string = "".join(string)
for i in wordsArray:
    for word in i: 
        stuart += len(string.split(word))-1

print(wordsArray)
string = [char for char in string]
wordsArray = []
word=""
for letter in  vow:
    index = string.index(letter)
    for i in range(index,len(string)):
        word += string[i]
        words.append(word)
    wordsArray.append(words)
    word = ""    
    words = []    

string = "".join(string)
for i in wordsArray:
    for word in i: 
        kevin += len(string.split(word))-1
print(wordsArray)            

print("Stuart", stuart)
print("Kevin", kevin)    
    
          
    