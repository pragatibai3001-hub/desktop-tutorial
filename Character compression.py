#Character compression aaabbccccd

def func(string):
    count_dict = {}
    
    for i in string:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    new_string = ''
    for key in count_dict:
        new_string += key + str(count_dict[key])
    return new_string
print (func('aaabbccccd'))
