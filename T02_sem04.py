my_list = list()
my_dict = {}

n = int(input('Number N = '))
for i in range(n):
    key = input()
    value = input()
    my_dict[key] = value

m = int(input('Number M = '))
for i in range(m):
    listValue = input()
    if my_dict.keys().__contains__(listValue):
        my_list.append(my_dict[listValue])
        my_dict.pop(listValue)
    else:
        my_list.append(listValue)

print(my_dict)
print(my_list)
