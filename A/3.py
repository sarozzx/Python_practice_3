#quick sort

def partition(list2, low, high):
    i = (low - 1)
    pivot = list2[high]
    for j in range(low, high):
        if list2[j] <= pivot:
            i += 1
            list2[i], list2[j] = list2[j], list2[i]
    list2[i + 1], list2[high] = list2[high], list2[i + 1]
    return (i + 1)


def quick_sort(list2, low, high):
    if low < high:
        pi = partition(list2, low, high)
        quick_sort(list2, low, pi - 1)
        quick_sort(list2, pi + 1, high)


list1=[1,431,142,542,7658,123,5643,13]


low = 0

high = len(list1) - 1

quick_sort(list1, low, high)

print("Sorted list :",list1)