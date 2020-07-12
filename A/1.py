#bubblesort

def bubblesort(list1):
    n=len(list1)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]

list1=[1,431,142,542,7658,123,5643,13]

bubblesort(list1)

print("Sorted list :",list1)
