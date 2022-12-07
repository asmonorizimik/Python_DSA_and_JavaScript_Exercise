
# x=2
# y=4
# o/p=2 power4

def power(x, y):
    if y == 0:
        return 1
    else:
        return (x*power(x, y-1))
print(power(9,3))

'''

'''