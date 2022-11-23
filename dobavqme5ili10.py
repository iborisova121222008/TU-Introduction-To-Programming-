list1= []
n = int(input('Num = '))

for i in range(n+1):
    list1.append(i)

token=int(input("Command = "))
for i in  range(0,len(list1)):
    if list1[i] % 2 == 0 and token == 1:
        list1[i] += 10
    if list1[i] % 2 != 0 and token == 0:
        list1[i] += 5
    print(list1[i], end=" ")
