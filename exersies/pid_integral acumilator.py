total = 0 

def add_to_total(x):
    global total
    total += x
    return total

for x in range(100):  
    add_to_total(5)
    print(total)  
