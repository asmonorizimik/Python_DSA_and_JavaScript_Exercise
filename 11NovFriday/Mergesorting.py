# MergeSort in Python


# def mergeSort(array):
#     if len(array) > 1:

#         #  r is the point where the array is divided into two subarrays
#         r = len(array)//2
#         L = array[:r]
#         M = array[r:]

#         # Sort the two halves
#         mergeSort(L)
#         mergeSort(M)

#         i = j = k = 0 #left index, right index and position
#         while i < len(L) and j < len(M):
#             if L[i] < M[j]:
#                 array[k] = L[i]
#                 i += 1
#             else:
#                 array[k] = M[j]
#                 j += 1
#             k += 1
#         while i < len(L):
#             array[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(M):
#             array[k] = M[j]
#             j += 1
#             k += 1

# # Print the array
# def printList(array):
#     for i in range(len(array)):
#         print(array[i], end=" ")
#     print()

# array = [6, 5, 12, 10, 9, 1]
# mergeSort(array)

# print("Sorted array is: ")
# printList(array)







def mergeSort(array):
    if len(array)>1:
        mid=len(array)//2
        left=array[:mid]
        right=array[mid:]
        mergeSort(left)
        mergeSort(right)
        leftIndex=0
        rightIndex=0
        position=0
        while leftIndex<len(left) and rightIndex<len(right):
            if left[leftIndex]<right[rightIndex]:
                array[position]=left[leftIndex]
                leftIndex+=1
            else:
                array[position]=right[rightIndex]
                rightIndex+=1
            position+=1
        while leftIndex < len(left):
            array[position] = left[leftIndex]
            leftIndex += 1
            position+= 1

        while rightIndex < len(right):
            array[position] = right[rightIndex]
            rightIndex+= 1
            position += 1

        return array
array=[32,2,0,-1,38,45,3,6,7,30]
print(mergeSort(array))
