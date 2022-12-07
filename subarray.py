''''
Given an unsorted array of size N that contains only non-negative integers, find a
contiguous subarray that adds to a given number S. In case of multiple subarrays, return
the subarray which comes first on moving from left to right. Eg, let us say the array is - 3,
6, 7, 5, 10. And the value of S = 12. The output should be - 7, 5'''




# def subsetsum(n,arr,sum):
#     i=0
#     while i<n:
#         j=0
#         while j<n:
#             if arr[i]+arr[j]==sum and arr[j]<arr[i]:
#                 # p=arr[i]+arr[j]
#                 s=[(arr[i]),arr[j]]
#             j+=1
#         i+=1
#     # if p==sum:
#     print("the subarray  of the sum",sum,"is: ",s)
#     # else:
#     #     print("there is no subset")
# n=int(input())
# arr=list(map(int,input().split()))
# sum=int(input())
# subsetsum(n,arr,sum)




'''sub arrays using recursion'''

# def rec_subarray(arr,start,end):
#     if end==len(arr):
#         return arr[0]
#     elif start>end:
#         return rec_subarray(arr,0,end+1)
#     else:
#         sub.append(arr[start:end+1])
#         return rec_subarray(arr,start+1,end)
# arr =[1,2,3,4]
# sub=[]
# rec_subarray(arr,0,0)
# print(sub)




# def recursiveSubArray(array,start,end):
#     if end==len(array):
#         return subArray
#     elif start>end: 
#         return recursiveSubArray(array,0, end+1)
#     else:
#         subArray.append(array[start:end+1])
#         return recursiveSubArray(array,start+1,end)
# array=[1,2,3,4,5]
# subArray=[]
# print(recursiveSubArray(array,0,0))



# def recursiveSubArray(array,start,end):
#     if end>len(array):
#         return ''
#     elif end==len(array):
#         return recursiveSubArray(array,start+1,start+1)
#     elif start<=end: 
#         print(array[start:end+1])
#         return recursiveSubArray(array,start, end+1)
# array=[4,5,7]
# # subArray=[]
# print(recursiveSubArray(array,0,0)) 



t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    subArray=[]
    for i in range(n+1):
        for j in range(i):
            subArray.append(a[j:i])
    print(subArray)
    c=1
    for i in range(len(subArray)):
        if len(subArray[i])==1:
            c+=1
        elif len(subArray[i])>1 and sum(subArray[i])%k==0:
            c+=1
        
    print(c)
    
            
    