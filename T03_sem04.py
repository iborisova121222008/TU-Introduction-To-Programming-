def list_avg(list, multiplier=1):
    sum = 0
    count = 0

    for i in range((len(list))):
        if type(list[i]) == int or type(list[i]) == float:
            sum += list[i] * multiplier
            count += 1
        elif type(list[i]) == str and list[i].isnumeric():
            sum += int(list[i]) * multiplier
            count += 1

    if count != 0:
        return (sum / count)
    else:
        print("Error message")
        return


print(list_avg(["4", 1.5, "@7$", 3.5, (1, "hi")]))
print(list_avg(['6', 3, 3.0], 2))
print(list_avg(['%$', {}]))
print(list_avg([]))
