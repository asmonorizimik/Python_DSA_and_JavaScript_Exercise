'''
Chef had a sequence of positive integers with length N + KN+K. He managed to calculate the arithmetic average of all elements of this sequence 
(let's denote it by V), but then, his little brother deleted K elements from it. All deleted elements had the same value.
Chef still knows the remaining N elements — a sequence A_1, A_2,....An

Help him with restoring the original sequence by finding the value of the deleted elements or deciding that 
there is some mistake and the described scenario is impossible.
Note that the if it is possible for the deleted elements to have the same value, then it can be proven that it is unique. 
Also note that this value must be a positive integer.

Input
The first line of the input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
The first line of each test case contains three space-separated integers NN, KK and VV.
The second line contains NN space-separated integers A_1, A_2,....An.

Output
For each test case, print a single line containing one integer — the value of the deleted elements, or -1 if there is a mistake.
Sample 1:
Input     Output
3
3 3 4
2 7 3     4
3 1 4
7 6 5    -1
3 3 4
2 8 3    -1
'''

t=int(input())
while t!=0:
    n,k,v=map(int,input().split())##n=3(len),k=3(deleted),v=4(average)
    arr=list(map(int,input().split()))## [2,7,3]=12
    s=0##sum of arr
    i=0
    while i<n:
        s+=arr[i]
        i+=1
    x=v*(n+k)-s##average *(no.of element)+(el. deleted)-sum
    if x%k==0 and x>0:
        print(x//k)
    else:
        print(-1)
    t-=1






# for  _ in range(int(input())):
#     a,b,c=map(int,input().split())
#     d=list(map(int,input().split()))
#     s=sum(d)
#     r=(((a+b)*c)-s)/b
    
#     if(r>0 and r%1==0):
#         print(int(r))
#     else:
#         print(-1)







# for _ in range(int(input())):
#     n,k,v=map(int,input().split())
#     l=list(map(int,input().split()))
#     s=sum(l)
#     i=v*(n+k)-s
#     if i%k==0 and i>0:
#         print(i//k)
#     else:
#         print(-1)



t=int(input())
while t!=0:
    n,k,v=map(int,input().split())##3,3,4(average)
    arr=list(map(int,input().split()))
    
    s=0
    i=0
    while i<len(arr):
        s+=arr[i]
        i+=1
    x=v*(n+k)-s
    if x%k==0 and x>0:
        print(x//k)
    else:
        print(-1)
    t-=1