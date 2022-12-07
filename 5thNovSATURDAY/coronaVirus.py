'''
There are NN people on a street (numbered 11 through NN). For simplicity, we'll view them as points on a line. For each valid ii, 
the position of the ii-th person is X_iX 
i

 .

It turns out that exactly one of these people is infected with the virus COVID-19, but we do not know which one. 
The virus will spread from an infected person to a non-infected person whenever the distance between them is at most 22. 
If we wait long enough, a specific set of people (depending on the person that was infected initially) will become infected;
 let's call the size of this set the final number of infected people.

Your task is to find the smallest and largest value of the final number of infected people, i.e. this number in the best and in
 the worst possible scenario.

Input
The first line of the input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
The first line of each test case contains a single integer NN.
The second line contains NN space-seperated integers X_1, X_2, \ldots, X_NX 
1

 ,X 
2

 ,…,X 
N
 .
Output
For each test case, print a single line containing two space-separated integers ― the minimum and maximum possible final number of infected people.


Sample 1:
Input         Output

3
2
3 6             1 1
3
1 3 5           3 3
5
1 2 5 6 7       2 3

Explanation:
Example case 1: The distance between the two people is 3, so the virus cannot spread and at the end, there will always be only one infected person.

Example case 2: The distance between each two adjacent people is 2, so all of them will eventually get infected.

Example case 3:
In one of the best possible scenarios, the person at the position 11 is infected initially and the virus will also infect the person at the position 22.
In one of the worst possible scenarios, the person at the position 55 is infected initially and the virus will also infect the people at the positions 66 and 77.
Practice Special Block
PYTH 3
'''



n=int(input())
while n!=0:
    x=int(input())##no. of items
    l=list(map(int,input().split()))
    k=[]
    c=1
    i=0
    while i<x-1:
        if((l[i+1]-l[i])<=2):
            c=c+1
        else:
            k.append(c)
            c=1
        i+=1
    k.append(c)
    j=0
    min=1000
    max=0
    while j<len(k):
        if k[j]<min:
            min=k[j]
        if k[j]>max:
            max=k[j]
        j+=1
    print(min,max)
    n-=1


