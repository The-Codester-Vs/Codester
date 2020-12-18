# Quick Sort
def partition(arr,l,h):
    i = l-1
    pivot = arr[h]
    
    for j in range(l,h):
        if arr[j] <= pivot:
            i += 1 
            arr[j],arr[i] = arr[i], arr[j]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return(i+1)

# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,l,h): 
	if l < h: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr,l,h) 

		# Separately sort elements before 
		# partition and after partition 
		quickSort(arr, l, pi-1) 
		quickSort(arr, pi+1, h) 

def iterative_Quicksort(arr,l,h):
    size = h-l + 1
    stack = [0] *(size)
    
    top = -1
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
    
    while top >= 0:
        h = stack[top]
        top -= 1 
        l = stack[top]
        top -= 1 
        
        p = partition(arr,l,h)
        
        if p-1>l:
            top = top+1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        
        if p+1 < h:
            top += 1
            stack[top] = p+1
            top += 1
            stack[top] = h
        
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
iterative_Quicksort(arr,0,n-1)
print ("Sorted array is:") 
for i in range(n): 
	print (arr[i],end= " ")


