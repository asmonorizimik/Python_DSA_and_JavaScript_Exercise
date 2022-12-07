'''
Description
Given an array of integers of length n and a positive integer K, the task is to find the count of the longest possible subarrays with the sum of its elements not divisible by K.
Input
Input Format
First line contains n and k separated by space
Second line contains strings of length n.
Constraints
1 <= n <=10^6
1 <= k <= 100
Output
Print count of sub arrays.
Sample Input 1 
4 3
2 3 4 6
Sample Output 1
1
Hint
Sample 1 Explanation
[2],[3],[4],[6],[2,3],[2,3,4],[3,4,6],[3,4],[4,6]
There is only one longest possible subarray of size 3 i.e. {3, 4, 6} having a sum 13, which is not divisible by K = 3.

'''


# n,k=map(int,input().split())
n,k=4,3
arr=[2,3,4,6]
# arr=list(map(int,input().split()))
sub=[]
for i in range(n+1):
    for j in range(i):
        sub.append(arr[j:i])
l=0
c=0
for x in range(len(sub)):
    sum=0
    for y in range(x):
        sum+=y
    if len(sub[x])>1 and len(sub[x])<=len(arr) and sum % k!=0:
        c+=1
print(c)
print(sub)






# n=5
# k=5
# s_arr=[]
# arr=[1,2,2,2,3]
# max_len=0
# count=0
# for i in range(0,n):
#     for j in range(i,n):
#         m=(arr[i:j+1])
#         m=(arr[i:j+1])
#         if (sum(m)%k!=0 and len(m)>max_len):
#             max_len=len(m)
#             count=0
#         # modified_arr.append(i)
#             # if len(m)>max_len:
#                 # max_len=len(m) #1 2
#                 # count=0
#             if len(m)==max_len:
#                 count+=1
# # modified_arr=[]
# # max_len=0
# # count=0
# # for i in s_arr:

#     # if (sum(i)%k!=0):
#     #     # modified_arr.append(i)
#     #     if len(i)>max_len:
#     #         max_len=len(i) #1 2
#     #         count=0
#     #     if len(i)==max_len:
#     #         count+=1

# # print(s_arr)
# # print(modified_arr)
# print(count)

