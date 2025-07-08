def print_linearly(i,n):
    if n < i:
        return 
    print(i)
    print_linearly(i+1, n)

if __name__ == "__main__":
    n = int(input())
    print_linearly(1, n)

"""
TC: O(n)
SC: O(n)
"""