# cook your dish here
import string
t=int(input())
while t>0:
    n=int(input())
    a=str(input())
    b=str(input())
    ans=0
    for i in range(0,n):
        if string.ascii_lowercase.index(a[i])>string.ascii_lowercase.index(b[i]):
            j=26-(string.ascii_lowercase.index(a[i])-string.ascii_lowercase.index(b[i]))
            ans+=j
        else:
            k=string.ascii_lowercase.index(b[i])-string.ascii_lowercase.index(a[i])
            ans+=k
    print(min(abs(ans%26-26),ans%26))
    t-=1