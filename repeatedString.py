n = 10
string = 'aba'
stringInN = n // len(string)
string = [char for char in string]
l = list(filter(lambda x:x=='a', string))
originalAs = len(l)
module = string[0:n%len(string)]
restofAs = len(list(filter(lambda x:x=='a', module)))

print(originalAs*stringInN+restofAs)
