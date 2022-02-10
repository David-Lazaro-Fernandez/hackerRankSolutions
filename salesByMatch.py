def sockMerchant(n, ar):
    # Write your code here
    count = 0
    while(len(ar) != 0):
        er = False
        rep = len(list(filter(lambda x: x==ar[0], ar)))
        count += rep // 2
        num = ar[0]
        while(er != True):
            try:
                ar.remove(num)
            except:
                er = True  
    return count     