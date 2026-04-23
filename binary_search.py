"""
Binary Search:
    A searching algorithm that recursively compares the target value to the midpoint element in SORTED array. \
    Has a time complexity of O(n log n)
"""
arr=[1,3,5,6,7,9,5,3,2]
def binary_search(arr, target, left=0, right=len(arr), iteration=0): #When just want to store left, right, and iteration for every recursion

    if left>=right: #Very rare edge case if left and right are pointing at the same thing already
        return  f"We can't find {target} from the array..."
    
    midpoint=(left+right)//2 #Computes the midpoint depending on the current left and right boundary from a certain recursion step

    if arr[midpoint]==target: #Yeah
        return f"{target} exists from the array with {iteration} recursion/s"
    elif arr[midpoint]>target: #If the midpoint element is greater than the target, then we disregard every element from the midpoint's right side
        return binary_search(arr, target, left, midpoint-1, iteration+1) 
    elif arr[midpoint]<target: # Vice versa
        return binary_search(arr, target, midpoint+1, right, iteration+1)
    else: #Self-explanatory
        return f"We can't find {target} from the array..."
    

print(binary_search(arr, 3))
    
