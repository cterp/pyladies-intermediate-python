from StringIO import StringIO
import pytest
import sys
import time

# Note: to run this file, use the "normal" way of running Python scripts from
# the command line. For example:
# $ python decorator_solutions.py


# Exercise 1
# Step 1: write a function called "print_message" 
# that prints the word "Hello!"
#
# Step 2: Write a decorator called "noisy" that prints
# the word "before" before the wrapped function is
# invoked, prints "Hello!" when the function is 
# invoked, and "after" after the function is
# invoked. If you like, also print the function's name 
# during the calls by using the __name__ attribute.
#
# Step 3: invoke your decorator by calling print_message()
#
# Output will look like the following 3 lines:
# before print_message
# Hello!
# after print_message
# ================================

print "Exercise 1 output:"

def noisy(func):
    def inner_function():
        print "before", func.__name__
        result = func()
        print "after", func.__name__
        return result
    return inner_function

@noisy
def print_message():
    print "Hello!"

print_message()

print "--------------------------"  # separate exercise output


# Exercise 2
# 
# Rewrite your "noisy" decorator so that it 
# accepts variable and variable keyword arguments.
# ================================

print "Exercise 2 output:"

def noisy(func):
    def inner_function(*args, **kwargs):
        print "before", func.__name__
        result = func(*args, **kwargs)
        print "after", func.__name__
        return result
    return inner_function

@noisy
def print_message():
    print "Hello there!"

print_message()

print "--------------------------"  # separate exercise output


# Exercise 3
# 
# Write a decorator that returns the product of two numbers.
# Step 1: write a function that returns the product of two numbers.
# Hint/step 2: can you re-use the decorator you wrote for Exercise 2?
# ================================
print "Exercise 3 output:"

@noisy
def mult(x,y):
	return x * y

print mult(3,6)

print "--------------------------"  # separate exercise output

# Exercise 4
# 
# Write a decorator that outputs the time a function takes to execute.
# Step 1: Write a function that does anything you like. Suggestion: append
# some numbers to a list.
# Step 2: Write a decorator that times how long it takes the function from
# step 1 to run. Hint: time.time(); the time module has already been 
# imported.
# ================================
print "Exercise 4 output:"

def timing_function(decorated_function):
    def decorating_function():
        start = time.time()
        decorated_function()
        end = time.time()
        return ("Time it took to run the function: %0.5f seconds" % (end - start))
    return decorating_function


@timing_function
def append_nums_to_list():
    num_list = []
    for num in range(0, 10000):
        num_list.append(num)
    print("Sum of all the numbers in the list: %d" % sum(num_list))

print append_nums_to_list()

print "--------------------------"


# Exercise 5
# Use a decorator to simulate rate-limiting. That is, have the decorator
# wait before invoking the wrapped function.
#
# Step 1: write a function that accepts a number and returns double the number.
# Step 2: write a decorator that accepts arguments and waits one second before
# calling the function from step 1. 
# Hint: time.sleep() will be useful.
# ================================
def rate_limit(decorated_function):
    def decorating_function(*args, **kwargs):
        time.sleep(1)
        result = decorated_function(*args, **kwargs)
        return result 
        # Note: the two preceding lines can be combined into one: 
        # return decorated_function(*args, **kwargs)
    return decorating_function


@rate_limit
def print_number(num):
    return num * 2

# invoke 
for num in range(1, 10):
    print print_number(num)


print "--------------------------"

# The code below is completely optional and shown only for funsies.
# To run: $ py.test decorator_solutions.py
# It's basically the same as exercise 2, except it also shows how to 
# capture output written to stdout and how to assert equality on that 
# output.
def test_decorator():

	def noisy(func):
	    def inner_function(*args, **kwargs):
	    	sys.stdout.write("before\n")
	        result = func(*args, **kwargs)
	        sys.stdout.write("after")
	        return result
	    return inner_function

	@noisy
	def middle():
	    sys.stdout.write("middle\n")

	# IO magic to capture output
	environment = sys.stdout
	sys.stdout = StringIO()
	middle()
	out = sys.stdout.getvalue()
	sys.stdout.close()
	sys.stdout = environment

	assert out == 'before\nmiddle\nafter'  # pretty cool, eh?
