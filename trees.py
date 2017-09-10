class Node(object):
    """
    creates node objects to be used in tree classes
    """

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.payload = value
        self.left = left
        self.right = right
        self.parent = parent
        self.key = key

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
        

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
        key is found, the value in the payload is returned.
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
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
            return self._get(key, currentNode, leftChild)
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

    def delete(self, key):
        """
        first use _get method to find the key we need to delete. If the tree
        only has one node, we are removing the root of the tree
        """
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
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

    def _delNoChildren(self, currentNode):
        """
        helper function for removing node. this one accounts for a situation
        in which there are no children AKA the node is a leaf.
        """
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

    def _delOneChild(self, currentNode):
        """
        helper function deletes from a branch with one child
        """
        if currentNode.hasLeftChild():
            if currentNode.isLeftChild():
                currentNode.leftChild.parent = currentNode.parent
                currentNode.parent.leftChild = currentNode.leftChild
            elif currentNode.isRightChild():
                currentNode.leftChild.parent = currentNode.parent
                currentNode.parent.rightChild = currentNode.leftChild
            else:
                currentNode.replaceNodeData(currentNode.leftChild.key,
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
              currentNode.replaceNodeData(currentNode.rightChild.key,
                                 currentNode.rightChild.payload,
                                 currentNode.rightChild.leftChild,
                                 currentNode.rightChild.rightChild)

    def _delTwoChild(self, currentNode):
        """
        helper function for deleting nodes if there are two children already.
        """
        pass
        
    def delete_tree(self):
        self.root = None

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node != None:
            self._print_tree(node.left)
            print str(node.value) + ' '
            self._print_tree(node.right)
