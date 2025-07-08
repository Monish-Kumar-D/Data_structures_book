def sum_first_n_terms(n):
    if n == 1:
        return 1
    else:
        return n + sum_first_n_terms(n-1)

if __name__ == "__main__":
    n = 3
    print(f"SUM of first {n} numbers is: ", sum_first_n_terms(n))


"""
TC: O(n)
SC: O(n)
"""