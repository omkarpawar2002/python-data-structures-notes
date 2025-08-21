# Here we see the python built-in data structure TUPLE.

# Tuple is Immutable in nature.
# Tuple is represented by paranthesis ().
# Tuple can store heterogenous data.
# Tuple can also store duplicate elements.
# Tuple also support positive or negative indexing.
# Tuple also support slicing.

# -----------------------------------------------------

# To create a Tuple there are 2 ways :- 

# First way :- 
# t = ()

# Second way :- 
# t = tuple()

# -----------------------------------------------------

# Tuple can store duplicate elements.
# t = (10,20,30,10,10)
# print(t)

# Tuple can store heterogenous data.
# t = (10,20,True,"welcome",34.54)
# print(t)

# Tuple support both positive indexing and negative indexing.

# t = (10,20,30,40,50)
# print("Positive Indexing")
# print(t[0])
# print(t[1])
# print(t[2])
# print(t[3])
# print(t[4])

# print()

# print("Negative Indexing")
# print(t[-1])
# print(t[-2])
# print(t[-3])
# print(t[-4])
# print(t[-5])

# Tuple also support Slicing :- [ Slicing menas to break down the sequences into subsequences ]
# t = (10,20,30,40,50,60,70,80,90,100)
# res = t[1:4]
# print(res)

# -----------------------------------------------------

# Note :- As we know Tuple is Immutable means once tuple is created we can not modify the content inside tuple. So python provide only 2 methods for tuple.

#1.index() :- 
#       It return the index position of specified element.

# t = (10,20,30,40,50)
# print("Original Tuple :- ",t)
# print("Index position :- ",t.index(30))

# ------

#2.count() :- 
#       It return the total count of occurances of specified element.

# t = (10,20,30,40,50,30,30,30)
# print("Original Tuple :- ",t)
# print("Index position :- ",t.count(30))