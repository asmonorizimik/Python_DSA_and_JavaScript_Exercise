'''
Description
Given an array of N integers, print the 3 distinct maximum and 3 distinct minimum elements of the array.
Input
Input Format
First line contains N
Second line contains N space separated integers which are elements of the array.
Constraints
0<=N<=100 (Please note that N can be 0 as well)
The values present in the array can be negative as well.

Output
In the first line, print the least 3 values (sorted) present in the array.
In the second line, print the top 3 values (sorted) present in the array.
In case there are not 3 min value, print "Not Possible" (without quotes).
In case there are not 3 max value, print "Not Possible" (without quotes).
So, according to the above statements, if both are not possible, you have to print "Not Possible" twice (once for each)
In the array, if you found out only 2 distinct min and 2 distinct max elements then also printNot Possibletwice [ one for minimum and other for maximum]
Sample Input 1 
8
1 2 3 4 2 1 6 5
Sample Output 1
1 2 3
4 5 6
'''
n=int(input())
arr1=[]
arr=list(map(int,input().split()))
i=0
while i<n:
    if arr[i] not in arr1:
        arr1.append(arr[i])
    i+=1
arr1.sort()
print(arr1)
if len(arr1)<3:
    
    print("not possible") 
else:
    print(arr1[-3:],"max")
    print(arr1[:3],"min")










# arr1=[1,2,3,4,2,1,6,5]
# a=set(arr1)
# arr=list(a)
# arr.sort()

# if len(arr)<3:
#     print("not possible") 
# else:
#     print(arr[-3:],"max")
#     print(arr[:3],"min")


