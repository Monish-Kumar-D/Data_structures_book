def nth_fibonacci(n):
    if n<=1:
        return n
    return nth_fibonacci(n-1) + nth_fibonacci(n-2)
    
if __name__ == "__main__":
    n = 8
    print(f"{n}th fibonacci number is: ", nth_fibonacci(n))


"""
TC: for every n we call 2, so tc will be nearly O(2^n)
SC: O(2^n)

"""