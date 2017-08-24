import numpy as np


class Array(object):
    """
    used to manipulate arrays
    """
    def __init__(self, array):
        self.array = array

    def binary_search(self, key):
        """
        given a sorted array of integers return the index of the given key
        runtime = O(logn), memory complexity = O(1). At every step, consider
        the array between low and high indices. Calculate the mid index
        if mid index is key, return mid. If element at mid is > key, reduce
        the array size such that high becomes mid - 1. If element at mid is <
        key, reduce array size such that low becomes mid + 1. When low > high,
        doesn't exist. Return -1
        """
        low_index = 0
        high_index = len(self.array) - 1

        while low_index <= high_index:
            mid_index = low_index + ((high_index - low_index) / 2)

            if self.array[mid_index] == key:
                return mid_index
            
            if key < self.array[mid_index]:
                high_index = mid_index - 1
            else:
                low_index = mid_index + 1
        return -1


class Element(object):
    """
    used to set up individual linked list node objects
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    """
    used to set up linked lists
    """
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """adds element to end of a list"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def list_print(self):
        """prints a linked list"""
        thing = self.head
        blank = []
        while thing:
            blank.append(thing.value)
            thing = thing.next
        print blank


def reverse_single_ll(ll):
    """
    Takes as input a linked list object composed of element objects e.g.
    [[3, 21, 4], ['daf', 34], ['paf', 'fa', (65, 5)], ('saf', 'dasf', 23), Null]
    list_to_do points to the start of the remaining list following the head e.g.
    [['daf', 34], ['paf', 'fa', (65, 5)], ['saf', 'dasf', 23], [Null]]
    reversed_list starts as head and points to null value e.g. [[3,21,4],Null]
    temp starts as list_to_do e.g. ['daf', 34] and points to end of start list.
    list_to_do then moves one further e.g. ['paf', 'fa', (65, 5)],
    temp.next becomes head e.g. [[3,21,4], null], reversed_list becomes temp
    taking temp.next into consideration e.g. ['daf',34],[3,21,4][null]
    Runtime complexity is Linear, O(n). Memory complexity is constant, O(1)
    
    """
    head = ll.head 
    if head == None or head.next == None:
        return head

    list_to_do = head.next 
    reversed_list = head 
    reversed_list.next = None

    while list_to_do != None:
        temp = list_to_do 
        list_to_do = list_to_do.next                        
        temp.next = reversed_list
        reversed_list = temp
    return reversed_list

def remove_duplicates(ll):
    """
    remove objects with values that are already present in a linked list
    """
    head = ll.head
    if head == None or head.next == None:
        return head

    exists = set()
    exists.add(head.value)
    current = head
    
    while current.next != None:
        
        if current.next.value in exists:
            current.next = current.next.next
        else:
            exists.add((current.next.value))
            current = current.next

   return current

def test_Array():
    """
    tests array class functions
    """
    array = [1, 10, 20, 47, 59, 63, 77, 88, 99, 111]
    key = 77
    array = Array(array)
    print array.binary_search(key)
    
def test_LinkedList():
    """
    tests LinkedList class functions
    """
    ll = LinkedList()

    #a, b, c, d ARE EACH ONE INSTANCE OF ELEMENT CLASS
    a = Element([3,21,4])
    b = Element(['daf', 34])
    c = Element(['paf', 'fa', (65, 5)])
    d = Element(('saf','dasf',23))

    #APPENDING INSTANCES ABC FROM CLASS ELEMENT TO A SINGLE LINKED LIST INSTANCE
    q = [a,b,c,d]
    for e in q:
        ll.append(e)

    x = reverse_single_ll(ll)
    y = [x.value, x.next.value, x.next.next.value, x.next.next.next.value]
    print y

#test_LinkedList()
