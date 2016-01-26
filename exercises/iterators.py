import pytest

# Replace each "pass" statement with your code.


# Exercise 1
# Create an iterator and output its values one at a time.
# Step 1: create a list with [0,1,2,3,4,5] in it. 
# Step 2: get an iterator for a_list by using the function iter()
# Step 3: return the iterator
# ================================

def iterator_1():
	pass

def test_iterator_1():
	my_iter = iterator_1()
	assert my_iter.next() == 0  # this and the next line are equivalent
	assert next(my_iter) == 1
	assert next(my_iter) == 2
	assert next(my_iter) == 3
	assert next(my_iter) == 4
	assert next(my_iter) == 5
	assert pytest.raises(StopIteration, next, my_iter)


# Exercise 2
# Write a function that uses an iterator to take the first two (leftmost) 
# items off the list [10,9,8,7].
# ================================

def iterator_2():
	pass

def test_iterator_2():
	my_iter = iterator_2()
	assert next(my_iter) == 8
	assert next(my_iter) == 7
	assert pytest.raises(StopIteration, next, my_iter)


# Exercise 3
# Write a function that takes the list [0,1,2,3,4] and iterates it 
# from the reverse direction.
# Hint: look up the built-in function reversed()
# ================================

def iterator_3():
	pass

def test_iterator_3():
	my_iter = iterator_3()
	assert next(my_iter) == 4 
	assert next(my_iter) == 3 
	assert next(my_iter) == 2 
	assert next(my_iter) == 1
	assert next(my_iter) == 0
	assert pytest.raises(StopIteration, next, my_iter)


# Exercise 4
# Write a function that merges together two iterables to form
# a list of tuples. The first items from each iterable form a single
# tuple as the first value, all second items become part of the second
# tuple, etc.
# Sample output: [(0,0), (1,1), (2,2), ...] 
# Hint: use zip()
# ================================

def iterator_4():
	pass

def test_iterator_4():
	my_iter = list(iterator_4())
	assert my_iter == [(0,0), (1,1), (2,2)]
