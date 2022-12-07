'''
Description
Given an array of non-negative integers, and a value 'sum', determine if there is a subset of the given set (array) with sum equal to given sum.
If there is a subset whose sum is equal to the required sum then print "yes" else print "no" without quotes.
Input
Input Format :
The first line of input contains an integer N - denoting size of the array.
The second line contains the N space seperated integers.
The third line of input will contain S - the required Sum value.

Constraints :
1<=n<= 18
1<=A[i]<=10^9
Output
Print "yes" or "no" without quotes.
Sample Input 1 
9
1 2 3 4 5 6 7 8 9
5
Sample Output 1
yes

'''

n=int(input())
arr=list(map(int,input().split()))
# arr=[2,3,4,6]
k=int(input())
sub_array=[]
for i in range(n):
    for j in range(i,n):
        sub_array.append(arr[i:j+1])
print(sub_array)
sub=[]
x=0
c=0
while x<len(sub_array):
    if sum(sub_array[x])==k and len(sub_array[x])>1:
        c+=1
        sub.append(sub_array[x])
    x+=1

if c>=1:
    print("yes")
    print(sub)
else:
    print('No')
# print(sub_array)
