def check_palindrome(left,n,array):
    if left >n-left-1:
        return True
    elif array[left] != array[n-left-1]: 
        return False
    else:
        return check_palindrome(left+1, n, array)

if __name__ == "__main__":
    string = ["MADAm", "HELLO", "ANA", "CUUC", "MONISH"]
    for i in string:
        left = 0
        i = i.lower()
        n = len(i)
        if check_palindrome(left, n, i):
            print("The string {} is a palindrome".format(i))
        else:
            print("The string {} is not a palindrome".format(i))

"""
TC : O(n)
SC : O(n)
"""