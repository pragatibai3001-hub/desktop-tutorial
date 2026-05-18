#Find longest word in a sentence

sentence = 'I will become a python programmer'

words = sentence.split()

print(words)

longest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

print (longest)
