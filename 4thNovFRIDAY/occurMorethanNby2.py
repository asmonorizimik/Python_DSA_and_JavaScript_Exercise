'''
PROBLEM -1
Description
Given an array A having N non-negative integers. Find the element that occurs more than N/2 times. If no such element is there then print -1.
Input
First line: Single integer T denoting the number of test cases.
For each test case:
First line: Single integer denoting the value of N.
Next line contains N single space separated integers denoting the elements of array A.
Constraints:
1 <= T<= 10
1<= N <= 100000
0 <= A[ i ] <= 100000
Output
For each test case, print in a new line a single integer denoting the majority element.
Sample Input 1 
2
6
1 1 1 1 2 3
5
1 1 2 2 3
Sample Output 1
1
-1
Hint
Given test cases :
Test case 1 :
N = 6,
A : 1 1 1 1 2 3
1 has occurred 4 times which is greater than N/2. Hence 1 is the majority element.
Test case 2 :
N = 5,
A : 1 1 2 2 3
'''

t=int(input())
while t!=0:
    n=int(input())
    arr=list(map(int,input().split()))
    d={}
    i=0
    while i<len(arr):
        if arr[i] not in d:
            d[arr[i]]=1
        else:
            d[arr[i]]+=1
        i+=1
    for j in d:
        if d[j]>n//2:
            print(1)
            break
        else:
            print(-1)
            break
    t-=1
        
