def factorial_of_n(n):
    if n == 1:
        return 1
    else:
        return n * factorial_of_n(n-1)

if __name__ == "__main__":
    n = 5
    print(f"Factorial of first {n} is: ", factorial_of_n(n))


"""
TC: O(n)
SC: O(n)
"""