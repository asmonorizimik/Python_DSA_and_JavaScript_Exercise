'''
Find the Union and Intersection of the two sorted arrays
input:
1 3 4 5 7
3 6 5 8 9
5
4
output:
intersection: [3, 5]
union: [1, 3, 4, 5, 7, 3, 6, 5, 8, 9]
'''


def union_intersection(arr1,arr2,n1,n2):
    i=0
    intersect=[]
    while i<n1 or i<n2:
        if arr1[i] in arr2:
            intersect.append(arr1[i])
        i+=1
    print("intersection:",intersect)
    print("union:",arr3)
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr3=arr1+arr2
n1=int(input())
n2=int(input())
union_intersection(arr1,arr2,n1,n2)




 