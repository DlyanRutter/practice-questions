class Element(object):
    """
    used to set up individual linked list node objects
    """
    def __init__(self, value=None, data=None):
        self.data = data
        self.value = value
        self.next = None
        self.first = None
        self.second = None

class Pointer(object):
    """
    creates pointers for splitting linked lists I guess
    """
    def __init__(self):
        self.first = None
        self.second = None

class LinkedList(object):
    """
    used to set up linked lists
    """
    def __init__(self, head=None):
         self.head = head
         self.first = None
         self.second = None
        
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

def split_in_half(head, first_second):
    """
    I'm pretty sure first_second is a tuple of Elements starting at
    value (None, None)
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

def merge_sorted(ll1, ll2):
    """
    merges two sorted linked lists. ll1 and ll2 are linked lists. runtime
    complexity is O(m + n) where m and n are the lengths of the lists. Memory
    complexity is O(1)
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
    elif head2 != None:
        merged_tail.next = head2

    return merged_head
            
        
def merge_sort(head):

    if head == None or head.next == None:
        return head

    first_second = LinkedList((None,None))
    split_in_half(head, first_second)

    first_second.first = merge_sort(first_second.first)
    first_second.second = merge_sort(first_second.second)

    return merge_sorted_lists(first_second.first, first_second.second)

   


ll1 = LinkedList()
numll = LinkedList()
numll2 = LinkedList()
numll3 = LinkedList()

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


aaaaa = Element(333)
bbbbb = Element(187)
ccccc = Element(69)
ddddd = Element(98)

u = [aaaaa, bbbbb, ccccc, ddddd]
for y in u:
    numll3.append(y)

#n = swap_nth_node(ll1, 5)
#print reverse(ll1)
#insertion_sort(numll)

n = merge_sort(aaa)
"""
aaa = insertion(numll)#merge_sort(aaaaa)

while aaa:
    if aaa.next:
        visualize.append(aaa.value)
        aaa = aaa.next
    else:
        visualize.append(aaa.value)
        break

print visualize
"""
