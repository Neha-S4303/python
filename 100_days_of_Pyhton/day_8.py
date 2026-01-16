# Create a Set: Define a set with multiple elements, including duplicates,
# and observe how duplicates are automatically removed.

my_set = {1, 0, 87, 34, 2, 1, 2, 34, 57, 67}
print(my_set)

# Add and Remove Items: Use add() to insert elements and remove() or discard() to delete them.

my_set.add(13)
print(my_set)

my_set.remove(57)
print(my_set)

my_set.discard(2)
print(my_set)

# Set Operations: Learn how to perform mathematical set operations like
#  union(),


set2 = {13, 45, 68, 79, 80, 12, 2, 4, }
uset = my_set.union(set2)
print(uset)

# intersection(),

set2 = {13, 45, 68, 79, 80, 12, 2, 4, }
iset = my_set.intersection(set2)
print(iset)


# and difference().

set2 = {13, 45, 68, 79, 80, 12, 2, 4, }
dset = my_set.difference(set2)
print(dset)

# Loop Through a Set: Use a loop to iterate over the elements in a set.

for i in my_set:
    if i > 10:
        print(i)

# Create a Dictionary: Define a dictionary with keys and corresponding values (e.g., name-age pairs).

my_dict = {'Name': 'Abby', 'Age': 20, 'Height': 5}
print(my_dict)


# Access Values: Use a key to retrieve the associated value using square brackets
# or the get() method.

print(my_dict['Name'])

wt = my_dict.get('Weight', None)
print(wt)


# Update and Add Items: Modify existing key-value pairs or add new ones.

my_dict['City'] = 'Boston'  # add key-value pair
print(my_dict)

my_dict['Age'] = 22  # update value of existing key
print(my_dict)

# Remove Items: Use methods like pop() or del to remove entries from the dictionary.

my_dict.pop('Age')
print(my_dict)

del my_dict['City']
print(my_dict)

# Loop Through a Dictionary: Iterate through keys, values,
#  or both using a for loop with .items(), .keys(), or .values().


for key in my_dict:  # loop through key (default)
    print(key)

for value in my_dict.values():  # loop through values
    print(value)

for key, value in my_dict.items():
    print(key, value)  # loop through key-value pair
