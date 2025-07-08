def print_subsequences(index, sum1, array, n):
    if index >= n:
        if sum1 == sum_wanted:
            print(array)
        return 
    else:
        array.append(main_array[index])
        sum1+=main_array[index]
        print_subsequences(index+1,sum1, array, n)
        array.pop()
        sum1-=main_array[index]
        print_subsequences(index+1,sum1, array, n)

if __name__ == "__main__":
    main_array = [1,2,1]
    sum_wanted = 2
    init_sum = 0
    array =[]
    n = len(main_array)
    i = 0
    print_subsequences(i,init_sum, array, n)

"""
Time complexity: O(2^n) x O(n)#for printing the array
Space complexity: O(n)

"""