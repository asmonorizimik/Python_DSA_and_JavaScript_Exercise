# str="abcde"
# i=len(str)-1
# print(i)
# s=""
# while i>=0:
#     s+=str[i]
#     i-=1
# print(s)

def rev_string(string):
    if len(string)==0:
        return ""
    else:
        return string[len(string)-1] + rev_string(string[0:len(string)-1])###string[-1]+
print(rev_string("abcde"))