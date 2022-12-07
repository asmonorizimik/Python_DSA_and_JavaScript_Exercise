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
    if len(sub[x])>1 and sum % k!=0:
        c+=1
print(c)
print(sub)

 

















