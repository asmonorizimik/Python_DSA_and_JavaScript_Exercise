'''
Chef has an array consisting of N + K - 1Nintegers. The array contains only the first NN positive odd numbers. Each number appears exactly once, except for one number which appears exactly KK times. The sum of integers in Chef's array is equal to SS.

For example, for N = 3N=3, K = 2K=2, the possible arrays could be [1, 1, 3, 5][1,1,3,5], [3, 1, 3, 5][3,1,3,5], [5, 3, 5, 1][5,3,5,1]. For N = 1N=1, K = 3K=3, there is only one possible array: [1, 1, 1][1,1,1].

Chef gives you three integers NN, KK and SS and asks you to find the only element which appears KK times in his array.

It is guaranteed that for the given input, there exists a valid array consisting of N + K -1N+K−1 elements with a sum exactly equal to SS.

Input Format
The first line of the input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
The first and only line of each test case contains three space-separated integers N, K, SN,K,S.
Output Format
For each test case, print a single line containing the integer which appeared KK times in Chef's array.

 
Sample 1:
Input:      output:
3
3 2 14       5
5 4 28       1
2 3 10       3

Explanation:
Test case 11: Chef's array could be [5, 3, 5, 1][5,3,5,1].

Test case 33: Chef's array could be [3, 1, 3, 3][3,1,3,3].
'''



# t=int(input())
# while t!=0:
#     n,k,s=map(int,input().split())
#     s=s-(n**2)
#     print(s//(k-1))
#     t-=1



# t = int(input())
# while(t):
#     n , k, s = map(int , input().split( ))
#     l = [(2*i-1) for i in range(1,n+1)]
#     print(l)
#     smm = sum(l)
#     for i in range(len(l)):
#         x = l[i]
#         y = smm + x*(k-1)
#         if(y == s):
#             print(x)
#             break
#     t -=1



t = int(input())
while t!=0:
    l=[]
    n,k,s = map(int,input().split( ))
    i=1
    while i<=n:
        l.append(2*i-1)
        i+=1
    j=0
    while j<len(l):
        x = sum(l)+ l[j]*(k-1)
        if(x==s):
            print(l[j])
            break
        j+=1
    t -=1

