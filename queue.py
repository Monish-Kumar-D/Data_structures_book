class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def dequeue(self):
        val = self.head.val
        self.head = self.head.next
        return val
    
    def peek(self):
        return self.head.val

    def print_queue(self):
        temp = self.head
        while temp!=None:
            print(temp.val, "->", end=" ")
            temp = temp.next
        print()
        

if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(3)
    q.print_queue()
    q.enqueue(7)
    q.enqueue(9)
    q.print_queue()
    print("dequeued: ", q.dequeue())
    q.print_queue()
    print(q.peek())
    q.print_queue()


