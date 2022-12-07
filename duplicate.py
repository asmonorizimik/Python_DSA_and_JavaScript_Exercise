'''Find duplicate elements in an array'''


n=int(input())
array=list(map(int,input().split()))
d={}
dup1=[]
array1=[]
i=0
while i<n:
    if array[i] not in d:
        d[array[i]]=1
    else:
        d[array[i]]+=1
    i+=1
for j in d:
    if d[j]>1:
        dup1.append(j)
    else:
        array1.append(j)
print(array1)
print("The duplicate element(s) in an array:",dup1)