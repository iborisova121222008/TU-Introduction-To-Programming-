n = int(input())
num1 = 0
num2 = 1

result = 0
for i in range(0,n+2):
    print(num1)

    result = num1 + num2
    num1=num2
    num2=result
