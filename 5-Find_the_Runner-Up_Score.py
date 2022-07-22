# 11:50
n=int(input("enter the number of elements: "))
arr=[]
for x in range(0,n):
    elements=int(input("enter elements: "))
    arr.append(elements)
print("The runner up score is")
print(sorted(list(set(arr)))[-2])
#12:26