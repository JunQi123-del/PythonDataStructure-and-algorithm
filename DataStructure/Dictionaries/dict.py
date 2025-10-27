#Intializing dictionary 

phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

print("Initial phonebook:", phonebook)
print("Nnumber of keys in phonebook:", len(phonebook))
print("get all the keys in hte phonebook:", phonebook.keys())
print("Get all the values in the phonebook:", phonebook.values())

#getting a value from the key:
print("Alice's number is:", phonebook.get("Alice"))
#or 
print("Bob's number is:", phonebook["Bob"]) #raises KeyError if key not found

#gettinng all the items in dictionary
for name,number in phonebook.items():
    print(f"call {name} at {number}")

#Dict comprehensions
ranks = [("Alice", "Captain"), ("Bob", "Lieutenant"), ("Charlie", "Recruit")]
rank_dict = {name: rank for name, rank in ranks} #Creating dictionary from list of tuples 
print("Rank dictionary:", rank_dict)

#Storing dictionary key in a list
keys_list = list(phonebook.keys())
print("List of keys in phonebook:", keys_list)

#python dict keys must be hashable 
# Immutabble: cannot change during its liftetime
# Examples of hashable types: str, int, float, tuple
# if you want to build a object that is hashable, you need to implement __hash__() and __eq__() methods
