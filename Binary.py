
n1 = int(input())
print(bin(n1) [2:])

binar = int(bin(n1) [2:])

list1 = list(map(int, str(binar)))
print(list1)

n2 = int (input())

if n2 <= len(list1):
    if list1[n2] == 1 :
      print("The number on this position {} is 1.".format(n2))
 
    elif list1[n2] == 0:
      print("The number on this position {} is 0.".format(n2))
       
else:
    print("List index out of range.")

