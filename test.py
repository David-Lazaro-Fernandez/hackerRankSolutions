# arr = [0] * 10
# arr[:5] += [110] * len(arr[:5])
# print(arr)
# arr[:5] += ([110] * len(arr[:5]))
# print(arr)


l1 = [1,2,3,10,49,2]
l1[0:3] = [sum(x) for x in zip(l1[0:3],[100]*3)] 
# l3 = [1] * len(l1)
# l2 = [sum(x) for x in zip(l1[:3],l3)]
print(l1)