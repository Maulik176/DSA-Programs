def countsort(arr, exp1):
	n = len(arr)

	result = [0] * (n)
	count = [0] * (10)

	for i in range(0, n):
		index = arr[i] // exp1
		count[index % 10] += 1

	for i in range(1, 10):
		count[i] += count[i - 1]

	i = n - 1
	while i >= 0:
		index = arr[i] // exp1
		result[count[index % 10] - 1] = arr[i]
		count[index % 10] -= 1
		i -= 1

	i = 0
	for i in range(0, len(arr)):
		arr[i] = result[i]


def radixSort(arr):
	MAX = max(arr)
	exp = 1
	while MAX / exp > 0:
		countsort(arr, exp)
		exp *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]

radixSort(arr)

for i in range(len(arr)):
	print(arr[i])