n = 0
n1 = 1 
print(n)

for _ in range(2, 25):
    new_num = n + n1
    print(new_num)
    
    n = n1
    n1 = new_num