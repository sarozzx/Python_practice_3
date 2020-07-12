#interpolation search

def interpolationSearch(arr, n, x):

    lo = 0
    hi = (n - 1)

    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo;
            return -1;

        pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            lo = pos + 1;

        else:
            hi = pos - 1;

    return -1

list1=[]

z=int(input("how many numbers are there in the list "))

for y in range(z):
    k=int(input())
    list1.append(k)

list1.sort()
n = len(list1)

x=int(input("what do u wnna search  "))

result = interpolationSearch(list1, n, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

