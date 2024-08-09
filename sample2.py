
a = 1
b = 2
c = 0

lists = []

for i in range(10):
    lists.append(c)
    lists.append(a)
    lists.append(b)
    c = a + b
    a = b + c
    b = c + a
    
print(lists)