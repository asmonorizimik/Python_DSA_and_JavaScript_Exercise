# arr=[5,1,2,4,3]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i]<arr[j]:
#             # arr[i],arr[j]=arr[j],arr[i]
#             # print(arr[i],arr[j])
#             t=arr[i]
#             arr[i]=arr[j]
#             arr[j]=t
# print(arr)





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




'''
not using any memory bcoz it swaps in that same array
4,3,8,2,0,5,8,12,7
3,4,8,2,0,5,8,12,7
3,4,2,8,0,5,8,12,7
3,4,2,0,8,5,8,12,7
3,4,2,0,5,8,8,12,7
3,4,2,0,5,8,8,12,7
3,4,2,0,5,8,8,7,12

3,4,2,0,5,8,8,7,12
3,2,4,0,5,8,8,7,12
3,2,0,4,5,8,8,7,12
3,2,0,4,5,8,8,7,12
3,2,0,4,5,8,8,7,12
3,2,0,4,5,8,7,8,12


2,3,0,4,5,8,7,8,12
2,0,3,4,5,8,7,8,12
2,0,3,4,5,8,7,8,12
2,0,3,4,5,8,7,8,12
2,0,3,4,5,7,8,8,12


0,2,3,4,5,7,8,8,12


'''


def bubSort(array,n):
    if n==0:
        return array
    else:
        for i in range(n-1):
            if array[i+1]<array[i]:
                array[i],array[i+1]=array[i+1],array[i]
        return bubSort(array,n-1)
array=list(map(int,input().split()))
n=len(array)
print(bubSort(array,n))