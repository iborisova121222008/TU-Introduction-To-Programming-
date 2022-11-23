n = int(input('Num = '))
list=[]
for i in range(1, n+1):
    print(f"{n}"*i,end=" + ")

total = 0
s = n
for i in range(0,n):

    total+=s
    s = s * 10 + n

print(" = ", total)
