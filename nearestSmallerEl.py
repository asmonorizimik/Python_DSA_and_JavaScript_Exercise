'''
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
Mathematically,
G[i] for an element A[i] is an element A[j] such that
j is maximum possible AND
j < i AND
A[j] < A[i]
Note: Elements for which no smaller element exist, consider next smaller element as -1.
nearest smallest element to the left :[-1,-1,19,21,35,-1,-1,-1]

input:   39 27 11 4 24 32 32 1
output: -1 -1 -1 -1 4 24 24 -1 
'''



# arr=[31,19,21,35,36,9,7,1] 
# arr=[39,27,11,32,32,32,32,1] 
# arr1=[]
# for i in range(len(arr)):
#     for j in range(i-1,-2,-1):
#         if arr[j]<arr[i]:
#             arr1.append(arr[j])
#             break
#         if j== -1:
#             arr1.append(-1)
#             break
# print(arr1)


# # # arr=[31,19,21,35,36,9,7,1]
# arr=[39,27,11,4,32,32,32,1] 
# # arr=list(map(int,input().split()))
# arr1=[-1]
# i=0
# while i<len(arr)-1:
#     if arr[i+1]<arr[i]:
#         arr1.append(-1)
#     elif arr[i+1]==arr[i]:
#         arr1.append(arr[i-1])
#     else:
#         arr1.append(arr[i])
#     i+=1
# print(arr1)










    