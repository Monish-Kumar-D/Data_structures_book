def print_subsequences(index, array, n):
    if index >= n:
        print(array)
    else:
        array.append(main_array[index])
        print_subsequences(index+1, array, n)
        array.pop()
        print_subsequences(index+1, array, n)

if __name__ == "__main__":
    main_array = [3,1,2]
    array = []
    n = len(main_array)
    i = 0
    print_subsequences(i, array, n)

"""
Time complexity: O(2^n) x O(n)#for printing the array
Space complexity: O(n)

"""