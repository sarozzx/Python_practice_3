#insertion sort

def insertionsort(list1):
    for i in range(1,len(list1)):
        key=list1[i]
        j=i-1
        while j>=0 and key<list1[j]:m
            list1[j+1]=list1[j]
            j-=1
        list1[j+1]=key

list1=[1,431,142,542,7658,123,5643,13]

insertionsort(list1)

print("Sorted list :",list1)