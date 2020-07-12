#linear search

def linearsearch(list1,key):
    for i in list1:
        if i==key:
            print("the number is present in the index :",list1.index(i))
            return True
    return False

list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

x=int(input("Enter a number to find in the list "))

if not linearsearch(list1,x):
    print("The number is not in the list")