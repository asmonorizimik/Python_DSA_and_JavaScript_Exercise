'''
use no built-in function like len() and list method
Find the mean, median, and mode in an array
Mean : The mean is the average of all numbers and is 
sometimes called the arithmetic mean.
Median : The median is the middle number in a group of numbers
Mode: The mode is the number that occurs most often within a set of numbers.
'''



def sort_array(array,n):
    i=0
    while i<n:
        j=0
        while j<n:
            if array[i]<array[j]:
                array[i],array[j]=array[j],array[i]
            j+=1
        i+=1
    return array
n=int(input())
array=list(map(int,input().split()))
# print(sort_array(array,n))


i=0
sum=0
d={}
remove_dup=[]
array1=sort_array(array,n)
# print(array1)
while i<n-1:
    sum+=array1[i]
    if array1[i] not in remove_dup:
        remove_dup.append(array1[i])
    if array1[i] not in d:
        d[array1[i]]=1
    else:

        d[array1[i]]+=1
    i+=1



mode=0
for k in d: 
    if d[k]>mode:
        mode=d[k]

mode_l=[]
for y in d:
    if d[y]==mode and d[y]>1:
        mode_l.append(y)

print("mean",sum/n)    
n1=len(remove_dup)
if n%2==0:
    x=remove_dup[n1//2]+remove_dup[n1//2-1]
    print("median:",remove_dup[x//2])
else:
    print("median",remove_dup[n1//2])
print("modes/mode: ",mode_l)  



