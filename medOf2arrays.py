'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the
median of the two sorted arrays.
'''



def medOfTwoArrays(num1,num2,size1,size2,num3):
    i=0
    size=size1+size2
    l=[]
    while i<size:
        j=0
        while j<size:
            if num3[i]<num3[j]:
                num3[i],num3[j]=num3[j],num3[i]
            j+=1
        i+=1
    k=0
    while k<size:
        if num3[k] not in l:
            l.append(num3[k])
        k+=1
    s=len(l)
    if s%2==0:
        x=l[s//2]+l[s//2-1]
        print("median:",l[s//2])
    else:
        print("median:",l[s//2])
    # print(num3)
    # print(l)
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
num3=num1+num2
size1=int(input())
size2=int(input())
medOfTwoArrays(num1,num2,size1,size2,num3)