#This data structure maintains the order of insertion of keys.
from collections import OrderedDict

#Intializing OrderedDict
ordered_phonebook = OrderedDict([
    ("Alice", "123-456-7890"),
    ("Bob", "987-654-3210"),
    ("Charlie", "555-555-5555")
])
print("Initial ordered phonebook:", ordered_phonebook)

#removing an item
removed_item = ordered_phonebook.popitem(last=False) #removes the first inserted item
print("Removed item:", removed_item)
print("Phonebook after removal:", ordered_phonebook)

removed_item = ordered_phonebook.popitem(last=True) #removes the last inserted item
# last = false removes the first item
# last = true removes the last item