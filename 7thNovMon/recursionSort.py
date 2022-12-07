# arr=list(map(int,input().split()))

# arr=[5,6,3,4,8,9,12]
# n=6
# def bubsort(arr,n):
#     for i in range(n-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]
#     if n>0:
#         bubsort(arr,n-1)

# bubsort(arr,n)
# print(arr)


# arr=[3,4,5,1,2]
# n=len(arr)
# def bubsort(arr,n):
#     if n==0:
#         return arr[0]
#     else:
#         for i in range(0,n-1):
#             if arr[i]>arr[i+1]:
#                 arr[i],arr[i+1]=arr[i+1],arr[i]
#         return bubsort(arr,n-1)
# print(bubsort(arr,n))
# print(arr)

''' insertion sort
    selection sort'''


'''insertion sort'''
# arr=[2,4,6,1,7,12,5]
# for i in range(1,len(arr)):
#     key=arr[i]
#     j=i-1
#     while j>=0 and key<arr[j]:
#         arr[j+1]=arr[j]
#         j-=1
#     arr[j+1]=key
# print(arr)






'''selection sort'''






# def swap(A, i, j):
#     temp = A[i]
#     A[i] = A[j]
#     A[j] = temp
# def selectionSort(A, i, n):
#     min = i
#     for j in range(i + 1, n):
#          if A[j] < A[min]:
#             min = j  
#     swap(A, min, i)
#     if i + 1 < n:
#         selectionSort(A, i + 1, n)
# A = [3, 5, 8, 4, 1, 9, -2]
# selectionSort(A, 0, len(A))
# print(A)
 



# def selectionSort(A,b):
#     if len(A)==0:
#         return ""
#     else:
#         j=A.index(min(A))
#         A[0],A[j]=A[j],A[0]
#         b.append(A[0])
#         return selectionSort(A[1:], b)
# A = [3, 5, 8, 4, 1, 9, -2]
# b=[]
# selectionSort(A,b)
# print(b)



    




# def bub_sort(arr,n):
#     if n==0:
#         return arr
#     else:
#         for i in range(n-1):
#             if arr[i+1]<arr[i]:
#                 arr[i],arr[i+1]=arr[i+1],arr[i]
#         return bub_sort(arr,n-1)
# arr=[2,3,1,4,5]
# print(bub_sort(arr,5))
# # print(arr)



