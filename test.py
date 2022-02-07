string = "HELLOWORLD"
s = string
aux = ""
finished = False
i = 0
arr = []
s = [char for char in s]
for i in s:
    try:
        arr.index(i)
    except:
        arr.append(i)
print(arr)              