
'''Chef is moving to a new house!

Unfortunately, this means he now has to pack up his things so that they can be moved too. Currently, 
Chef is packing up his (rather impressive) book collection into cardboard boxes.

Chef has XX shelves of books, each of which contains exactly YY books. Each cardboard box can hold at
 most ZZ books. In order to not mess up the organization of the books, Chef will also ensure that books 
 from different shelves will not be placed in the same box.

Under these conditions, what is the minimum number of boxes needed to pack all the books?'''

t=int(input())
while t!=0:
    box=0
    x,y,z=map(int,input().split())
    if y%z==0:
        box=x*(y//z)
    else:
        box=x*(y//z+1)
    print(int(box))
    t-=1
    