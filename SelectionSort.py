numbers = [0, 6, 12, 2, 3, 4, 5, 88, 34, 111, 23, 13, 99, 28]
# O(n2) - Nested for loop
print('unsorted', numbers)

for i in range(0, len(numbers) - 1):
	minIndex = i

	for j in range(i + 1, len(numbers)):
		if numbers[j] < numbers[minIndex]:
			minIndex = j
			
	if minIndex != i:
		numbers[i], numbers[minIndex] = numbers[minIndex], numbers[i]

print('sorted', numbers)