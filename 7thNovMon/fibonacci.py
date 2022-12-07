'''fibonac'''
# def fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(fibo(n-1) + fibo(n-2))
# n = 10
# if n>=0:
#    print("Fibonacci sequence:")
#    for i in range(n):
#        print(fibo(i))


def fibo(n):
    if n<=1:
        # arr.append(0)
        return n
    else:
        arr.append(fibo(n-1)+fibo(n-2))
        return fibo(n-1)+fibo(n-2)
arr=[]
n=10
print(fibo(n))
print(arr)