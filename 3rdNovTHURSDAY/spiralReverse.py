'''
Description
You are given a square matrix of size N x N.
You have to print the spiral traversal of the matrix.
Refer the figure given below for better understanding.

Input
The first line of the input contains T, the number of test cases.
The first line of each test case contains N, the size of the matrix.
The next N lines contain N integers each denoting the values of the matrix.
Constraints
1 <= T <= 10
1 <= N <= 500
1 <= A[i][j] <= 500
Output
For each test case, print the spiral traversal of the matrix, as shown in the problem description, on a single line, on a new line.
Sample Input 1 
1
3 
1 2 3
4 5 6
7 8 9

Sample Output 1
7 8 9 6 3 2 1 4 5
Hint
The spiral traversal for a given matrix is shown in the image in the problem description.
'''



# l=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# arr=[]
# n=3
# top=0
# side=0
# rows=n
# col=n
# while side < col and top<rows:
#     for i in range(side,col):
#         arr.append(l[rows-1][i])
#     rows-=1
#     for i in range(rows-1,top-1,-1):
#         arr.append(l[rows-1][-1])
#     col-=1
#     for i in range(col-1,side-1,-1):
#         arr.append(l[top][i])
#     top+=1
#     for i in range(top,rows):
#         arr.append(l[i][side])
#     side+=1
# print(*arr)



# 7 8 9 6 3 2 1 4 5
# 12369745

l=[[1,2,3],
   [4,5,6],
   [7,8,9]]
arr=[]
n=3
top=0
side=0
rows=n
col=n
while side < col and top<rows:
    for i in range(side,col):
        arr.append(l[top][i])
    print(arr)
    col-=1
    for i in range(top+1,col):
        arr.append(l[rows-1][-1])
        print(arr,2)
    rows-=1
    for i in range(col-1,side-1,-1):
        arr.append(l[rows][i])
    print(arr,3)
    top+=1
    for i in range(top,rows):
        arr.append(l[i][side])
    print(arr,4)
    side+=1
print(*arr)
