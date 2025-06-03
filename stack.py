class Stack:
    def __init__(self, length):
        """
            input: length -> takes an integer which is
        
        """
        self.arr = [0]*length
        self.length = length
        self.index = -1

    def push(self, num):
        if self.index <self.length:
            self.index +=1
            self.arr[self.index] = num
        else:
            print("Stack overflow")
        
    def pop(self):
        if self.index == -1:
            print("stack underflow")
        else:
            temp = self.index
            self.index -=1
            return self.arr[temp]

    def peek(self):
        return self.arr[self.index]
    
    def print_stack(self):
        print(self.arr)

if __name__ == "__main__":
    stack = Stack(10)
    stack.push(5)
    stack.push(10)
    stack.print_stack()
    s = stack.pop()
    print(s)
    stack.print_stack()
    stack.push(4)
    stack.print_stack()
    r =stack.peek()
    print(r)
    print(stack.pop())
    stack.print_stack()
    stack.push(3)
    stack.print_stack()