
arr = [0] * 11
queries = [[2, 6, 8],[5, 9, 15],[1, 8, 1],[3, 5, 7]]
current = 0 
maximum = -1
for i in range(len(queries)):
  arr[queries[i][0]] += queries[i][2]
  arr[queries[i][1]+1] += -queries[i][2]
  print(arr)

print(arr)
for i in arr:
  current += i
  if(current > maximum):
    maximum = current
    
print(maximum)    