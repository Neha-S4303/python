#  Merge dictionaries.
# Merge two dictionaries.

# using | operator
dict_1 = {'Nmae': 'Abby', 'Age': 20, 'Height': 5.5}
fav_dict = {'Color': 'Purple', 'Number': 11, 'Fruit': 'Mango'}
merge_dict = dict_1 | fav_dict
print(merge_dict)

# using update (updates first dictionary)
dict_1 = {'Nmae': 'Abby', 'Age': 20, 'Height': 5.5}
fav_dict = {'Color': 'Purple', 'Number': 11, 'Fruit': 'Mango'}
dict_1.update(fav_dict)
print(dict_1)

# using upacking dict
dict_1 = {'Nmae': 'Abby', 'Age': 20, 'Height': 5.5}
fav_dict = {'Color': 'Purple', 'Number': 11, 'Fruit': 'Mango'}
merge_dict = {**dict_1, **fav_dict}
print(merge_dict)
