#binary search

def bsearch(list1,l,h,x):
    if(h>=l):
        mid =(h+l)//2
        if(list1[mid]==x):
            return mid
        elif list1[mid]>x:
            return bsearch(list1,l,mid-1,x)
        else:
            return bsearch(list1,mid+1,h,x)
    else:
        return -1

list1=[]

z=int(input("how many numbers are there in the list "))

for y in range(z):
    k=int(input())
    list1.append(k)

list1.sort()

x=int(input("what do u wnna search  "))

result=bsearch(list1,0,len(list1)-1,x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array") 