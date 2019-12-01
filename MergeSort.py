numberList = [0, 6, 12, 2, 3, 4, 5, 88, 34, 111, 23, 13, 99, 28, 47, 1]
print('numbers: ', numberList)
# Merge Sort is efficient for larger data sets
# O(n log n)
def merge_sort(numbers):
	merge_sort2(numbers, 0, len(numbers) - 1)

def merge_sort2(numbers, first, last):
	if first < last:
		middle = (first + last)//2
		merge_sort2(numbers, first, middle)
		merge_sort2(numbers, middle+1, last)
		merge(numbers, first, middle, last)

def merge(numbers, first, middle, last):
	L = numbers[first:middle+1]
	R = numbers[middle+1:last+1]
	i = j = 0
	for k in range(first, last+1):
		if i >= len(L) and j <= len(R):
			numbers[k] = R[j]
			j += 1
			continue
		if j >= len(R) and i <= len(L):
			numbers[k] = L[i]
			i += 1
			continue
		if L[i] <= R[j]:
			numbers[k] = L[i]
			i += 1
		else:
			numbers[k] = R[j]
			j += 1


merge_sort(numberList)
print('sorted list: ', numberList)