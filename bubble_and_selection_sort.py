"""
Bubble Sort:
    Repeatedly compares neighboring elements and swaps them if they are in the wrong order.
    The largest unsorted element "bubbles up" to the end of the array after each pass.
    The sorted portion grows from the BACK of the array.
 
Selection Sort:
    Finds the smallest unsorted element and places it at the front.
    It assumes the first unsorted element is the smallest, then scans the rest to check.
    The sorted portion grows from the FRONT of the array.
"""

arr=[2,2,5,8,4,3,6,34, 67, 1, 7]

def bubble_sort(arr):
    n=len(arr)

    for i in range(n): #this one is responsible for telling j how many elements are already bubbled (not necessary to check anymore)
        for j in range(0, n-1-i): #j is dependent on i iterations, each succesful bubble means the range will shrink by 1 at the end 
            if arr[j]>arr[j+1]: #classic comparison, only swaps when there previous element is larger than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j] # python specific sytax for swapping two variables in a single line
    return arr
            
def selection_sort(arr):
    n=len(arr)

    for i in range(n-1): #i is reponsible for telling j how many 'smallest' numbers have been locked to the left end
        smallest=i #the first element is always the assumed smallest
        for j in range(1+i, n): #the purpose of j is to update the smallest variable within a range, i tells j which indexes to only check
            if arr[j]<arr[smallest]:
                smallest=j #there is a new smallest in town!
        arr[smallest], arr[i] = arr [i], arr[smallest] # swapping the new smallest to the initial smallest, YES in the outer loop!
    return arr
    
print(bubble_sort(arr))
print(selection_sort(arr))