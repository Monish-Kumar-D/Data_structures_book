def print_from_1_to_n_using_backtrack(n):
    if n < 1:
        return 
    print_from_1_to_n_using_backtrack(n-1)
    print(n)

if __name__ == "__main__":
    n = int(input())
    print_from_1_to_n_using_backtrack(n)

"""
TC: O(n)
SC: O(n)
"""