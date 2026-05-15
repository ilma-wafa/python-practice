fruits = ["Papaya", "Cherry", "Banana", "Apple"]
fruits.append("Kiwi") #add an item
print(fruits)

fruits.insert(0, "Orange") #add an item to a certain place
print(fruits)

fruits.insert(0, "Orange") 
fruits.insert(25, "Peach") #add an item to a certain place
print(fruits)

fruits.insert(0, "Orange") 
fruits.insert(25, "Peach") #add an item to a certain place
fruits.remove("Papaya") #Remove an item
fruits.pop(3) #Remove an item using index
fruits[2] = "Melon" #Add an item using index
print(fruits)