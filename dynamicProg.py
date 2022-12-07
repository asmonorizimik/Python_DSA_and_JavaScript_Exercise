# '''factorial
# 5=5*4*3*2*1 = 120'''
# arr=[]
# for i in range(1,6):
#     if i==1:
#         arr.append(1)
#     else:
#         arr.append(arr[-1]*i)
# print(arr)




'''store the previous value
'''



'''fibonacci series
0,1,1,2,3,5,8,13....
'''

# i=2
# arr=[0,1]
# while i<=11:
#     arr.append(arr[-1]+arr[-2])
#     i+=1
# print(arr) 


'''power of 2'''
a=[2]
for i in range(1,11):
    a.append(2*a[-1])
print(a)



'''
check whether the given no. is power of 2 or not
16= 4 power 2'''
# n=int(input())
# i=1
# res=False
# while i<=n:
#     if 2**i>n:
#         res=False
#     elif 2**i==n:
#         res = True
#         break
#     i+=1
# print(res)







'''missing series
n=max element of the array
s=sum of the array
formula: x= n*(n+1)//2 now x-s= missing number
max element * max element + 1 divided by 2 and this value minus the sum of the array find out the missing element'''
arr=[1,2,3,5]
x=sum(arr)
y=((max(arr)*(max(arr)+1))//2)
print(y-x)








'''square of number till 100 using dynamic prog
[2,4,9,16,25,36,49,64,81,100]'''

# i=1
# arr=[1,4]
# n=int(input())
# while i<9:
#     arr.append(arr[-1]+n+(2*i))
#     i+=1
# print(arr)

