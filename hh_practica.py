# def check_all_students_passed(scores_input: str, names_input: str) -> str:
# 	a = scores_input.split(',')
# 	names = names_input.split(',')
# 	v = []
# 	for i in a:
# 		if int(i) < 35:
# 			v.append(a.index(i))
#
# 	if not v:
# 		return 'Все сдали'
# 	else:
# 		print('Есть не сдавшие')
# 		for i in v:
# 			print(names[i])
#
# scores_input = input()
# names_input = input()
# result = check_all_students_passed(scores_input, names_input)
# print(result)


def classify_triangle(input_string: str) -> str:
	num = list(map(int, input_string.split()))
	num.sort()
	if sum(num[0:2]) > num[2]:
		if num[0] == num[1] and num[1] == num[2]:
			return 'Равносторонний'
		elif num[0] == num[1] or num[1] == num[2] or num[0] == num[2]:
			return "Равнобедренный"
		else:
			return 'Разносторонний'
	else:
		return 'Не треугольник'


input_string = input()
result = classify_triangle(input_string)
print(result)
