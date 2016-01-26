import pytest
import types

# Replace each "pass" statement with your code.


# GENERATORS

# Exercise 1
# Implement a generator that yields 1 then 2.
# ================================
def one_then_two():
	pass

# Exercise 2
# Implement a generator that yields numbers one at a 
# time. The largest number should be given by the user,
# otherwise it should return up to 10 by default.
# ================================
def gen_sequence(n=10):
	pass

# Exercise 3
# Write a generator that outputs the cube of the numbers
# 1-5, inclusive.
# ================================
def find_cubes(n=5):
	pass


# GENERATOR EXPRESSIONS

# Exercise 4
# Create a generator expression that generates the
# numbers from 1 up to and including 5
# ================================
def to_five():
	pass


# Exercise 5
# Write a generator expression that generates the squares 
# of the integers from 1 up to and including 10
# ================================
def squares_to_ten():
	pass


# Exercise 6 
# Use a generator expression to compute the sum of the digits 1-100.
# Hint: write a generator expression and use it with sum().
# ================================
def gen_sum():
	pass


# Exercise 7
# Use a generator expression to create a dictionary where the 
# keys are the numbers 0-5 and each key's value is the square of 
# the key.
# Sample output: {1: 1, 3: 9, ...}
# Hint: wrap your expression with dict()
# ================================
def dict_gen():
	pass


# Exercise 8
# Find the sum of the squared integers from 1 to 1000000.
# Hint: first write a generator expression to compute the squares,
# and then find the sum.
# ================================
def sum_squares():
	pass


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
