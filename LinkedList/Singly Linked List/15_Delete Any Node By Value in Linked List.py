class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("The Linked list is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end="")
                n = n.next

    def add_begin(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def add_end(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = Node(data)

    def after_node(self,data,x):
        if self.head is None and x != 0:
            print("Number is out of bound")
        else:
            n = self.head
            i =0
            while i <x and n is not None:
                i = i +1
                n = n.next
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
    
    def before_node(self,data,x):
        if self.head is None and x != 0:
            print("Number is out of bound")
        else:
            n = self.head
            i = 0
            while i < x-1 and n is not None:
                i = i+1
                n = n.next
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node


# Delete Any Node By Value in Linked List 

    def delete_by_value(self,x):
        if self.head is None:
            print("The Linked list is Empty We can't delete this element!")
            return
        if self.head == x:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Out of bound")
        else:
            n.next = n.next.next

        
         
        
        

LL = LinkedList()
LL.add_begin(10)
LL.add_begin(20)
LL.add_end(300)
LL.add_end(293)
LL.after_node(899,1)
LL.after_node(10033,4)
LL.before_node(57,2)
LL.delete_by_value(10)

LL.print_LL()
