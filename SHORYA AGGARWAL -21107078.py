# SID 21107078
# SHORYA AGGARWAL
# MECHANICAL ENGINEERING


# In a sorted infinite array/list we have to find the end point r which is the last element for searching
# Binary search algorithm implementation
def binary_search(arr,l,r,x):
 
    if r >= l:
        mid = l+(r-l)//2
 
        if arr[mid] == x:
            return mid
 
        if arr[mid] > x:
            return binary_search(arr,l,mid-1,x)
 
        return binary_search(arr,mid+1,r,x)
 
    return -1
 
# function takes an infinite size array and a key to be
# searched and returns its position if found else -1.
# We don't know size of a[] and we can assume size to be
# infinite in this function.
# NOTE THAT THIS FUNCTION ASSUMES a[] TO BE OF INFINITE SIZE
# THEREFORE, THERE IS NO INDEX OUT OF BOUND CHECKING
def findPos(arr, key):
  
    l, h, val = 0, 1, arr[0]
 
    # Find h to do binary search
    while val < key:
        l = h            #store previous high
        h = 2*h          #double high index
        val = arr[h]       #update new val
 
    # at this point we have updated low and high indices,
    # thus use binary search between them
    return binary_search(arr, l, h, key)
 
# Driver function
arr = []
i=0
while i<1000 :
    arr.append(i)
    i=i+1
n = int(input("Enter the digit to find in the array"))
ans = findPos(arr,n)
if ans == -1:
    print ("Element not found")
else:
    print("Element found at index",ans)