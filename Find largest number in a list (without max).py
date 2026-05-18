#Find largest number in a list (without max)


my_list = [100,20,40,255,70]

largest = my_list[0]

for i in my_list:
    if largest < i:
        largest = i
print (largest)
        
    
