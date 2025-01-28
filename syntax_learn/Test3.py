

# dictionary = {}
# a = '{"number": 0, "type": "standard_single_room", "status": 0, "floor": 1},\n{"number": 1, "type": "delux_single_room", "status": 0, "floor": 2},\n{"number": 1, "type": "delux_single_room", "status": 0, "floor": 2},\n{"number": 1, "type": "delux_single_room", "status": 0, "floor": 2},'
# a1 = [
# 	{"number": 0, "type": "standard_single_room", "status": 0, "floor": 1},
# 	{"number": 1, "type": "delux_single_room", "status": 0, "floor": 2},
# ]
#
#
# b = a.split('\n')
# # print(b)
# for i in b:
# 	print(

# import os

# print(type(os.path.exists("./syntax_learn/Annotation.py")))

# a = input("malumot: ")
#
# print(type(a))


# a = {"asd345": 23, "asdfg": 234}
#
# b = {"asda": 23, "asdf56": 23434}
#
# c =  {**a, **b}
# print(c)

a = [{ "a": 1, "b": 2, "c": 3, "d": 4, "e": 5 }, {"a": 3, "b": 4, "c": 433, "d": 64, "e": 75}]


print([i for i in a if i["a"] == 1][0]['a'])


