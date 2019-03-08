###....LISTS and TUPLES store one or more objects or values in a specific order,
###......the difference being that 'lists' are mutable, however tuples are immutable,
###......meaning once tuples are created, objects can't be added or removed, and the order cannot be changed.

###....Creating a list or tuple is easy, here are some empty ones:
emptylst = []
emptytup = ()

###....To create non-empty lists or tuples, values are separated by commas:
lst = [1, 2, 3]
print(lst)
print('\n')	
###....tuple value(s) can be surrounded by parenthesies, or Not (see below)
tup1a = (4, 5, 6)
print(tup1a)
tup1b = ('four', 'five', 'six')
print(tup1b)
print('\n')
###....tuple value(s) with No parenthesies (Or Not)
tup2a = 7, 8, 9
print(tup2a)
tup2b = 'seven', 'eight', 'nine'
print(tup2b)
print('\n')	
###....To create a tuple with only one value, add a trailing comma to the value
tup_sgl = 0,
print(tup_sgl)
print('\n')	
###....values in lists and tuples, as with other sequence types, are referenced by an index
print(lst[1])
print(tup1a[2])
print('\n')	
###....Using an index below zero gets the values starting from the end of the list or tuple:
print(lst[-1])
print(tup1a[-2])
print('\n')	
###....Multiple values can be referenced by "slicing" the list or tuple (referencing a range[start:stop]):
print(lst[0:2])
print(tup1b[1:3])
print('\n')	
###....# Note an out-of-range stopindex translates to the end
print(tup2b[1:5])
print('\n')
###....Values for lists can be assigned using indexes (as long as the index already exists), but not for tuples:
lst[2] = 'three'  #...re-assign/change value in list (change int 3 to a char 'three')
print(lst)
print('\n')	
###....Can't change value in a tuplee using indexes:
####tup1a[2] = 'six'  #...If you try, you get error msg: TypeError: 'tuple' object does not support item assignment
###....Values can also be added to lists (and lists can be combined, or concatenated) with the '+' operator,
print(lst)
lst += [None]
print(lst)
###...... or with the standard append method:
lst.append(5)
print(lst)
print('\n')
###....A single value can be removed from lists with the del keyword: example...remove 'None' from lst array
del lst[3]
print(lst)
print('\n')
###....Or a group of values using slicing deletion: example...no stop index means start with given offset and delete to the end
del lst[2:]  #...Remove all entries starting at offset 2
print(lst)
print('\n')

###....The assignment and deletion methods used for lists(above) don't work for tuples, but concatenation works:
###....# Note: only tuples can be added to tuples
tup1b += (7,)  #...don't forget, a ',' always follows a single value being added
tup2b += 10,  #...don't forget, a ',' always follows a single value being added
print(tup1b)
print(tup2b)
print('\n')

###....Even though tuples are not mutable like lists, with the slicing technique and a little creativity,
###..... tuples can be manipulated like lists:
print('\n' + '\n' + '\n')
print(tup1a)
tup1a = tup1a[0:2]  #... Almost like the 'slice deletion' we did with lists (removes last entry from tuple 'tup1a')
print('\n', '\n')
print(tup_sgl)
tup_sgl += tup1b  #...adding values(another tuple) to a defined tuple(remember, tuples are supposed to be immutable)
print(tup_sgl)
print('\n' + '\n' + '\n')
print(tup1b)
print(tup2b)
print('\n')

tup1b = tup1b[0:1] + (1,) + tup2b[2:]  #... almost like index assignment
print(tup1b)
print('\n')
###....In addition, if a tuple contains a list, the mutability of the list in that tuple is preserved:
tup3 = 0, 'one', None, []  #....offset 3 is a placeholder for adding another value to our tuple
print(tup3)
tup3[3].append('three') #...adding 'three' into our empty placeholder
print(tup3)


###....Remember, lists and tuples can be nested (can contain lists and tuples,
###..... and other data types that store sets of values, such as dictionaries)