from mealticket import *
from sofiv_lab4 import *
from random import *

def defaultTestTickets(vals):
    """
        Generates a list of meal tickets with the provided list of values
    """
    result = []
    for i in range(len(vals)):
        ticket = MealTicket("My Meal " + str(i))
        ticket.ticketID = vals[i]
        ticket.addItem(("Test Item", round(uniform(0, 30), 2)))
        result.append(ticket)
    return result

def randomTestTickets(size):
    """
        Generates a list of random mealtickets with no duplicates
        Returns <size> mealtickets
    """
    result = []
    vals = sample(range(1, size+20), size)
    for i in range(size):
        ticket = MealTicket("My Meal " + str(i))
        ticket.ticketID = vals[i]
        ticket.addItem(("Test Item", round(uniform(0, 30), 2)))
        result.append(ticket)
    return result

def displayNodes(node):
    """
        Input: the root of your RBTree
        For every node in the tree, it will print it's relationships
        (children, parent, etc.) as well as the color.
        Useful for debugging your tree and making sure things are working
    """
    if not node.isSentinel():
        print(node)
        print(f"Color: {node.getColor()}\n")
        displayNodes(node.getLChild())
        displayNodes(node.getRChild())

def redParent(CN):
    """
        A function that checks if every node in the tree has 
        two black children if it is red 
    """
    if (not CN.isSentinel()):
        if (CN.getColor == 'red'):
            left = CN.getLChild()
            right = CN.getRChild()
            if (left.getColor() == 'red' or right.getColor() == 'red'):
                return False
        lRes = redParent(CN.getLChild())
        if (lRes == False):
            return False
        rRes = redParent(CN.getRChild())
        if (rRes == False):
            return False

    return None


def getBlackHeight(CN):
    """
        A function that checks if a tree has the black-height
        property satisfied
    """
    if (CN.isSentinel()):
        return 0
    leftHeight = getBlackHeight(CN.getLChild())
    rightHeight = getBlackHeight(CN.getRChild())
    
    incr = 0
    if (CN.getColor() == 'black'):
        incr = 1

    if (leftHeight == -1 or rightHeight == -1 or leftHeight != rightHeight):
        return -1
    else:
        return leftHeight + incr


def isRedBlack(tree):
    """
        A function that checks whether a given tree satisfies the 
        Red-Black properties
    """
    if (tree._root.getColor() != 'black'):
        print("Error: Root is not black!")
        return False
    if (redParent(tree._root) == False):
        print("Error: Red node in tree has a red child!")
        return False
    if (getBlackHeight(tree._root) == -1):
        print("Error: Black height property is not satisfied")
        return False
    return True
    

def main():
    SIZE = 10                      # Number of nodes you want in tree
    testValues = [13, 6, 8, 2]    # Premade tickets to test specific cases 
    # 4, 15, 16, 9, 17, 23, 26, 18, 19, 1 

    #testTickets = randomTestTickets(SIZE)             # For random tickets
    testTickets = defaultTestTickets(testValues)     # For premade tickets
    
    testTree = RedBlackTree()

    print("List of Test Tickets:", end=" ")
    print([t.ticketID for t in testTickets])

    print("============ Testing Insert Method ============")
    res = True
    for ticket in testTickets:
        print("Inserting " + str(ticket.ticketID), end=": ")
        res = testTree.insert(ticket) 
        res = res and isRedBlack(testTree)
        print(res)
        if not res:
            print("INSERTION FAILED")
            break
    

    if res:
        print("============ Testing Traversal Methods ============")
        print("Pre-order:", end=" ")
        print(testTree.traverse("pre-order"))
        print("In-order:", end=" ")
        print(testTree.traverse("in-order"))
        print("Post-order:", end=" ")
        print(testTree.traverse("post-order"))

        print("============ Testing Find Method ============")
        findTestVals = []
        for _ in range(2):
            # Grab a ticket that should be in the tree
            findTestVals.append(choice(testTickets).ticketID)
            # Grab a random value (may or may not be in tree)
            findTestVals.append(randint(1, SIZE+20))
        for value in findTestVals:
            result = testTree.find(value)
            if result is not False:
                result = True
            print(f"Is {value} in the tree: {result}" )

        print("============ Testing Delete Method ============")
        print("Deleting nodes until tree is empty:")
        while len(testTickets) > 0:
            deleteTicket = choice(testTickets)
            testTickets.remove(deleteTicket)
            deleteID = deleteTicket.ticketID
            print(f"Deleting node {deleteID}...")
            deleteResult = testTree.delete(deleteID)
            deleteResult = deleteResult and isRedBlack(testTree)
            if deleteResult:
                print("DELETION SUCCESSFUL!\n")
            else:
                print("DELETION FAILED!\n")
                break
    


if __name__ == '__main__':
    main()