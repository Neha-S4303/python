# Create a List: Start by creating a list with 5 elements.
# These could be fruits, numbers, or a mix of data types.

my_list = ['apple', 'banana', 'orange', 'mango']
print(my_list)

# Access Elements: Use both positive and negative indices to retrieve items from the list.

print(my_list[1])  # positive index
print(my_list[-1])  # negative index

# Modify the List: Learn how to append, insert, remove, or update elements using built-in methods.

my_list.append('kiwi')  # adding element
print(my_list)

my_list.insert(1, 'papaya')  # inserting element
print(my_list)

my_list.remove("mango")  # removing element
print(my_list)

my_list[0] = 'grapes'  # updating element
print(my_list)

# Slice the List: Use slicing to create sublists by selecting a specific range of elements.

print(my_list[1:4])  # slicing

# Iterate Through the List: Use loops (like for or while) to go through each item and perform operations on them.

for i in my_list:  # basic iteration
    print(i)

for i in range(len(my_list)):  # iteartion with index
    print(i, my_list[i])

for i, value in enumerate(my_list):  # iteration with index and value
    print(i, value)

# Create a Tuple: Define a tuple containing different types of data, such as strings, numbers, or booleans.

my_tuple = ('apple', 'banana', 'ornage', 'mango')
print(my_tuple)

# Access Elements: Retrieve elements using index positions, just like you would with a list.

print(my_tuple[0])  # first element
print(my_tuple[-1])  # last element

# Tuple Operations: Perform operations like concatenation (+) and repetition (*), or check membership with in.

fruit_tuple = ('cherry', 'strawberry')
new_tuple = my_tuple + fruit_tuple  # concatenation
print(new_tuple)

print(fruit_tuple * 3)  # repetition

print('banana' in my_tuple)  # check membership

# Convert to a List: If you need to modify the tuple, convert it into a list, make the changes, and convert it back if needed.

lst = list(my_tuple)  # convert to list
lst.append('kiwi')  # make changes
t = tuple(lst)  # convert back to tuple
print(t)
