# merge sort
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        MergeSort(L)
        MergeSort(R)
        
        i = k = j = 0 
        while i < len(L) and j< len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k]= R[j]
            j += 1
            k += 1
def printlist(arr):
    for i in range(len(arr)):
        print(arr[i],end = " ")
    print()                          

if __name__ == '__main__':
    arr = [1,2,4,5,7,4,2,0]
    printlist(arr)
    MergeSort(arr)
    printlist(arr)
                                        