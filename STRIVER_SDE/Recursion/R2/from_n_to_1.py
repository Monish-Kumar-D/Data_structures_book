def print_from_n_to_1(n):
    if n < 1:
        return 
    print(n)
    print_from_n_to_1(n-1)

if __name__ == "__main__":
    n = int(input())
    print_from_n_to_1(n)

"""
TC: O(n)
SC: O(n)
"""