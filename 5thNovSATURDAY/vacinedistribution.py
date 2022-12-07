'''
Finally, a COVID vaccine is out on the market and the Chefland government has asked 
you to form a plan
to distribute it to the public as soon as possible. There are a total of NN people 
with ages a_1, a_2, \ldots, a_Na 
1

 ,a 
2

 ,…,a 
N

 .

There is only one hospital where vaccination is done and it is only possible to vaccinate up to DD people per day.
 Anyone whose age is \ge 80≥80 or \le 9≤9 is considered to be at risk. On each day, 
 you may not vaccinate both a person who 
 is at risk and a person who is not at risk. Find the smallest number of days needed to vaccinate everyone.

Input
The first line of the input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
The first line of each test case contains two space-separated integers NN and DD.
The second line contains NN space-separated integers a_1, a_2, \ldots, a_Na 
1

 ,a 
2

 ,…,a 
N

 .
Output
For each test case, print a single line containing one integer ― the smallest required number of days.


Sample 1:
Input                                    Output
2
10 1
10 20 30 40 50 60 90 80 100 1              10
5 2
9 80 27 72 79                              3

Explanation:
Example case 1: We do not need to worry about how the people are grouped, since only one person can be 
vaccinated in a single day. We require as many days as there are people.

Example case 2: There are two people at risk and three people who are not at risk. One optimal strategy 
is to vaccinate the two people at risk on day 11 and the remaining three on the next 22 days.
'''


t=int(input())
while t!=0:
    n,d=map(int,input().split())## no of people for a day
    age=list(map(int,input().split()))##ages of the people
    l=[]
    day=0
    for j in age:
        if j<=9 or j>=80:
            l.append(j)###apeople at the risk 
    x=n-len(l)
    if len(l)%d==0:
        day=int(len(l)/d)
    else:
        day=int(len(l)/d)+1
    if x%d==0:
        day+=int(x/d)
    else:
        day+=int(x/d)+1
    print(day)
    t-=1