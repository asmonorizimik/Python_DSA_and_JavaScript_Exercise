''' ending number counting and sum of that counts
'''

a=[12,30,45,56,73,33,35,57,68,90,78,51]
num=[0,0,0,0,0,0,0,0,0,0]
i=1
d={}
while i<len(a):
    last=a[i]%10
    num[last]+=1
    i+=1
sum=0
for i in range(len(num)):
    d[i]=num[i]
    sum+=num[i]
print(d)
print(sum)

