"""  Bubble sort Algorithm """

""" version 1 """

# nums = [4, 6, 3, 5, 8, 9, 1, 4, 2, 3, 2, 0]
#
# swaps = True
# while swaps:
# 	swaps = False
# 	for i in range(len(nums) - 1):
# 		if nums[i] > nums[i + 1]:
# 			swaps = True
# 			nums[i], nums[i + 1] = nums[i + 1], nums[i]
# print(nums)

""" version 2  """

# for i in range(len(nums)):
# 	for j in range(len(nums) - i - 1):
# 		if nums[i] > nums[i + 1]:
# 			swaps = True
# 			nums[i], nums[i + 1] = nums[i + 1], nums[i]
# print(nums)

""" Factorial of number with Recursion"""

# number = 998
#
# def factorial(n):
# 	if n == 0:
# 		return 1
#
# 	return factorial(n - 1) * n
#
# print(factorial(number))

""" Factorial of number with Loop """

# number = 1000
#
# def factorial(n):
# 	if n == 0:
# 		return 1
#
# 	f = 1
# 	i = 0
# 	while i < n:
# 		i += 1
# 		f *= i
#
# 	return f
#
# print(factorial(number))


"""  Fibonacci   """







