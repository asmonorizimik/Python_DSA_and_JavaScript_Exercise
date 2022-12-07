'''
sum of digit of a number until it becomes one digit
n=123
k=2
n*k=123123123
sum of digit===123123123 --18 --9
output =9
'''

n=int(input())
k=int(input())
s=int(str(n)*k)
def oneDigit(s):
    sum=0
    while s!=0:
        digit=s%10
        sum+=digit
        s=s//10
    if sum>9:
        return oneDigit(sum)
    else:
        return sum
print(oneDigit(s))


