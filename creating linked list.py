class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def creation(self,n):
        i=0
        while i<n:
            newnode=Node(input("Enter Node value "))
            if i==0:
                self.head=newnode
            else:
                t=self.head
                while t.next:
                    t=t.next
                t.next=newnode
            i=i+1
    def show(self):
        x=self.head
        while x:
            print(x.val,end=" ")
            x=x.next
a=linkedlist()
b=int(input("Enter number of nodes "))
a.creation(b)
a.show()
