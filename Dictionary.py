# Here we see the python built in data structure DICTIONARY.

# Dictionary is mutable in nature.
# Dictionary is represented by curly brackets {}.l
# In Dictionary data will be store in key - value pair form.
# In Dictionary each key will be unique and value can be duplicate.
# After python 3.6 Dictionary will become ordered data structure before 3.6 it's unordered.
# In Dictionary indexing and slicing is not possible , through keys we can access values inside Dictionary.

# --------------------------------

# To create a Dictionary in python there are 2 ways :- 

# First Way :- 
# d = {}

# Second way :- 
# d = dict()

# ----------------------------------

# How to access values inside Dictionary.

# d = {1:10,2:20,3:30,4:40}
# print(d[1])
# print(d[2])
# print(d[3])
# print(d[4])

# ----------------------------------

# Here we see how do we create dictionary 

# d = {
#     1:'Welcome',
#     2:'to',
#     3:'jumanji',
#     4:'world'
# }
# print(d)

# # Here we see how to access single item from dictionary
# print(d[3])

# # Here we see how to modify dictionary keys value 
# d[2] = "my new"
# print(d)

# # Here we see how to delete dictionary key,value pairs
# del d[2]
# print(d)


# ----------------------------------

# Note :- So as we know dictionary is mutable so python provided some built in methods to work with dictionary so we can manipulate [ update , delete ] dictionary . 

#1.get() :- 
#       This get() method basically return the value of specified key if key is present in dictionary otherwise it return None.

# d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
# print(d.get(2))
# print(d[2])

# Note :- 
#       Best recommanded way to used get() method instead of [] subscript operator to access any key's value.

# ------------------

# 2.update() :- 
#       Update() method is used to add multiple key-value pairs or other iterable object of dictionary.

# d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
# print(d)
# d.update({5:'home',6:'tour'})
# print(d)

# ----------------------

# 3.keys() :- 
#       This keys() method will return the list of all keys in dictionary.

# d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
# print(d)
# dict_keys = d.keys()
# for i in dict_keys:
#     print(i)

# -----------------

# 4.values() :- 
#       This values() method will return the list of all the values in dictionary.

# d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
# print(d)
# dict_values = d.values()
# for value in dict_values:
#     print(value)

# -----------------

# 5.items() :- 
#       Items will return the list of all the key , value pair in tuple from dictionary in list format.

# d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
# dict_items = d.items()
# print(dict_items)
# for key , value in d.items():
#     print(f"Here is a {key} and here is value :- {value.upper()}")

# ------------------------

# 6.clear() :- 
#       If we want to remove entire list key - value pair then we used this clear() method.

# d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
# print(d)
# d.clear()
# print(d)

# ------------------------

# 7.popitem() :- 
#       popitem() will remove and return the last inserted key - value pairs.

# d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
# print(d)
# print(d.popitem())
# print(d)

# -------------------------

# 8.pop() :- 
#       pop() method will remove and return the specified key value pair from dictionary.

# d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
# print(d)
# d.pop(2)
# print(d)

# --------------------------

# 9.copy() :- 
#       copy() method will return the shallow copy of dictionary

# d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
# print(d)
# res = d.copy()
# print(d,id(d))
# print(res,id(res))

# --------------------------

# 10.setdefault() :- 
#       If the specified key is not present in dictionary then setdefault will be added new key and value or if the key is present in dictionary then it will just ignore the content .

# d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
# print(d)
# d.setdefault(4,"newone")
# print(d)

# -------------------------

# 11.fromkeys() :- 
#       fromkeys() will create a dictionary from given sequence of keys and values.

# keys = (1,2,3,4)
# values = "welcome"
# d = dict.fromkeys(keys,values)
# print(d)

