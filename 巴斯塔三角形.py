
lists = []
a = 1
b = 11
c = 0

user = int(input("階層數"))
for i in range(user):
    lists.append(a)
     
    c = a * b 
    
    lists.append(c)   
    
    a = c * b
    
print(lists)
   
