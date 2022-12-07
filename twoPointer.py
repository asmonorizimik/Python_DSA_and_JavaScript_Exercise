'''subset sum sorted array or two pointer
[1,2,3,4,5,6,7,8,9,11,12]
target=17
divide the array
take out mid point= 6
start =0
last = len of array = 10
if start +last 13 is less than target , start +1
1+12=13 0
2+12=14 1
3+12=15 2
4+12=16 3
5+12=17 4
if start + last == target, they are in index 4 and 10
print array[start] and  array[end] array[4]+array[10] = 5+12 =17

'''
arr=[1,2,3,4,5,6,7,8,9,12]