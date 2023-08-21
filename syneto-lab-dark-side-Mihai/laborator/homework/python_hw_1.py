def fibonacci(n): 
    if n <= 0: #if something else than a number below 1 is selected, there's no fibonacci sequence
        print("No sequence generated")
    else:
        l=[]
        for i in range(n): #the first 2 numbers are 1
            if i == 0:
                l.append(1)
            elif i == 1:
                l.append(1)
            else:
                l.append(l[i-1]+l[i-2]) 
        return l
        
print(fibonacci(10))
print(fibonacci(0))
print(fibonacci(50))
    
    