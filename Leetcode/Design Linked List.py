
# coding: utf-8

# In[1]:


class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        node = self.head
        i = 0
        while node:
            if i != index:
                node = node.next
                i += 1
                print (i)
            else:
                return node.val
        

    def addAtHead(self, val):
        if self.head == None:
            newnode = ListNode(val)
            newnode = self.head
        else:
            newnode.next = self.head
            self.head = newnode

    def addAtTail(self, val):
        newnode = ListNode(val)
        if self.head == None:
            newnode = self.head
        else:
            node = self.head
            while node:
                if node.next:
                    node.next = newnode
                else:
                    node = node.next
                    
    def addAtIndex(self, index, val):
        newnode = ListNode(val)
        if index == 0:
            if self.head == None:
                newnode = self.head
            else:
                newnode.next = self.head
        else:
            node = self.head
            i = 0
            while node:
                if i != index:
                    temp = node
                    node = node.next
                    i += 1
                else:
                    newnode = temp.next
                    node = newnode.next
            if node == None and i == index+1:
                newnode = self.tail.next
                self.tail = newnode

    def deleteAtIndex(self, index):
        node = self.head
        i = 0
        while node:
            if i != index:
                temp = node
                node = node.next
                i += 1
            else:
                temp.next = node.next

