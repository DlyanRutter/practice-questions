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
          
    def is_numerical(self, new):
        """
        used to append new element objects to numerical lists. Will only
        accept elements that have numerical values either int or float
        """
        
        if isinstance(new, Element)==True:
            if isinstance(new.value,int)==True or\
               isinstance(new.value,float)==True:
                return True
            else:
                print" 'new' must be an Element object with type int or float"
                              
        else:
            print " 'new' must be an Element object"
        return False

    def append_number(self, new):
        """
        appends a number element to a link list composed exclusively of
        numerical elements
        """
        if self.is_numerical(self,new) == True:
            self.append(self, new)
        else:
            return

    def list_print(self):
        """prints a linked list"""
        thing = self.head
        blank = []
        while thing:
            blank.append(thing.value)
            thing = thing.next
        print blank
    
    def delete(self, key, first_only=False):
        """
        Deletes an element object from a linked list if the element object's
        value = key. If first_only is set to True, only the first link found
        with that value will be deleted, else, all elements with that value
        will be deleted. Runtime complexity is O(n), memory is O(1)
        """
        current = self.head
        if current.value == key:
            self.head = current.next
            
        while current.next:
            if current.next.value == key:
                current.next = current.next.next
                if first_only==True:
                    return
                else:
                    continue
            current = current.next

def get_length(ll):
    """
    Gets the length of a linked list. Time complexity is O(n), and memory
    complexity is O(1)
    """
    list_length = 0
    current = ll.head
    while current != None:
        current = current.next
        list_length += 1
    return list_length

def intersect(ll1, ll2):
    """
    Given two linked lists (self.ll and ll2), find out if they intersect
    and return the value of intersection. Runtime complexity is O(m+n)
    where m is the length of the self.ll and n is the length of ll2. Memory
    complexity is O(1). Works by turning ll1 and ll2 into new lists, each
    of the same size (new_ll1_start and new_ll2_start) and runs along them
    both simultaneously comparing values. Must be the same value at the
    same index to be considered an intersection.
    """
    new_ll1_start = None
    new_ll2_start = None

    ll1_length = get_length(ll1)  
    ll2_length = get_length(ll2)
    difference = 0

    if ll1_length >= ll2_length:
        difference = ll1_length - ll2_length
        new_ll1_start = ll1.head
        new_ll2_start = ll2.head        
    else:
        difference = ll2_length - ll1_length
        new_ll1_start = ll2.head
        new_ll2_start = ll1.head

    while difference > 0:
        new_ll1_start = new_ll1_start.next
        difference-=1
    
    while new_ll1_start != None:
        if new_ll1_start.value == new_ll2_start.value:
            return new_ll1_start.value        
        new_ll1_start = new_ll1_start.next
        new_ll2_start = new_ll2_start.next

    return False

def reverse_single_ll(ll, printt=True):
    """
    Takes as input a single linked list object composed of element objects e.g.
    [[3, 21, 4], ['daf', 34], ['paf', 'fa', (65, 5)], ('saf', 'dasf', 23), Null]
    list_to_do points to the start of the remaining list following the head e.g.
    [['daf', 34], ['paf', 'fa', (65, 5)], ['saf', 'dasf', 23], [Null]]
    reversed_list starts as head and points to null value e.g. [[3,21,4],Null]
    temp starts as list_to_do e.g. ['daf', 34] and points to end of start list.
    list_to_do then moves one further e.g. ['paf', 'fa', (65, 5)],
    temp.next becomes head e.g. [[3,21,4], null], reversed_list becomes temp
    taking temp.next into consideration e.g. ['daf',34],[3,21,4][null]
    Runtime complexity is Linear, O(n). Memory complexity is constant, O(1)
    setting printt to True will return a list representation of the reversed
    linked list. Setting to False will return an element with property
    "element.next"
    
    """
    head = ll.head
    reversed_list = []
    if head == None or head.next == None:
        return head

    new_ll = LinkedList()
    node_to_do = head.next 
    reversed_list_end = head 
    reversed_list_end.next = None

    while node_to_do != None:
        temp = node_to_do 
        node_to_do = node_to_do.next                        
        temp.next = reversed_list_end
        reversed_list_end = temp
        
    if printt == True:
        while reversed_list_end.next:
            reversed_list.append(reversed_list_end.value)
            reversed_list_end = reversed_list_end.next
        reversed_list.append(ll.head.value)   
        print reversed_list
        
    return reversed_list_end

def remove_ll_duplicates(linked):
    """
    remove objects with values that are already present in a linked list
    runtime is O(n), memory is O(n) because you have to make the set AKA
    hashtable
    """
    if linked == None:
        return linked

    exists = set()
    exists.add(linked.head.value)
    current = linked.head
    
    while current.next != None:
        
        if current.next.value in exists:
            current.next = current.next.next
        else:
            exists.add(current.next.value)
            current = current.next
    return linked

def insertion_sort_helper(head, node):
    """
    Helper function for insertion_sort. Head is the head of the linked_list,
    and node is the node to be inserted. Works by transferring values from
    one list to a new one, placing them in order as they switch.
    """
    if node == None:
        return head

    if head == None or node.value <= head.value:
        node.next = head
        return node

    current = head
    while current.next != None and current.next.value < node.value:
        current = current.next
        
    node.next = current.next
    current.next = node
    return head

def insertion_sort(ll):
    """
    Main insertion sort function. Takes a linked list as input and outputs a
    linked list sorted by numericall value (low to high). Works by first
    initiating a new linked list with initial value of None. Then inserts
    the current value into new linked list using helper function recursively.
    Runtime is O(n^2), and memory is O(1)
    """
    head = ll.head
    sorted = None
    current = head
    
    while current != None:
        temp = current.next
        sorted = insertion_sort_helper(sorted, current)
        current = temp
        
    return sorted

def split_in_half(head, first_second):
    """
    Splits a linked list in half. head argument is the head of a ll, and
    I'm pretty sure first_second is LinkedList with two elements
    """
    if head == None:
        first_second.first = None
        first_second.second = None
        return

    elif head.next == None:
        first_second.first = head
        first_second.second = None

    else:
        slow = head
        fast = head.next

        while fast != None:
            fast = fast.next

            if fast != None:
                fast = fast.next
                slow = slow.next
                
        first_second.first = head
        first_second.second = slow.next
        slow.next = None

def merge_sorted_lists(first, second):
    """
    Merge sort helper function. Takes two separate Element objects
    as arguments
    """
    if first == None:
        return second
    
    if second == None:
        return first

    new_head = None
    if first.value <= second.value:
        new_head = first
        first = first.next
    else:
        new_head = second
        second = second.next

    new_current = new_head
    while first != None and second != None:       
        temp = None
        if first.value <= second.value:
            temp = first
            first = first.next
        else:
            temp = second
            second = second.next

        new_current.next = temp
        new_current = temp

    if first != None:
        new_current.next = first
    elif second != None:
        new_current.next = second

    return new_head
        
def merge_sort(head):
    """
    Used to sort a linked list. Works by splitting an input list into
    two halves repeatedly until there are either 0 or 1 Element objects.
    We then merge sorted linked lists and keep doing it until we have
    a completely sorted linked list. Runtime complexity is O(nlog(n)).
    Memory complexity is O(log(n))
    """

    if head == None or head.next == None:
        return head

    first_second = LinkedList((None,None))
    split_in_half(head, first_second)

    first_second.first = merge_sort(first_second.first)
    first_second.second = merge_sort(first_second.second)

    return merge_sorted_lists(first_second.first, first_second.second)

def merge_sorted_ll_heads(head1, head2):
    """
    merges two linked lists which are already sorted. Works by iterating
    over both lists simultaneously and adding the lesser value to a
    new list. Runtime complexity is O(m + n) where m and n are lengths
    of both linked lists. Memory is O(1). This one takes as input two
    heads.
    """
    if head1 == None:
        return head2
    if head2 == None:
        return head1
        
    mergedHead = None
    if head1.value <= head2.value:
        mergedHead = head1
        head1 = head1.next
    else:
        mergedHead = head2
        head2 = head2.next
    
    mergedTail = mergedHead
    while head1 != None and head2 != None:
        temp = None
        if head1.value <= head2.value:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next
    
    mergedTail.next = temp
    mergedTail = temp
    
    if head1 != None:
        mergedTail.next = head1
    elif head2 != None:
        mergedTail.next = head2
    
    return mergedHead

def merge_sorted_ll(ll1,ll2):
    """
    given two sorted linked lists, merge them. works by comparing 
    head values one at a time. memory consumption is O(1). runtime
    complexity is O(m + n) where m and n are the lengths of ll1 
    and ll2 respectively. This one takes as input two linked lists
    """
    head1 = ll1.head
    head2 = ll2.head    
    
    if head1 == None:
        return head2
    elif head2 == None:
        return head1

    merged_head = None
    
    if head1.value <= head2.value:
        merged_head = head1
        head1 = head1.next
    else:
        merged_head = head2
        head2 = head2.next
        
    merged_tail = merged_head    
    while head1 != None and head2 != None:       
        temp = None
        if head1.value <= head2.value:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        merged_tail.next = temp
        merged_tail = temp
    
    if head1 != None:
        merged_tail.next = head1 
    else:
        merged_tail.next = head2
        
    return merged_head

ll1 = LinkedList()
numll = LinkedList()
numll2 = LinkedList()
aaa = Element(14)
bbb = Element(26)
ccc = Element(90)
ddd = Element(200)
eee = Element(330)

r = [aaa, bbb, ccc, ddd, eee]

for o in r:
    numll2.append(o)

bb = Element(24)
cc = Element(325)
dd = Element(342)
aa = Element(87)
numll.append(bb)
numll.append(aa)
numll.append(cc)
numll.append(dd)
#numll.append(Element(325))
#numll.append(Element(93))

#a, b, c, d ARE EACH ONE INSTANCE OF ELEMENT CLASS
a = Element((3,21,4))
b = Element(('daf', 34))
c = Element(('paf', 'fa', (65, 5)))
d = Element(94)
e = Element(('da1f', 34))
f = Element((12, 23))
g = Element(('paf', 'fa', (65, 5)))
h = Element(('saf','dasf',23))

#APPENDING INSTANCES ABC FROM CLASS ELEMENT TO A SINGLE LINKED LIST INSTANCE
q = [a,b,c,d,e,f,g, h]
for z in q:
    ll1.append(z)
visualize = []
