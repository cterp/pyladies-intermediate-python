import pytest

# Exercise 1
# Use list comprehension to create a function that multiplies
# each element in a sequence of numbers by 2
# ================================
def double(sequence):
	return [x*2 for x in sequence]

def test_double():
    assert double(range(3)) == [0,2,4]


# Exercise 2
# Use list comprehension to create a function that finds
# the odd elements in a sequence of numbers
# ================================
def odd(sequence):
	return [i for i in sequence if i % 2 != 0]

def test_odd():
	assert odd(range(6)) == [1,3,5]


# Exercise 3
# Use list comprehension to create a function that finds
# the elements divisible by 3 and 5 in a sequence of numbers
# ================================
def by_five(sequence):
	return [i for i in sequence if i % 3 == 0 and i % 5 == 0]

def test_by_five():
	assert by_five(range(1,31)) == [15, 30]


# Exercise 4
# Use list comprehension to create a function that finds
# words containing the letter 'e' in a list of words
# ================================
def e_present(words):
	return [word for word in words if 'e' in word]

def test_e_present():
	assert e_present(['dog', 'cat', 'heron', 'turtle', 'aardvark', 'pythons', 'elephant']) == ['heron', 'turtle', 'elephant']


# Exercise 5
# Use list comprehension to display the index position in front of each element
# of a list. For example, say you're given the list ["zero", "one", "two"]. 
# The output of your list comprehension would be ['0: zero', '1: one', '2: two']
# 
# Hint 1: use helper functions
# Hint 2: write a function that accepts the index position and element of each item
# in the list, and formats the element into the form 'index: element'
# Hint 3: use enumerate() in the iterator portion of the list comprehension
# ================================

def treat(index, element):
	return '%d: %s' % (index, element)

def format_pair(sequence):
	return [treat(i, e) for i, e in enumerate(sequence)]

def test_format_pair():
	assert format_pair(["zero", "one", "two"]) == ['0: zero', '1: one', '2: two']
