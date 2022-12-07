'''
You have a binary string SS. You can perform the following operation on SS:
Select any substring S which is sorted in non-decreasing order and remove it from S. 
(Both the left and right halves are concatenated after performing the operation)
For e.g. if S = 100011000, we can perform the following operation: 100011000 =remove 011 = 100000
Find the minimum number of operations required so that the final binary string S is sorted in non-decreasing order.

Note that a substring is formed by deleting some (possibly zero) characters from the beginning and some (possibly zero) characters from the end of the string.

Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first line of each test case contains an integer N — the length of the binary string S.
The second line of each test case contains a binary string S of length N containing 0s and 1s only.

Output Format
For each test case, output the minimum number of operations required so that the final binary string SS is sorted in non-decreasing order.


Sample 1:
Input      Output
3
3
000         0
5           
01110       1
2           
10          1

Explanation:
Test case 1: The binary string is already sorted, so we need no operations.

Test case 2: We can use one operation to remove the sorted substring S2...4}= 111S 
2…4
 =111. Thus, the remaining string 0000 is sorted.

Test case 3: We can use one operation to remove the sorted substring S2...2 = 0S 
2…2
 =0. Thus, the remaining string 11 is sorted.
'''

t= int(input())
while t!=0:
    n=int(input())
    s=input()
    c=0
    i=0
    while i<n-1:
        if s[i]+s[i+1]=='10':
            c+=1
        i+=1

    print(c)
    t-=1
   

# 01110
# for x in range(int(input())):
#     n=int(input())
#     x='01110'#input()
#     c=0
#     for i in range(1,n):
#         if x[i-1]=='1' and x[i]=='0':
#             c=c+1
#     print(c)


# for t in range(int(input())):
#     n = int(input())
#     s = input()
#     print(s.count("10"))
    