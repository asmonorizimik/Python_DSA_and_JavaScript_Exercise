
# def selectionSort(arr,numOfElements):
#     i=0
#     mid=i
#     while i<numOfElements:
#         j=i+1
#         while j<numOfElements:
#             if arr[j]<arr[mid]:
#                 mid=j
#             j+=1
#         arr[i],arr[mid]=arr[mid],arr[i]
#         i+=1
# arr =list(map(int,input().split()))
# numOfElements = int(input())-1
# selectionSort(arr, numOfElements)
# print(arr)




# arr=[3,4,2,1,5]
# i=0
# while i<len(arr):
#     min=i
#     j=i+1
#     while j<len(arr):
#         if arr[j]<arr[min]:
#             min=j
#         j+=1
#     arr[i],arr[min]=arr[min],arr[i]
#     i+=1
# print(arr)


'''
Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration 
and places that element at the beginning of the unsorted list.

select first element as minimum

Compare minimum with the second element. If the second element is smaller than minimum, assign the second element as minimum.
Compare minimum with the third element. Again, if the third element is smaller, then assign minimum to the third element 
otherwise do nothing. The process goes on until the last element
and so on


[5,1,4,2,3]
find the min ...
min=1
1,5,4,2,3
min=2
1,2,4,5,3
min=3
1,2,3,4,5
min=5
1,2,3,4,5



[2,4,5,1,4,8,3,7,0]
let the first index be the minimum number and check all the element whether there is lower than the minimum if there is lower number than the minimum then swap or replace with it
min=2,1,0
0,4,5,1,4,8,3,7,2
min=4,3,2,1
0,1,5,4,4,8,3,7,2
min=5,4,3,2
0,1,2,4,4,8,3,7,5
min=4,3
0,1,2,3,4,8,4,7,5
min=4
0,1,2,3,4,4,8,7,5
min=8,7,5
0,1,2,3,4,4,5,7,8
min=7
0,1,2,3,4,4,5,7,8

'''


# def selectionSort(array,sortedArray):
#     if len(array)==0:
#         return sortedArray
#     else:
#         minIndex=array.index(min(array))
#         array[0],array[minIndex]=array[minIndex],array[0]
#         sortedArray.append(array[0])
#         return selectionSort(array[1:],sortedArray)
# array=[8,2,4,0,-1,-9,-10,67,45,3]
# sortedArray=[]
# print(selectionSort(array,sortedArray))





def selectionSort(array,sortedArray):
    if len(array)==0:
        return sortedArray
    else:
        minIndex=array.index(min(array))
        array[0],array[minIndex]=array[minIndex],array[0]
        sortedArray.append(array[0])
        return selectionSort(array[1:],sortedArray)
array=[8,4,5,34,21,-8,-56,0,1,59]
sortedArray=[]
print(selectionSort(array,sortedArray))


    