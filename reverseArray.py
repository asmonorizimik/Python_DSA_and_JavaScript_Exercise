





n=int(input())-1
array=list(map(int,input().split()))
reversed_arrray=array
while n>=0:
    reversed_arrray[n]=array[n]
    n-=1
print(reversed_arrray)
