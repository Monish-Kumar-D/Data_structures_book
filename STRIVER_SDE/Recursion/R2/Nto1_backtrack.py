def print_from_n_to_1_using_backtrack(i, n):
    if n < i:
        return 
    print_from_n_to_1_using_backtrack(i+1, n)
    print(i)

if __name__ == "__main__":
    n = int(input())
    print_from_n_to_1_using_backtrack(1, n)

"""
TC: O(n)
SC: O(n)
"""