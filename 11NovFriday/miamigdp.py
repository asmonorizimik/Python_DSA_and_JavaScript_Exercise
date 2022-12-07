'''

'''




t=int(input())
while t!=0:
    x,y=map(int,input().split())
    if (x*107)/100>=y:
        print("YES")
    else:
        print("NO")
    t-=1