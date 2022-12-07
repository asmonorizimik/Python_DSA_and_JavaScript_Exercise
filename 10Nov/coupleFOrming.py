t=int(input())
while t!=0:
    n=int(input())
    h_boys=list(map(int,input().split()))
    h_boys.sort()
    h_girls=list(map(int,input().split()))
    h_girls.sort()
    couple=[]
    i=0
    while i<n:
        couple.append(h_boys[i]+h_girls[i])
        i+=1
    print(h_boys)
    print(h_girls)
    j=0
    m=0
    while j<len(couple):
        if couple[j]>m:
            m=couple[j]
        j+=1
    print(m)
    t-=1