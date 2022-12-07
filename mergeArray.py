'''Input: arr1[] = { 1, 3, 2}, arr2[] = {4, 6, 5} 
Output: arr3[] = {1, 2, 3, 4, 5,6}
Merge two sorted arrays into a single sorted array
'''




def mearge_array(array1,array2,array3,n1,n2):
    i=0
    k=0
    while i<n1:
        array3[k]=array1[i]
        i+=1
        k+=1
    j=0
    while j<n2:
        array3[k]=array2[j]
        j+=1
        k+=1
    x=0
    while x<len(array3):
        y=0
        while y<len(array3):
            if array3[x]<array3[y]:
                array3[x],array3[y]=array3[y],array3[x]
            y+=1
        x+=1
    return array3
array1=list(map(int,input().split()))
array2=list(map(int,input().split()))
array3=array1+array2
n1=int(input())
n2=int(input())

print(mearge_array(array1,array2,array3,n1,n2))