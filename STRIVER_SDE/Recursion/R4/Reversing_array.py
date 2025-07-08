def reverse_array_using_recursion(left,n,array):
    if left >n-left-1:
        return 
    else:
        array[left], array[n-left-1] = array[n-left-1], array[left]
        reverse_array_using_recursion(left+1, n, array)

if __name__ == "__main__":
    array = [10,9,8,7,6,5,4,3,2,1]
    print("initial_array", array)
    left = 0
    n = len(array)
    reverse_array_using_recursion(left, n, array)
    print("final array: ", array)

"""
TC : O(n)
SC : O(n)
"""