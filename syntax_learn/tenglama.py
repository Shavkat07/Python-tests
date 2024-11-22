# import sympy as sp
#
#
# def solve_equation(equation_str):
#     x = sp.symbols('x')
#     equation = sp.sympify(equation_str)
#
#     solutions = sp.solve(equation, x)
#     return solutions
#
#
# equation_str = input("Введите уравнение с одной неизвестной x: ")
# solutions = solve_equation(equation_str)
#
# if solutions:
#     print("Решения уравнения:")
#     for solution in solutions:
#         print(solution)
# else:
#     print("Уравнение не имеет решений или решение не найдено.")

# f = open("file.txt", "r")
# print(f.read(20))
# print(f.read(8))
# print(f.read(3))

memory = [0] * 30000
pointer = 0

memory[pointer] += 8
while memory[pointer] > 0:
    pointer += 1
    memory[pointer] += 7
    pointer += 1
    memory[pointer] += 10
    pointer += 1
    memory[pointer] += 3
    pointer -= 3
    memory[pointer] -= 1

print(chr(memory[pointer]), end='')

pointer += 1
print(chr(memory[pointer]), end='')

pointer += 1
while memory[pointer] > 0:
    pointer += 1
    print(chr(memory[pointer]), end='')
    pointer += 1
    memory[pointer] += 2

pointer += 1
print(chr(memory[pointer]), end='')

pointer += 1
while memory[pointer] > 0:
    pointer += 1
    print(chr(memory[pointer]), end='')

print()
