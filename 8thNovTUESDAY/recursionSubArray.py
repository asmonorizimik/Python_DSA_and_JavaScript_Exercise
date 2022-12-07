'''sub arrays using recursion'''

# def rec_subarray(arr,start,end):
#     if end==len(arr):
#         return arr[0]
#     elif start>end:
#         return rec_subarray(arr,0,end+1)
#     else:
#         sub.append(arr[start:end+1])
#         return rec_subarray(arr,start+1,end)
# arr =[1,2,3,4]
# sub=[]
# rec_subarray(arr,0,0)
# print(sub)




# def recursiveSubArray(array,start,end):
#     if end==len(array):
#         return subArray
#     elif start>end: 
#         return recursiveSubArray(array,0, end+1)
#     else:
#         subArray.append(array[start:end+1])
#         return recursiveSubArray(array,start+1,end)
# array=[1,2,3,4,5]
# subArray=[]
# print(recursiveSubArray(array,0,0))



def recursiveSubArray(array,start,end):
    if end>len(array):
        return ''
    elif end==len(array):
        return recursiveSubArray(array,start+1,start+1)
    elif start<=end: 
        print(array[start:end+1])
        return recursiveSubArray(array,start, end+1)
array=[1,2,3,4,5]
# subArray=[]
print(recursiveSubArray(array,0,0)) 