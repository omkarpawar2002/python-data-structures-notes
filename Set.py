# Here we see the python built-in data structure SET.

# Set is mutable in nature but it can store only immutable objects.
# Set is unordered collection of data structure.
# Set does not allow duplicate values.
# Set does not support indexing and slicing.
# Set support some mathematical operations like union , intersection , difference and symetric-difference

# ----------------------------------------------------

# To create an empty set we have only one way that is set() function :- 
# s = set()

# ----------------------------------------------------

# Methods in sets :- 

# 1.add() :- 
#       This method is used to add single element inside set.

# s = {10,20,30,40}
# print("Original set :- ",s)
# s.add(101)
# print("Updated set :- ",s)

# -------------

# 2.update() :- 
#       This method is used to add any other iterable object suct as list , tuple , set etc.,

# s = {10,20,30,40}
# print("Original set :- ",s)
# s.update((101,122))
# print("Updated set :- ",s)

# ------------

# 3.remove() :- 
#       This method is used to remove the specified element in set . If the element does not found it will show an keyError

# s = {10,20,30,40}
# print("Original set :- ",s)
# s.remove(20)
# print("Updated set :- ",s)

# ------------

# 4.discard() :- 
#       This method is used to discard the specified element in set . If the element does not found it will just ignore it.

# s = {10,20,30,40}
# print("Original set :- ",s)
# s.discard(2000)
# print("Updated set :- ",s)

# ------------

# 5.pop() :- 
#       This method is remove an any arbitrary(random) element from set.

# s = {10,20,30,40}
# print("Original set :- ",s)
# s.pop()
# print("Updated set :- ",s)

# ------------

# 6.clear() :- 
#       This method is used to remove all the element inside set.

# s = {10,20,30,40}
# print("Original set :- ",s)
# s.clear()
# print("Updated set :- ",s)

# ------------

# 7.copy() :- 
#       This method will return the shallow copy of set.

# s = {10,20,30,40}
# print("Original set :- ",s)
# res = s.copy()
# print("Updated set :- ",res)

# ------------

# 8.union() :- 
#       Union method will return all the distinct(unique) element from sets.

# s1 = {10,20,30,40,50}
# s2 = {40,50,60,70,80}
# print(s1.union(s2))
# print(s1 | s2)

# ------------

# 9.intersection() :- 
#       Intersection method will return the only common element between the sets.

# s1 = {10,20,30,40,50}
# s2 = {40,50,60,70,80}
# print(s1.intersection(s2))
# print(s1 & s2)

# ----------

# 10.Intersection_update() :- 
#       Intersection update method will compute the result between two sets and gives common element between them and update it to the calling set.

# s1 = {10,20,30,40,50}
# s2 = {40,50,60,70,80}
# s1.intersection_update(s2)
# print(s1)

# ------------

# 11.difference() :- 
#       Difference method compute the result between two sets and return the element that are present in set1 but not in set2.

# s1 = {10,20,30,40,50}
# s2 = {40,50,60,70,80}
# print(s1.difference(s2))
# print(s1 - s2)

# ------------

# 12.difference_update() :- 
#       Difference update method compute the difference between two sets and update it to the calling set.

# s1 = {10,20,30,40,50}
# s2 = {40,50,60,70,80}
# s2.difference_update(s1)
# print(s2)

# ------------

# 13.symmetric_difference() :- 
#       Symmetric difference method return the elements that are present in both set but except the intersection element.

# s1 = {10,20,30,40,50}
# s2 = {40,50,60,70,80}
# print(s1.symmetric_difference(s2))
# print(s1 ^ s2)

# ------------

# 14.Symmetric_difference_update() :- 
#       Symmetric_difference_update method compute the symmetric_difference between two set and update it to the calling set.

# s1 = {10,20,30,40,50}
# s2 = {40,50,60,70,80}
# s2.symmetric_difference_update(s1)
# print(s2)

# ------------

# 15.isdisjoitnt() :- 
#       If the both the sets don't have any common elements between them means they are disjoint otherwise they are not.

# s1 = {10,20,30,40,50}
# s2 = {60,70,80}
# print(s1.isdisjoint(s2))

# ------------

# 16.issubset() :- 
#       This method return True if all the elements of set1 is present in set2 otherwise it return False.

# s1 = {40,50}
# s2 = {40,50,60,70,80}
# print(s1.issubset(s2))

# ------------

# 17.issuperset() :- 
#       If all the elements of set2 is present in set1 then it return True otherwise False

# s1 = {10,20,30,40,50,60,70,80}
# s2 = {40,50,60,70,80}
# print(s1.issuperset(s2))

# ------------

# Set comprehension :- 
#       Set comprehension is a concise way of creating set in python.

# s = {item for item in range(1,21) if(item%2==0)}
# print(s,type(s))

# -----------------

