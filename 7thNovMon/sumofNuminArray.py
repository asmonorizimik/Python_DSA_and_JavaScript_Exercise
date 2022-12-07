arr=list(map(int,input().split()))
def sumOfArray(arr):
    if len(arr)==0:
        return 0
    else:
        return arr[0]+sumOfArray(arr[1:len(arr)])
print(sumOfArray(arr))



'''
reverse substring
power of number'''