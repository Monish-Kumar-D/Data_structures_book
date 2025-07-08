def count_subseq_with_sum_k(index, current_sum, sum_required, n):
    if index >=n:
        if current_sum == sum_required:
            return 1
        return 0
    else:
        current_sum +=main_array[index]
        l = count_subseq_with_sum_k(index+1, current_sum, sum_required, n)
        current_sum-=main_array[index]
        r = count_subseq_with_sum_k(index+1, current_sum, sum_required, n)
        return l+r
            
if __name__ == "__main__":
    main_array = [1,2,1]
    sum_required = 2
    n = len(main_array)
    index = 0
    current_sum = 0
    print(count_subseq_with_sum_k(index, current_sum, sum_required, n))