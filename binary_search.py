import random

array_start = int(input('Enter the start number\n'))
array_end = int(input('Enter the end number\n'))

def binary_search(start, end):
	true_number = random.randint(start,end)

	max_number = end

	min_number = start

	counter = 1


	while min_number <= max_number:

		mid_number = (min_number + max_number) // 2 	
		
		if mid_number == true_number:
			print(true_number)
			break

		if mid_number > true_number:
			max_number = mid_number
		else:
			min_number = mid_number

		print(f'Step {counter}')
		counter += 1

binary_search(array_start,array_end)


