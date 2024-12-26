

def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	barrier = arr[0]
	L = []
	M = []
	R = []
	for i in arr:
		if i == barrier:
			M.append(i)
		elif i < barrier:
			L.append(i)
		else:
			R.append(i)

	quick_sort(L)
	quick_sort(R)

	k = 0

	for i in L + M + R:
		arr[k] = i
		k += 1

	print(arr)

print(quick_sort([23, 46, 45, 65, 423, 334, 53, 43, 53, 42, 34, 24, 12]))
