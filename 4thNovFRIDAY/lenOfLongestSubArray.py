'''
Description
Given an array A with n integers, find out the length of the longest subarray which is strictly increasing i.e, every element is 
greater than it's the previous element in that subarray.
Expected Time Complexity O(n^2) for each array.

Input:
The first line of the input contains one integer t (1 ≤ t ≤ 10) — the number of test cases. Then t test cases follow.
The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the number of elements in the array A.
The second line of each test case contains n integers (1 ≤ Ai ≤ 100).

Output:
For each test case, print the answer: The length of the longest subarray.
Sample Input 1 
2
2
1 1 -------1
6
1 2 1 2 3 1-----3

Sample Output 1
1
3
'''



# '''subarray using binary numbers'''
# arr=[1,2,3]
# n=3
# res=[]
# for i in range(1,2**n):
#     a=str(bin(i)[2:])[::-1]##binary numbers
#     temp_arr=[]
#     for i in range(len(a)):
#         if a[i]=='1':
#             # print(type(arr[i]))
#             temp_arr.append(arr[i])
#     res.append(temp_arr)
# print(res)








# Q:=[1,2,1,2,3,1]
# #output:[[1],[2,1],[1,2,3],[2,3,1]]  output:largest len =3


t=int(input())
while t!=0:
    n=int(input())
    arr=list(map(int,input().split()))
    array=[]
    d={}
    for i in range(1,n+1):
        d[str(i)]=[]
    for i in range(n):
        for j in range(i,n):
            a=arr[i:j+1]
            d[str(len(a))].append(a)
    l=0
    for i in d:
        if int(i)>l and int(i)<n:
            l=int(i)
    print(d)
    print(l)
    t-=1








