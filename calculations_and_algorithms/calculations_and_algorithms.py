#!/bin/python3

from random import randrange
import numpy as np

# --- QUADRATIC EQUATION --- #

def calculate_quadratic(a, b, c):
	delta = b**2 - 4 * a * c

	if delta < 0:
		raise NumberError("No real roots!")
	elif delta == 0:
		return - b / (2 * a)
	else:
		return (- b + delta**(1/2) ) / (2 * a), (- b - delta**(1/2) ) / (2 * a)

#print(calculate_quadratic(1, 2, 1))  # Case for Delta = 0
#print(calculate_quadratic(1, 4, 1))  # Case for Delta > 0
#print(calculate_quadratic(10, 2, 1)) # Case for Delta < 0 (error)


# --- SORTING --- #

unsorted_array = np.asarray([randrange(100) for _ in range(5)])
print(f"Unsorted:\n{unsorted_array}")

# Quick sort implementation
def my_sort(array):

	half_array_length = int(len(array) / 2)
	# take the middle-ish element as pivot
	pivot = array[half_array_length]

	for i in range(len(array)):
		j = len(array) - i - 1

		if j == i:
			j -= 1
		elif j < i:
			break

		if array[i] > array[j]:
			array[j], array[i] = array[i], array[j]

	print(locals())
	new_array = np.array([])
	# sort left side
	if len(array[:half_array_length]) > 1:
		np.append(new_array, my_sort(array[:half_array_length]))
	# sort right side
	if len(array[half_array_length:]) > 1:
		np.append(new_array, my_sort(array[half_array_length:]))

	print(locals())
	return array

sorted_array = my_sort(unsorted_array)
natively_sorted_array = np.sort(unsorted_array)

print(f"My sort:\n{sorted_array}")
print(f"Built-in sort:\n{natively_sorted_array}", end="\n\n")
print(f"'Are the arrays sorted the same?'...{(sorted_array == natively_sorted_array).all()}")
