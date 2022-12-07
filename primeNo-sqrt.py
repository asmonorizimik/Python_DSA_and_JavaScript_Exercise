# # n=int(input())
# # print(n**((1//2)+1)) ##square root +1
# # i=1
# # c=0
# # while i<=n**((1//2)+1):
# #     if n%i==0:
# #         c+=1
# #     i+=1
# # if c==2:
# #     print("prime")
# # else:
# #     print("not prime")






# start=int(input()) #10
# stop=int(input()) #30
# arr=[]
# while start<=stop:
#     j=2
#     c=0
#     while j<=start**((1//2)+1):
#         if start%j==0:
#             c+=1
#         j+=1
#     if c==1:
#         arr.append(start)
#     start+=1
# print(arr)




# t=int(input())
# while t!=0:
#     a,b=map(int,input().split())
#     j=1
#     p=[]
#     while j<=b:
#         if b%j==0:
#             p.append(j)
#         j+=1
#     c=0
#     pf=[]
#     i=0
#     while i<len(p):
#         j=1
#         c=0
#         while j<p[i]:
#             if p[i]%j==0:
#                 c+=1
#             j+=1
#         if c==1:
#             pf.append(p[i])
#         i+=1
#     res=""
#     for k in range(len(pf)):
#         if a%pf[k]==0:
#             print("YES")
#             break
            
#         elif a%pf[k]!=0:
#             print("NO")
#             break
            
#     t-=1


















t=int(input())
while t!=0:
    a,b=map(int,input().split())
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors  
    # print(prime_factors(b))
    x=prime_factors(b)
    for j in range(len(x)):
        if a%x[j]==0:
            print("YES")
            break
        elif a%x[j]!=0:
            print("NO")
            break
    t-=1

