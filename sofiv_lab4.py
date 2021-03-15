"""
Lab 4 - Red Black Tree
Author: Sofi Vinas
Date: March 5th, 2021
Description: Red-Black Tree Implementation
Notes:
    1. Edited the Sentinel class to inherit from RBNode class, to access some functions
"""
from mealticket import *

#============================== Aux Classes ====================================

class RBNode():
    """ This class implements a node for the RBT. """
    def __init__(self, ticket):
        """
        Description: The constructor for the Node class.
        Inputs: A valid MealTicket (input validation should be done by insert)
        """
        self._parent = Sentinel()
        self._leftChild = Sentinel()
        self._rightChild = Sentinel()
        self._value = ticket
        self._key = ticket.ticketID
        self._color = "red"

    def __str__(self):
        """ Returns a string rep of the node (for debugging ^,^) """
        returnValue = "Node: {}\n".format(self._key, self._color)
        returnValue += "Parent: {}\n".format(self._parent._key)
        returnValue += "Left Child: {}\n".format(self._leftChild._key)
        returnValue += "Right Child: {}\n".format(self._rightChild._key)
        return returnValue

    def isSentinel(self):
        """ A helper method for figureing out if a node is a Sentinel """
        return False

    #Accessor Methods
    def getColor(self):
        """
        Description: This method returns the color.
        """
        return self._color

    def getParent(self):
        """
        Description: Accessor method for the Node. Returns parent.
        """
        return self._parent


    def getRChild(self):
        """
        Description: Accessor method for the Node. Returns right child.
        """
        return self._rightChild

    def getLChild(self):
        """
        Description: Accessor method for the Node. Returns left child.
        """
        return self._leftChild

    def getValue(self):
        """
        Description: Accessor method for the Node. Returns the MealTicket.
        """
        return self._value

    # Mutator methods
    def setParent(self, node):
        """
        Description: Mutator method. Sets the parent reference.
        Input: A Node() reference.
        """
        self._parent = node

    def setLChild(self, node):
        """
        Description: Mutator method. Sets the lchild reference.
        Input: A Node() reference.
        """
        self._leftChild = node

    def setRChild(self, node):
        """
        Description: Mutator method. Sets the rchild reference.
        Input: A Node() reference.
        """
        self._rightChild = node

    def setColor(self, color):
        """
        Description: This method sets the color
        """
        self._color = color

    #comparison operators
    def __gt__(self, other):
        """
        Description: Overloads the > operator to allow direct comparison of
                     nodes. Now we can do node1 > node2.
        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key > other._key
        return returnValue

    def __lt__(self, other):
        """
        Description: Overloads the < operator to allow direct comparison of
                     nodes. Now we can do node1 < node2.
        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key < other._key
        return returnValue

    def __eq__(self, other):
        """
        Description: Overloads the == operator to allow direct comparison of
                     nodes. Now we can do node1 == node2.
        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key == other._key
        return returnValue

    def __ne__(self, other):
        """
        Description: Overloads the != operator to allow direct comparison of
                     nodes. Now we can do node1 != node2.
        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key != other._key
        return returnValue

    def __le__(self, other):
        """
        Description: Overloads the <= operator to allow direct comparison of
                     nodes. Now we can do node1 <= node2.
        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key <= other._key
        return returnValue

    def __ge__(self, other):
        """
        Description: Overloads the >= operator to allow direct comparison of
                     nodes. Now we can do node1 >= node2.
        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key >= other._key
        return returnValue

    #Some helper methods to make things easy in the BST
    def hasLeftChild(self):
        """
        Description: This method returns true if the current node
                     has a left child
        """
        returnValue = False
        cond1 = not self._leftChild.isSentinel()
        cond2 = self._leftChild._parent is self
        if(cond1 and cond2):
                returnValue = True
        return returnValue

    def hasRightChild(self):
        """ This method returns true|false depending on if the current
            node has a right child or not."""
        returnValue = False
        cond1 = not self._rightChild.isSentinel()
        cond2 = self._rightChild._parent is self
        if(cond1 and cond2):
                returnValue = True
        return returnValue

    def hasOnlyOneChild(self):
        """ Returns True if the current node has only one child."""
        LC = self.hasLeftChild()
        RC = self.hasRightChild()
        return (LC and not RC) or (not LC and RC)

    def hasBothChildren(self):
        """ Returns True if the current node has both children"""
        return self.hasLeftChild() and self.hasRightChild()

    def isLeaf(self):
        """ Returns true if the current node is a leaf node."""
        returnValue = False
        if(self._rightChild.isSentinel() and self._leftChild.isSentinel()):
            returnValue = True
        return returnValue

    def isLeftChild(self):
        """Returns true if the current node is a left child"""
        cond1 = not self._parent.isSentinel()
        cond2 = self._parent._leftChild is self
        cond3 = self._parent._rightChild is not self
        return cond1 and cond2 and cond3

    def isRightChild(self):
        """Returns true if the current node is a right child"""
        cond1 = not self._parent.isSentinel()
        cond2 = self._parent._rightChild is self
        cond3 = self._parent._leftChild is not self
        return cond1 and cond2 and cond3
#===============================================================================
class Sentinel(RBNode):
    """This class builds the Sentinel nodes"""

    def __init__(self):
        """The constructor for the Sentinel class"""
        self._key = None
        self._value = None
        self._leftChild = None
        self._rightChild = None
        self._parent = None
        self._color = "black"

    def isSentinel(self):
        """ This method makes it easy to check if a given node is a Sentinel"""
        return True

        # Accessor Methods
        # Accessor Methods
#Accessor Methods
    def getColor(self):
        """
        Description: This method returns the color.
        """
        return self._color




class RedBlackTree:
    """ Skeleton code for the red-black tree"""


    def __init__(self):
        """ The constructor for the red-black tree
        Running time is O(1)
        """
        self._root = Sentinel()
        self._treeHeight = 0
        self.output = ""

    def colorPrint(self, node):
        if(not node.isSentinel()):
            self.output += "{" + str(node._key) + ","+ str(node._color) + "}" + ", "
            self.colorPrint(node.getLChild())
            self.colorPrint(node.getRChild())

    def _isRoot(self, node):
        """
        Description: This function returns true if the given node is the root.
        """
        return node is self._root

    def _isEmpty(self):
        """
        Description: This method returns true if the tree is empty, else False.
        """
        return self._root.isSentinel()

    def _isValid(self, ticket):
        """
        Description: A method for checking if the given ticket is a valid
                     mealticket.
        Inputs: Some object in the variable ticket.
        Outputs: Boolean (True|False) depending on if it is a valid mealticket.
        """
        return type(ticket) == MealTicket

    def _transplantR(self, cNode):
        """
        Description: This transplant attaches the currentNodes right child
                     to the current nodes parent.
        Notes:
                1. Do not call this method when cNode is the root.
                2. Don't forget to handle the cNodes references in your func.
        """
        parent = cNode.getParent()
        child = cNode.getRChild()
        if(cNode.isLeftChild()):
            parent.setLChild(child)
            child.setParent(parent)
        else:
            parent.setRChild(child)
            child.setParent(parent)

    def _transplantL(self, cNode):
        """
        Description: This transplant attaches the currentNodes right child
                     to the current nodes parent.
        Notes:
                1. Do not call this method when cNode is the root.
                2. Don't forget to handle the cNodes references in your func.
        """
        parent = cNode.getParent()
        child = cNode.getLChild()
        if(cNode.isLeftChild()):
            parent.setLChild(child)
            child.setParent(parent)
        else:
            parent.setRChild(child)
            child.setParent(parent)


    def traverse(self, mode):
        """
        Description: The traverse method returns a string rep
                     of the tree according to the specified mode
        """
        self.output = ""
        if(type(mode) == str):
            if(mode == "in-order"):
                self.inorder(self._root)
            elif(mode == "pre-order"):
                self.preorder(self._root)
            elif(mode == "post-order"):
                self.postorder(self._root)
            elif(mode == "color-print"):
                self.colorPrint(self._root)
        else:
            self.output = "  "
        return self.output[:-2]

    def inorder(self, node):
        """ computes the inorder traversal """
        if(not node.isSentinel()):
            self.inorder(node.getLChild())
            self.output += str(node._key) + ", "
            self.inorder(node.getRChild())

    def preorder(self, node):
        """computes the pre-order traversal"""
        if(not node.isSentinel()):
            self.output += str(node._key) + ", "
            self.preorder(node.getLChild())
            self.preorder(node.getRChild())

    def postorder(self, node):
        """ compute postorder traversal"""
        if(not node.isSentinel()):
            self.postorder(node.getLChild())
            self.postorder(node.getRChild())
            self.output += str(node._key) + ", "

    def _findMinimum(self, node):
        """
        Description: Finds the minimum child of a tree when given a node.
        Inputs: A node from the BST.
        Outputs: The minumum node from the sub-tree (e.g the left-most child).
        """
        returnValue = False
        if not node.isSentinel():
            returnValue = node
            while not returnValue.getLChild().isSentinel():
                returnValue = returnValue.getLChild()
        return returnValue

    def _findSuccessor(self, node):
        """
        Description: Given a node, returns the successor of that node,
                     or False if there is no successor.
        """
        succ = False
        # if node has a right child
        if(node.hasRightChild()):
            # then successor is the min of the right subtree
            succ = self._findMinimum(node._rightChild)
        # node has no right child, but has a parent
        elif(node.getParent().isSentinel()):
            if(node.isLeftChild()): # node is a left child
                succ = node.getParent() # then succ is the parent
            else: # node is right child, and has not right child
                succ = node.getParent()
                while not succ.getParent().isSentinel() and node.isRightChild():
                    node = succ
                    succ = succ.getParent()
        return succ

    #=========================== Manditory Methods =============================
    #You write these. I will update with BST solution on saturday.
    def find(self, ticketID):
        """ Hints: This method returns either a stored mealticket or False
                   just like in the BST lab. Start at the root then make
                   your way to the RBNode whose ticketID matches the input.
                   Then return the value of that node.
            Running time is O(lg(n))
            Valid input: A positive integer. Return False on invalid input
        """
        ret = False
        if(type(ticketID) == int and ticketID > 0):
            currentNode = self._root
            while(not currentNode.isSentinel()):
                if(currentNode._key == ticketID):
                    ret = currentNode.getValue()
                    break
                elif(ticketID < currentNode._key):
                    currentNode = currentNode.getLChild()
                else:
                    currentNode = currentNode.getRChild()
        return ret

    #TODO #Call delete fixup at each of the if else statements
    def delete(self, ticketID):
        """ The delete method starts out the same as BST but then you need
            to restructure your RBT.
            Running time is O(lg(n))
            Valid input: A positive integer. Return False on invalid input
            Description: Remove a MealTicket from the tree. Check to see if the
            tree breaks any of the red-black properties (to which we call deleteFixup).
            If so, perform appropriate rotations, and or recolorings.
        """

        ret = False
        if(type(ticketID) == int and ticketID > 0):
            currentNode = self.findNode(ticketID) #changed from self._find(ticketID)
            originalColor = currentNode.getColor()
            if(type(currentNode) == RBNode):
                ret = True
                #Step-02: If the node is a leaf - just delete it
                if(currentNode.isLeaf()): #parent replaces leaf, call deleteFixup on parentb
                    parent = currentNode.getParent()
                    new = Sentinel()
                    if(currentNode is self._root):
                        self._root = new

                    elif(currentNode.isLeftChild()):
                        parent.setLChild(new)
                        new._parent = parent
                    else:
                        parent.setRChild(new)
                        new._parent = parent
                    currentNode.setParent(None)
                    currentNode.setLChild(None)
                    currentNode.setRChild(None)
                    if (originalColor == "black"):
                        self.deleteFixup(new)

                #Step-02: If the node has only one child then transplant
                elif(currentNode.hasOnlyOneChild()):
                    if(currentNode.hasLeftChild()):
                        child = currentNode.getLChild()
                        #transplant left
                        if(currentNode is self._root):
                            self._root = currentNode.getLChild()
                        else:
                            self._transplantL(currentNode) #changed from currentNode
                            # this line may need to change

                    else:
                        child = currentNode.getRChild()
                        #transplant right
                        if(currentNode is self._root):
                            self._root = currentNode.getRChild()
                        else:
                            self._transplantR(currentNode) #changed from currentNode

                    currentNode.setParent(None)
                    currentNode.setLChild(None)
                    currentNode.setRChild(None)
                    # this line may need to change
                    #child is either current nodes left or right child
                    if(originalColor == "black"):
                        self.deleteFixup(child)


                #Step-03: If the node has both children - Find successor
                else:
                    successor = self._findSuccessor(currentNode)

                    self.delete(successor._key) #takes ticketID
                    currentNode._value = successor._value
                    currentNode._key = successor._key
                    # this line may need to change


        return ret



    #TODO #fix up tree after insertion (at the end) DONE
    def insert(self, ticket):
        """
        Hints: add a key to the tree. Don't forget to fix up the tree
        and balance the nodes.
        Running time is O(lg(n)).
        Valid input: An object of type: MealTicket. Return False on invalid input.
        """
        ret = False
        if(self._isValid(ticket)):
            newNode = RBNode(ticket) #the node is set to RED
            ret = True
            if(self._root.isSentinel()): #if its the sentinel, set to BLACK
                self._root = newNode
                self._root.setColor("black")
            else:
                currentNode = self._root
                while(not currentNode.isSentinel()):
                    if(newNode <= currentNode):
                        lChild = currentNode.getLChild()
                        if(lChild.isSentinel()):
                            currentNode.setLChild(newNode)
                            newNode.setParent(currentNode)
                            currentNode = Sentinel()
                        else:
                            currentNode = lChild
                    else:
                        rChild = currentNode.getRChild()
                        if(rChild.isSentinel()):
                            currentNode.setRChild(newNode)
                            newNode.setParent(currentNode)
                            currentNode = Sentinel()
                        else:
                            currentNode = rChild


                #THIS LINE MAY OR MAY NOT BE CORRECT
                self.insertFixup(newNode)
        return ret

    #========================== Additional Methods =============================
    #I think these are useful. Implement them if you want.
    def findNode(self, ticketID): #just liike bst
        """
        Hints: This method finds a node and returns it or
               false if no node is found. First do a BST search for the RBNode
               with the same key as the input ticketID. Then return that node.
        """
        #will at some point be sentinel that has none of the methods you want to call with it
        #similar to find but returns a node (used internally for find sucessor
        # and delete). Same steps as above, just return currentNode
        ret = False
        if type(ticketID) is int and ticketID > 0:
            current = self._root  # current equal to root
            while True:
                if current._key == ticketID:
                    ret = current  # THIS IS THE ONLY LINE THAT CHANGES
                    break
                if current.isSentinel():
                    break
                if ticketID < current._key:
                    if current.hasLeftChild():  # check for left
                        current = current.getLChild()
                    else:
                        break
                if ticketID > current._key:
                    if current.hasRightChild():
                        current = current.getRChild()
                    else:
                        break
        return ret

    #TODO: DONE
    def insertFixup(self, currentNode):
        """Hint: write a function to balance your tree after inserting"""
        #Using the book pseudocode
        while(currentNode.getParent().getColor() == "red"):
            if currentNode.getParent().isLeftChild():
                uncle = currentNode.getParent().getParent().getRChild()
                if uncle.getColor() == "red":
                    uncle.setColor("black")
                    currentNode.getParent().setColor("black")
                    currentNode.getParent().getParent().setColor("red")
                    currentNode = currentNode.getParent().getParent()
                else:
                    if currentNode.isRightChild():
                        currentNode = currentNode.getParent()
                        self.leftRotate(currentNode)
                    currentNode.getParent().setColor("black")
                    currentNode.getParent().getParent().setColor("red")
                    self.rightRotate(currentNode.getParent().getParent())
            else:
                uncle = currentNode.getParent().getParent().getLChild()
                if uncle.getColor() == "red":
                    uncle.setColor("black")
                    currentNode.getParent().setColor("black")
                    currentNode.getParent().getParent().setColor("red")
                    currentNode = currentNode.getParent().getParent()
                else:
                    if currentNode.isLeftChild():
                        currentNode = currentNode.getParent()
                        self.rightRotate(currentNode)
                    currentNode.getParent().setColor("black")
                    currentNode.getParent().getParent().setColor("red")
                    self.leftRotate(currentNode.getParent().getParent())


        self._root.setColor("black")


    #TODO:
    def deleteFixup(self, currentNode):
        """
        Hint: receives a node and fixes up the tree,
              balancing from that node.
        """
        while ((currentNode is not self._root) and currentNode.getColor() == "black"):
            parent = currentNode.getParent()
            # Question 1: is CurrentNode a Left Child?
            if currentNode.isLeftChild():
                sibling = parent.getRChild()

                if(sibling.getColor() == "red"):
                    sibling.setColor("black")
                    parent.setColor("red")
                    self.leftRotate(parent)
                    sibling = parent.getRChild()

                if sibling.getLChild().getColor() == "black" and sibling.getRChild().getColor() == "black":
                    sibling.setColor("red")
                    currentNode = parent

                else:
                    if(sibling.getRChild().getColor() == "black"):
                        sibling.getLChild().setColor("black")
                        sibling.setColor("red")
                        self.rightRotate(sibling)
                        sibling = parent.getRChild()

                    #No matter what- do this
                    sibling.setColor(parent.getColor())
                    parent.setColor("black")
                    sibling.getRChild().setColor("black")
                    self.leftRotate(parent)
                    currentNode = self._root
            else:
                sibling = parent.getLChild()

                if (sibling.getColor() == "red"):
                    sibling.setColor("black")
                    parent.setColor("red")
                    self.rightRotate(parent)
                    sibling = parent.getLChild()

                if sibling.getLChild().getColor() == "black" and sibling.getRChild().getColor() == "black":
                    sibling.setColor("red")
                    currentNode = parent

                else:
                    if (sibling.getLChild().getColor() == "black"):
                        sibling.getRChild().setColor("black")
                        sibling.setColor("red")
                        self.leftRotate(sibling)
                        sibling = parent.getLChild()

                    # No matter what- do this
                    sibling.setColor(parent.getColor())
                    parent.setColor("black")
                    sibling.getLChild().setColor("black")
                    self.rightRotate(parent)
                    currentNode = self._root

        currentNode.setColor("black")

    #DONE
    def leftRotate(self, currentNode):
        """ perform a left rotation from a given node"""
        """Running time is O(1)"""
        y = currentNode.getRChild() #set y
        currentNode.setRChild(y.getLChild()) #turn y's left subtree into x's right subtree
        if y.hasLeftChild(): #check to see it's NOT a leaf node
            y.getLChild().setParent(currentNode)

        y.setParent(currentNode.getParent()) #link x's parent to y
        if currentNode.getParent().isSentinel():
            self._root = y
        elif currentNode == currentNode.getParent().getLChild():
            currentNode.getParent().setLChild(y)
        else:
            currentNode.getParent().setRChild(y)

        y.setLChild(currentNode)
        currentNode.setParent(y)

    #DONE
    def rightRotate(self, currentNode):
        """ perform a right rotation from a given node, symmetric to left rotate"""
        """Running time is O(1)"""
        y = currentNode.getLChild() #set y variable
        currentNode.setLChild(y.getRChild())
        if y.hasRightChild():
            y.getRChild().setParent(currentNode)

        y.setParent(currentNode.getParent())
        if currentNode.getParent().isSentinel():
            self._root = y
        elif currentNode == currentNode.getParent().getRChild():
            currentNode.getParent().setRChild(y)
        else:
            currentNode.getParent().setLChild(y)

        y.setRChild(currentNode)
        currentNode.setParent(y)

