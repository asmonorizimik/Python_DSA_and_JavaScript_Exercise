'''The first thing Chefu wanted to do was to calculate the result of his homework — the sum of AA and BB, and write it using matches. 
input:
3 
123 234
10101 1010
4 4

output:
13
10
7

Example case 1: The result is 357357. We need 55 matches to write the digit 33, 55 matches to write the digit 55 and 33 matches to write the digit 77.
Example case 2: The result is 1111111111. We need 22 matches to write each digit 11, which is 2 \cdot 5 = 102⋅5=10 matches in total
'''



t=int(input())
while t!=0:
    matchs=[6,2,5,5,4,5,6,3,7,6]
    x,y=map(int,input().split())
    sum=str(x+y)
    c=0
    i=0
    while i<len(sum):
        c+=matchs[int(sum[i])]
        i+=1
    print(c)
    t-=1

