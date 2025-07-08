def print_any_one_subseq_with_sum_k(index, array, current_sum, sum_required, n):
    if index >=n:
        if current_sum == sum_required:
            print(array)
            return True
        return False
    else:
        array.append(main_array[index])
        current_sum +=main_array[index]
        if print_any_one_subseq_with_sum_k(index+1, array, current_sum, sum_required, n) == True:
            return True
        array.pop()
        current_sum-=main_array[index]
        if print_any_one_subseq_with_sum_k(index+1, array, current_sum, sum_required, n) == True:
            return True
        return False
            
if __name__ == "__main__":
    main_array = [1,2,1]
    sum_required = 2
    n = len(main_array)
    index = 0
    current_sum = 0
    array = []
    print_any_one_subseq_with_sum_k(index, array, current_sum, sum_required, n)