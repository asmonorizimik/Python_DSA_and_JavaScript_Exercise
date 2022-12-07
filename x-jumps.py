'''Problem
Chef is currently standing at stair 00 and he wants to reach stair numbered XX.

Chef can climb either YY steps or 11 step in one move.
Find the minimum number of moves required by him to reach exactly the stair numbered XX.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of a single line of input containing two space separated integers XX and YY denoting the 
number of stair Chef wants to reach and the number of stairs he can climb in one move.
Input:     output:
4
4 2 -------- 2
8 3 -------- 4
3 4 -------- 3
2 1 -------- 2

Explanation:
Test case 1: Chef can make 2 moves and climb 2 steps in each move to reach stair numbered 4.
Test case 2: Chef can make a minimum of 4 moves. He can climb 3 steps in 2 of those moves and 1
 step each in remaining 2 moves to reach stair numbered 8.
Test case 3: Chef can make 3 moves and climb 1 step in each move to reach stair numbered 3.

Test case 4: Chef can make 2 moves and climb 1 step in each move to reach stair numbered 2.
'''



t=int(input())
while t!=0:
    x,y=map(int,input().split())
    #x=no. of stair chef wants to reach
    #y=no. of stairs he can climb in one move
    move=0
    if x<y:
        move=x
    else:
        move=(x//y)+(x%y)
    print(move)
    t-=1
    