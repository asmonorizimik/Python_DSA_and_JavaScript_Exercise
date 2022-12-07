# Binary Search in python
'''
Binary Search is a searching algorithm for finding an element's position in a sorted array.
In this approach, the element is always searched in the middle portion of an array.
It follows the divide and conquer method
'''

def binarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2 ##middle number

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1
array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]#list(map(int,input().split()))
# array.sort()
x = int(input("enter search"))
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")




# def binarySearch(array, start,end,number):
#     if start<=end:
#         mid =start+(end-start)//2
#         if array[mid]==number:
#             return mid
#         elif number<array[mid]:
#             return binarySearch(array,start,mid-1,number)
#         elif array[mid]<number:
#             return binarySearch(array,mid+1,end,number)
#     else:
#         return "element no found!"
# array=[1,2,3,4,5,6]
# number=int(input())
# print(binarySearch(array,0,len(array)-1,number))















