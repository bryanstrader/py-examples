numbers = [0, 6, 12, 2, 3, 4, 5, 88, 34, 111, 23, 13, 99, 28]

print("pre-sort: ", numbers)

for n in numbers:
	for i, n2 in enumerate(numbers):
		if len(numbers) > i+1:
			if n2 > numbers[i+1]:
				temp = numbers[i+1]
				numbers[i+1] = n2
				numbers[i] = temp

print("after-sort:", numbers)