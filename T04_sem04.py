def input_nums(n):
    my_list = []
    for i in range(n):
        num = input("Enter element: ")
        if num.isnumeric() or type(num) == int:
            my_list.append(num)
    return my_list


def sum_list(lst):
    sum = 0
    for i in lst:
        if type(i) == int or type(i) == float:
            sum += i
        elif type(i) == str and i.isnumeric():
            sum += float(i)
    return sum

    # print(sum_list([1, "a", 3.14, "5"]))
    
def max_of_two(a, b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return a if a >= b else b
        return a

    if type(b) == int or type(b) == float: return b

    return

print(max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"))

# def max_of_two(a, b):
#     if check_number(a) >= check_number(b):
#         if a >= b:
#             return a
#         else:
#             return b
#     if check_number(a):
#         if check_number(b) == False:
#             return a
#     if check_number(b):
#         if check_number(a) == False:
#             return b
#     return
#
#
# def check_number(a):
#     if type(a) == int and type(a) == float:
#         return True
#     elif type(a) == str and a.isnumeric():
#         return True
#     return False


# def max_of_two(a, b):
#     if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float) and a > b:
#         return a
#     elif (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float) and a < b:
#         return b
#     elif (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float) and a == b:
#         return a
#     elif (type(a) == int or type(a) == float) and (type(b) != int or type(b) != float):
#         return a
#     elif (type(b) == int or type(b) == float) and (type(a) != int or type(a) != float):
#         return b
#     return


# print(max_of_two(2.5, 13))
# print(max_of_two("@#$", {}))
# print(max_of_two('a', 5))

# print(max_of_two(sum_list(input_nums(4)), sum_list(3)))
print(max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"))
