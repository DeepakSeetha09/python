class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def append(self,n1,n2):
        for i in range(len(n1)):
            data = int(n1[i])+int(n2[i])
            if self.head is None:
                self.head = Node(data)
            else:
                itr = self.head
                while itr.next:
                    itr = itr.next
                itr.next = Node(data)
    def display(self):
        print("The nodes:")
        itr = self.head
        while itr:
            print(itr.data,end=" ")
            itr = itr.next
l1 = Linkedlist()
n1=(input("Enter the nodes:"))
n2=input("Enter the nodes")
l1.append(n1,n2)
l1.display()
