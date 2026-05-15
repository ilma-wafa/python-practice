multiples = []
for x in range(1, 11):
    multiples.append ( x*7)
print(multiples)

#We can do this in a simpler way using List Comprehensions

multiples= [x*7 for x in range(1, 11)]
print(multiples)