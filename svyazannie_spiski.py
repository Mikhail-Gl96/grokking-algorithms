import copy
import random


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = f'LinkedList[\n{current.value}\n'
            while current.next != None:
                current = current.next
                out += f'{current.value}\n'
            return f'{out}]'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def Len(self):
        self.length = 0
        if self.first != None:
            self.length += 1
            current = self.first
            while current.next != None:
                current = current.next
                self.length += 1
        return self.length

    def Push(self, x):
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        else:
            self.first = Node(x, self.first)


    def add(self, x):
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def InsertNth(self, i, x):
        if (self.first == None):
            self.first = Node(x, self.first)
            self.last = self.first.next
            return
        if i == 0:
            self.first = Node(x, self.first)
            return
        curr = self.first
        count = 0
        while curr != None:
            if count == i - 1:
                curr.next = Node(x, curr.next)
                if curr.next.next == None:
                    self.last = curr.next
                break
            curr = curr.next

    def Pop(self):
        oldhead = self.first
        if oldhead == None:
            return None
        self.first = oldhead.next
        if self.first == None:
            self.last = None
        return oldhead.value

    def Del(self, i):
        if (self.first == None):
            return
        old = curr = self.first
        count = 0
        if i == 0:
            self.first = self.first.next
            return
        while curr != None:
            if count == i:
                if curr.next == self.last:
                    self.last = curr
                    break
                else:
                    old.next = curr.next
                break
            old = curr
            curr = curr.next
            count += 1

    def SortedInsert(self, x):
        if (self.first == None):


L = LinkedList()
L.add(1)
L.add(2)
L.add(3)
[L.add(i) for i in range(5, 9)]

print(L)
