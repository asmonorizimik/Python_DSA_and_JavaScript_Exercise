
'''check at left side 
Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
Insertion sort works similarly as we sort cards in our hand in a card game.


We assume that the first card is already sorted then, we select an unsorted card. If the unsorted card is greater 
than the card in hand, it is placed on the right otherwise, to the left. In the same way, other unsorted cards are 
taken and put in their right place'''


'''card
key=2
[2,4,6,1,7,12,5]
key=4
2,4,6,1,7,12,5
key=6
2,4,6,1,7,12,5
key=1
1,2,4,6,7,12,5
key=7
1,2,4,6,7,12,5
key=12
1,2,4,6,7,12,5
key=5
1,2,4,5,6,7,12'''









# arr=[2,4,6,1,7,12,5]
# for i in range(len(arr)):
#     key=arr[i]
#     j=i
#     while j!=0 and key<arr[j-1]:
#         arr[j],arr[j-1]=arr[j-1],arr[j]
#         j-=1
#     key=arr[j]
# print(arr)

'''
0
i in range(7) 0 to 7
key =arr[0]=2
j=i = 0
while 0!=0 and 2<5: false
key =arr[j] =2

1
key=arr[1] =2
j=1
1!=0()True and 2<arr[0](2)False
key= arr[1]=4
j=0
0!=0

2
2!=0 and 4<arr[2-1]=arr[1]=4(False)
1!=0 and 4<arr[1]=4
key = 6

3
j=3-1 = 2
3!=0 and 6<arr[2]=6
j=2-1 =1
2!=0 and 6<arr[1]=4
    arr[j],arr[j-1]=arr[j-1],arr[j]
    4,


'''



# arr=[2,4,6,1,7,12,5]
# for i in range(1,len(arr)):
#     key=arr[i]
#     j=i-1
#     while j>=0 and key<arr[j]:
#         arr[j+1]=arr[j]
#         j-=1
#     arr[j+1]=key
# print(arr)

    






# def insertion_sort(arr, Len):
#     if Len <= 1:
#         return arr
#     else:
#         insertion_sort(arr, Len - 1)
#         end = arr[Len - 1]
#         i = Len - 2
#         while(i>=0 and arr[i] > end):
#             arr[i+1] = arr[i]
#             i = i - 1
#         arr[i + 1] = end
# array = [9, 1, 7, 3, 5]
# insertion_sort(array, len(array))
# print(array)




