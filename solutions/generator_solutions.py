import pytest
import types

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

def test_gen_expressions():

	# Exercise 4
	# Create a generator expression that generates the
	# numbers from 1 up to and including 5
	# ================================
	to_five = (x for x in xrange(1,6))
	assert isinstance(to_five, types.GeneratorType)
	assert next(to_five) == 1
	assert next(to_five) == 2
	assert next(to_five) == 3
	assert next(to_five) == 4
	assert next(to_five) == 5
	assert pytest.raises(StopIteration, next, to_five)


	# Exercise 5
	# Write a generator expression that generates the squares 
	# of the numbers from 1 up to and including 10
	# ================================
	squares_to_ten = (x ** 2 for x in xrange(1,11))
	assert isinstance(squares_to_ten, types.GeneratorType)
	assert list(squares_to_ten) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


	# Exercise 6
	# Use a generator expression to compute the sum of the digits 1-100.
	# Hint: write a generator expression and use it with sum().
	# ================================
	gen_sum = sum(x for x in xrange(101))
	assert isinstance(gen_sum, types.IntType)
	assert gen_sum == 5050


	# Exercise 7
	# Use a generator expression to create a dictionary where the 
	# keys are the numbers 0-5 and each key's value is the square of 
	# the key.
	# Sample output: {1: 1, 3: 9, ...}
	# Hint: wrap your expression with dict()
	# ================================
	dict_gen = dict((i,i ** 2) for i in xrange(6))
	assert isinstance(dict_gen, types.DictType)
	assert dict_gen == {5: 25, 0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


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



