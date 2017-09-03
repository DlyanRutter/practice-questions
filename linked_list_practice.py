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
            if thing.next:
                thing = thing.next
            else:
                break               
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

def n_from_last(ll, n):
    """
    finds nth from last node where n is an integer. Time complexity is O(n)
    memory complexity is O(1)
    """
    if ll.head == None or n < 1:
        return None
    head = ll.head
    tail = head

    while tail != None and n > 0:
        tail = tail.next
        n -=1

    if n != 0:
        return None
    
    while tail != None:
        tail = tail.next
        head = head.next
        
    return head.value
    
def swap_nth_node(ll, n):
    """
    Makes the nth node the head of a ll, and puts the head where n once was.
    starts by bringing current out to node 'n'. Next, turns prev.next (n-1)
    into ll.head. Then creates a temp that points to the original head.next.
    Next, turns original head.next into current.next. Finally, current.next
    is set = to temp.next. Time is O(n), memory is O(1)
    """
    prev = None
    current = ll.head

    if ll.head == None or n == 1:
        return ll.head

    count = 1
    while current != None and count < n:
        prev = current
        current = current.next
        count +=1

    if current == None:
        return ll.head
    
    prev.next = ll.head
    temp = ll.head.next
    ll.head.next = current.next
    current.next = temp

    return current
