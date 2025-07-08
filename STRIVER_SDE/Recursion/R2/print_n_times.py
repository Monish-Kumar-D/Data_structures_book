def print_name(i,n, name):
    if n == i:
        return 
    print(name)
    print_name(i+1,n,name)

if __name__ == "__main__":
    name = input("Name: ")
    n = int(input("Enter n: "))
    print_name(0,n,name)

"""
Time Complexity: O(n)

Space Complexity also the stack complexity in the memory space for the recursion: O(n)

"""