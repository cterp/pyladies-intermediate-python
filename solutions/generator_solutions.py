import pytest
import types

# Note: either xrange() or range() will work for the problems below. I 
# used xrange() to stick with the theme of lazy evaluation (and because
# I am using Python 2.7). In Python 3, range() is a generator.

# In 2.7:
# xrange() isn't a generator but behaves like one in that it lazily 
# generates a sequence. You can index it directly (but not slice), it
# has no next() method, and it doesn't exhaust the sequence when you 
# iterate over it. range() stores the whole sequence in memory. 
# But in the context of a generator, even  using range() won't create
# the whole sequence. 


# GENERATORS

# Exercise 1
# Implement a generator that yields 1 then 2.
# ================================
def one_then_two():
	for i in xrange(1,3):
		yield i

# Exercise 2
# Implement a generator that yields numbers one at a 
# time. The largest number should be given by the user,
# otherwise it should return up to 10 by default.
# ================================
def gen_sequence(n=10):
	for i in xrange(1, n + 1):
		yield i

# Exercise 3
# Write a generator that outputs the cube of the numbers
# 1-5, inclusive.
# ================================
def find_cubes(n=5):
	for i in xrange(1, n + 1):
		yield i ** 3


# GENERATOR EXPRESSIONS

# Exercise 4
# Create a generator expression that generates the
# numbers from 1 up to and including 5
# ================================
def to_five():
	return (x for x in xrange(1,6))


# Exercise 5
# Write a generator expression that generates the squares 
# of the integers from 1 up to and including 10
# ================================
def squares_to_ten():
	return (x ** 2 for x in xrange(1,11))


# Exercise 6 
# Use a generator expression to compute the sum of the digits 1-100.
# Hint: write a generator expression and use it with sum().
# ================================
def gen_sum():
	return sum(x for x in xrange(101))


# Exercise 7
# Use a generator expression to create a dictionary where the 
# keys are the numbers 0-5 and each key's value is the square of 
# the key.
# Sample output: {1: 1, 3: 9, ...}
# Hint: wrap your expression with dict()
# ================================
def dict_gen():
	return dict((i,i ** 2) for i in xrange(6))


# Exercise 8
# Find the sum of the squared integers from 1 to 1000000.
# Hint: first write a generator expression to compute the squares,
# and then find the sum.
# ================================
def sum_squares():
	square = (i*i for i in xrange(1000000))
	
	total = 0
	for i in square:
		total += i
	
	return total


# ================================
# Tests!

def test_gen():
	# Exercise 1 tests
	first_gen = one_then_two()
	assert isinstance(first_gen, types.GeneratorType)
	assert next(first_gen) == 1
	assert next(first_gen) == 2
	assert pytest.raises(StopIteration, next, first_gen)

	# Exercise 2 tests
	second_gen = gen_sequence()
	assert isinstance(first_gen, types.GeneratorType)
	assert list(second_gen) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	assert pytest.raises(StopIteration, next, second_gen)

	second_gen = gen_sequence(15)
	assert isinstance(first_gen, types.GeneratorType)
	assert list(second_gen) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
	assert pytest.raises(StopIteration, next, second_gen)

	# Exercise 3 tests
	cubes = find_cubes()
	assert isinstance(cubes, types.GeneratorType)
	assert list(cubes) == [1, 8, 27, 64, 125]
	assert pytest.raises(StopIteration, next, cubes)


def test_gen_expressions():
	# Exercise 4 tests
	ge_to_five = to_five()
	assert isinstance(ge_to_five, types.GeneratorType)
	assert next(ge_to_five) == 1
	assert next(ge_to_five) == 2
	assert next(ge_to_five) == 3
	assert next(ge_to_five) == 4
	assert next(ge_to_five) == 5
	assert pytest.raises(StopIteration, next, ge_to_five)

	# Exercise 5 tests
	ge_squares_to_ten = squares_to_ten()
	assert isinstance(ge_squares_to_ten, types.GeneratorType)
	assert list(ge_squares_to_ten) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

	# Exercise 6 tests
	ge_gen_sum = gen_sum()
	assert isinstance(ge_gen_sum, types.IntType)
	assert ge_gen_sum == 5050

	# Exercise 7 tests
	ge_dict_gen = dict_gen()
	assert isinstance(ge_dict_gen, types.DictType)
	assert ge_dict_gen == {5: 25, 0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

	# Exercise 8 tests
	ge_sum_squares = sum_squares()
	assert isinstance(ge_sum_squares, types.IntType)
	assert ge_sum_squares == 333332833333500000
