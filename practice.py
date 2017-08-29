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

class NumericalLinked(object):
    """
    used to make numerical linked lists
    """
    def __init__(self, head=None):
        self.head = head
        
    def is_okay(self, new):
        """
        used to append new element objects to numerical lists. Will only
        accept elements that have numerical values either int or float
        """
        
        if isinstance(new, Element)==True:
            if isinstance(new.value,int)==True or\
               isinstance(new.value,float)==True:
                return True
            else:
                return" 'new' must be an Element object with type int or float"
                              
        else:
            return " 'new' must be an Element object"
        

    def append(self, new, in_order=True):
        """
        used to append new element objects to numerical lists. Will only
        accept elements that have numerical values either int or float
        """

        if self.is_okay(new) != True:
            print self.is_okay(new)
            return

        #right now I'm trying to figure out how to add numbers so they
        #are sorted
        if new.value <= self.head:
            current = self.head
            self.head.next = current
            self.head = new
            self.head.next 
        while new.value >= current
        if self.head:
            while current.next:
                current = current.next
            current.next = new
        else:
            self.head = new

    def insertion_sort_helper(self, node):
        if node == None:
            return self.head

        if self.is_okay(node) != True:
            print self.is_okay(node)
            return
        
        if self.head == None or node.value <= self.head.value:
            node.next = self.head
            return node
        
        current = self.head
        while current.next != None and current.next.value < node.value:
            current = current.next

        node.next = current.next
        current.next = node

        return self.head

    def insertion_sort(self):
        sort = None
        current = self.head

        while current != None:
            temp = current.next
            sort = sorted_insert(sort, current)
            current = temp
        return sort
    
    def list_print(self):
        """prints a linked list"""
        thing = self.head
        blank = []
        while thing:
            blank.append(thing.value)
            thing = thing.next
        print blank

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
