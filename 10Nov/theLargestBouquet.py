# for _ in range(int(input())):
#     mg,my,mr = map(int, input().split(' '))
#     oog,ooy,oor = map(int, input().split(' '))
#     pg,py,pr =  map(int, input().split(' '))
#     var = [(mg+my+mr),(oog+ooy+oor),(pg+py+pr),(mg+oog+pg),(my+ooy+py),(mr+oor+pr)]
#     print(var)
#     # print(var)
#     for i in range(len(var)):
#         if var[i]%2==0:
#             var[i]-=1
#     var.append(0)
#     print(max(var))
#     print(var)








# cook your dish here
t=int(input())
while t!=0:
    # green,yellow,red
    mg,my,mr=map(int,input().split())
    og,oy, orr=map(int,input().split())
    pg,py,pr=map(int,input().split())
    bouquets=[]
    bouquets.append(mg+my+mr)
    bouquets.append(og+oy+orr)
    bouquets.append(pg+py+pr)
    bouquets.append(mg+og+pg)
    bouquets.append(my+oy+py)
    bouquets.append(mr+orr+pr)
    print(bouquets)
    j=0
    while j<len(bouquets):
        if bouquets[j]%2==0:
            bouquets[j]-=1
        j+=1
    bouquets.append(0)
    print(max(bouquets))
    print(bouquets)
    t-=1




# cook your dish here
# t=int(input())
# while t!=0:
#     # green,yellow,red
#     maple=list(map(int,input().split()))
#     oak=list(map(int,input().split()))
#     poplar=list(map(int,input().split()))
#     bouquets=[]
#     bouquets.append(sum(maple))
#     bouquets.append(sum(oak))
#     bouquets.append(sum(poplar))
#     i=0
#     while i<len(maple):
#         x=maple[i]+oak[i]+poplar[i]
#         bouquets.append(x)
#         i+=1
#     j=0
#     m=0
#     while j<len(bouquets):
#         if bouquets[j]%2!=0 and bouquets[j]>m:
#             m=bouquets[j]
#         j+=1
#     print(m)
#     t-=1