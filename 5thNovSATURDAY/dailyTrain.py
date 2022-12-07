# cook your dish here
# from math import factorial
# x, n = map(int, input().split())
# ans = 0
# for _ in range(n):
#     s = input()
#     cp = 54
#     for i in range(9):
#         value = str(s[i*4:i*4+4] + s[cp-2:cp])
#         cp -= 2
#         comb = value.count('0')
#         if(comb > x):
#             ans += factorial(comb) / (factorial(comb - x)*factorial(x))
#         elif(x == comb):
#             ans += 1
# print(int(ans))


'''
A daily train consists of N cars. Let's consider one particular car.
It has 54 places numbered consecutively from 1 to 54, some of which are 
already booked and some are still free. The places are numbered in the following fashion:

The car is separated into 9 compartments of 6 places each, as shown in the picture. 
So, the 1st compartment consists of places 1, 2, 3, 4, 53 and 54, the 2nd compartment consists of places 5, 6, 7, 8, 51 and 52, and so on.

A group of X friends wants to buy tickets for free places, all of which are in one compartment (it's much funnier to travel together).
You are given the information about free and booked places in each of the N cars.
Find the number of ways to sell the friends exactly X tickets in one compartment (note that the order in which the tickets are
sold doesn't matter).

Input
The first line of the input contains two integers X and N (1 ≤ X ≤ 6, 1 ≤ N ≤ 10) separated by a single space. 
Each of the following N lines contains the information about one car which is a string of length 54 consisting of '0' and '1'. 
The i-th character (numbered from 1) is '0' if place i in the corresponding car is free, and is '1' if place i is already booked.

Output
Output just one integer -- the requested number of ways.

Sample 1:
Input
Output
1 3
100101110000001011000001111110010011110010010111000101
001010000000101111100000000000000111101010101111111010
011110011110000001010100101110001011111010001001111010
85
Explanation:
In the first test case, any of the free places can be sold.

Sample 2:
Input
Output
6 3
100101110000001011000001111110010011110010010111000101
001010000000101111100000000000000111101010101111111010
011110011110000001010100101110001011111010001001111010
1
Explanation:
In the second test case, the only free compartment in the train is compartment 3 in the first car (places 9, 10, 11, 12, 49 and 50 are all free).

Sample 3:
Input
Output
3 2
000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000
360
Explanation:
In the third test case, the train is still absolutely free; as there are 20 ways to sell 3 tickets in an empty compartment, the answer is 2 * 9 * 20 = 360
'''


def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

(x,n) = map(int, input().split())
s = []
seat = 0
for i in range(n):
    s = input()
    counter=[]
    car = 0
    for j in range(9):
        counter = []
        counter.append(s[(j*4)+0])
        counter.append(s[(j*4)+1])
        counter.append(s[(j*4)+2])
        counter.append(s[(j*4)+3])
        counter.append(s[(j*-2)-2])
        counter.append(s[(j*-2)-1])
        place = 6-sum(map(int, counter))
        if place >= x:
            ways = fact(place)/(fact(x)*fact(place-x))
        else:
            ways = 0
        car = car+ways
    seat = seat + car
print(int(seat))