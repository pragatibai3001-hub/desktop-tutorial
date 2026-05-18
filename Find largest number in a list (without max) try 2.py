#Find largest number in a list (without max)

my_list = [10,20,30,40,50,10.5]

largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i
print (largest)
    
