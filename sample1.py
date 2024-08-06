lists = []
a = 1
b = 11
d = 0

for i in range(10):
    lists.append(a)
    
    c = a * b 
    
    lists.append(c)
    
    a = c * b
    
print(lists)
   