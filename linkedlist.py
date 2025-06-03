class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def add_first(self,val):
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def remove_first(self):
        temp = self.head
        self.head = self.head.next
        print("Removed element", temp.val)
    
    def print_ll(self):
        temp = self.head
        while temp!=None:
            print(temp.val, "->", end= " ")
            temp = temp.next
        print("None")
    
    def add_last(self,val):
        node = Node(val)

        temp = self.head
        while temp.next!=None:
            temp = temp.next
        temp.next = node
    
    def remove_last(self):
        temp = self.head
        while temp.next.next!=None:
            temp = temp.next
        print("Removed element: ", temp.next.val)
        temp.next = None

    def get_len(self):
        temp = self.head
        l = 0
        while temp!=None:
            l+=1
            temp = temp.next
        return l 

    def add_index(self,val, idx):
        if idx == 0:
            self.add_first(val)
        elif idx == self.get_len():
            self.add_last(val)
        elif 0 < idx < self.get_len():
            node = Node(val)
            temp = self.head
            temp2 = None
            for _ in range(idx):
                temp2 = temp
                temp = temp.next
            node.next = temp
            temp2.next = node
        else:
            print(f"error occured: Invaid Index {idx} when only {self.get_len()} in the list")
    
    def remove_index(self, idx):
        if idx == 0:
            self.remove_first(val)
        elif idx == self.get_len():
            self.remove_last(val)
        elif 0 < idx < self.get_len():
            temp = self.head
            for _ in range(idx-1):
                temp = temp.next
            val = temp.next.val
            temp.next = temp.next.next
            print(f"Removed element {val} at index {idx}")
        else:
            print(f"error occured: Invaid Index {idx} when only {self.get_len()} in the list")
            


if __name__ == "__main__":
    ll = Linkedlist()
    ll.add_first(1)
    ll.add_first(2)
    ll.print_ll()
    ll.remove_first()
    ll.add_first(5)
    ll.add_first(7)
    ll.print_ll()
    ll.add_last(3)
    ll.add_last(25)
    ll.print_ll()
    ll.remove_last()
    ll.print_ll()
    ll.add_index(2,0)
    ll.add_index(4,5)
    ll.print_ll()
    ll.add_index(5, 10)
    ll.add_index(8,2)
    ll.print_ll()
    ll.remove_index(2)
    ll.print_ll()