class Node(object):
    """
    creates node objects to be used in tree classes
    """
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.key = key

    def hasLeftChild(self):
        """
        returns True if a node has a left child
        """
        return self.leftChild

    def hasRightChild(self):
        """
        returns True if a node has a right child
        """
        return self.rightChild

    def isLeftChild(self):
        """
        returns True if a node is a left child
        """
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        """
        returns True if a node is a right child.
        """
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        """
        returns True if a node is the tree's root
        """
        return not self.parent

    def isLeaf(self):
        """
        returns True if a node is a tree's leaf
        """
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        """
        returns True if a node has any children
        """
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        """
        returns True if a node has two children
        """
        return self.rightChild and self.leftChild

    def replaceData(self, key, value, lc, rc):
        """
        replaces data at a given node
        """
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        """
        successor is the node that has the next largest key in the tree. e.g.
        with tree.  ===============17===============
                 =5=                               =35=
            =====   =====                     =====     ====
            2           =11=                  29            38
                    ====    =====
                  =9=           16
               ====
               =7=
                  ===
                     8
        say you wanted to delete node 5. the successor of node five is 7. if
        node has a right child, then the successor is the smallest key following
        the right child. if the node has no right child and is the left child of
        its parent, then the parent is the successor. if the node is the right
        child of its parent and it has no right child, then the successor is
        the successor of the parent, excuding the current node.
        """
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        """
        finds the node with minimum value in a true
        """
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        """
        makes necessary modifications to surrounding nodes when deleting
        """
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.LeftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
        

class Binary(object):
    """
    functions for binary search trees
    """
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        """
        returns the length of a binary tree
        """
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def get_root(self):
        """
        returns the root of a tree
        """
        return self.root

    def put(self, key, val):
        """
        starting at tree root, search tree comparing the new key to the key in
        the current node. If the new key is less than the current node, search
        the left subtree, otherwise search the right. When there is no left or
        right child to search, we have found the position in the tree where the
        new node should be installed. To add a node to the tree, create a new
        Node object at the point discovered.
        """
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = Node(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        """
        if key is less than the current node's key and if the current node has
        a left child, call _put function again turning the input value for
        currentNode into the parent. if key > currentNode.key and currentNode
        has a right child, call the function again, but use currentNode.right
        Otherwise, create a new rightChild object, making its parent currentNode
        """
        if key == currentNode.key:
            currentNode.value = val
            return

        elif key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = Node(key, val, parent = currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = Node(key, val, parent = currentNode)

    def __setitem__(self, key, value):
        """
        overloads the [] operator for assignment. Allows us to write python
        statements like myZipTree['Plymouth'] = 187, just like in a dict
        """
        self.put(key, value)

    def get(self, key):
        """
        searches tree recursively until it gets to a matching key. When the
        key is found, returns the Node object # the payload is returned.
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res#.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        """
        helper function for recursive search, returns the Node object
        rather than just a value
        """
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self,key):
        """
        can write a python statement that looks like we are accessing something
        in a dictionary e.g. z = myZipTree['Fargo']
        """
        return self.get(key)

    def __contains__(self,key):
        """
        calls get and returns true if get returns a value or false if it
        returns none. __contains__ overloads the in operator and allows us
        to write statements like if "Northfield" in myZipTree: print 'yay'
        """
        if self._get(key,self.root):
            return True
        else:
            return False

    def _delNoChildren(self, currentNode):
        """
        helper function for removing node. this one accounts for a situation
        in which there are no children AKA the node is a leaf. in this case,
        all we need to do is delete the node and remove the referce to this
        node in the parent.
        """
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

    def _delOneChild(self, currentNode):
        """
        helper function deletes from a branch with one child. we promote the
        child to take the place of its parent. if current is a left child, then
        we update the parent reference of the left child to point to the parent
        of current, and then update left child of the parent to point to the
        current node's left child. similar process with right. if current has
        no parent, it is the root, so we replace the key, payload, leftchild
        and right child by calling replaceData
        """
        if currentNode.isLeaf() == False:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceData(currentNode.leftChild.key,
                                            currentNode.leftChild.payload,
                                            currentNode.leftChild.leftChild,
                                            currentNode.leftChild.rightChild)
            else:
                 if currentNode.isLeftChild():
                     currentNode.rightChild.parent = currentNode.parent
                     currentNode.parent.leftChild = currentNode.rightChild
                 elif currentNode.isRightChild():
                     currentNode.rightChild.parent = currentNode.parent
                     currentNode.parent.rightChild = currentNode.rightChild
                 else:
                     currentNode.replaceData(currentNode.rightChild.key,
                                        currentNode.rightChild.payload,
                                        currentNode.rightChild.leftChild,
                                        currentNode.rightChild.rightChild)

    def _delTwoChild(self, currentNode):
        """
        helper function for deleting nodes if there are two children already.
        searches the tree for a node that can be used to replace the one to be
        deleted. that node preserves the binary search tree relationships for
        both of the existing left and right subtrees. the node that will do this
        is the next largest node in the tree AKA the successor. successor has
        no more than one child, so we remove it and put it in the tree in place
        of the node to be deleted. findSuccessor() and splice out are functions
        in the Node class. function works by finding the successor of the curr
        Node and then removing it. you then change the value of curretNode's
        key and payload.
        """
        if currentNode.hasAnyChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
            self._delNoChildren(currentNode)

    def _remove(self, currentNode):
        """
        removes a node having a given key from a tree helper function
        """
        if currentNode.hasAnyChildren == False:
            self._delNoChildren(currentNode)
        elif currentNode.hasBothChildren:
            self._delTwoChild(currentNode)
        elif (currentNode.hasRightChild() and not currentNode.hasLeftChild()) or\
             (currentNode.hasLeftChild() and not currentNode.hasRightChild()):
            self._delOneChild(currentNode)


    def delete(self, key):
        """
        first use _get method to find the key we need to delete. If the tree
        only has one node, we are removing the root of the tree.
        """
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self._remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1

        else:
            raise KeyError('Error, key not in tree')        
    
    def __delitem__(self,key):
        """
        changes del operator I think
        """
        self.delete(key)
        
    def delete_tree(self):
        """
        deletes an entire tree
        """
        self.root = None

    def print_tree(self):
        """
        prints a tree
        """
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        """
        print_tree helper function
        """
        if node != None:
            #if node.leftChild:
            self._print_tree(node.leftChild)
            print str(node.payload) + ' '
            self._print_tree(node.rightChild)

tree = Binary()
tree[13] = "red"
tree[16] = "blue"
tree[15] = "yellow"
tree[17] = "green"
tree[18] = "pink"
tree[2] = "at"

#print (tree[6].payload)
#print (tree[18].payload)
#tree.delete(18)
#tree.delete(2)
#tree.print_tree()

