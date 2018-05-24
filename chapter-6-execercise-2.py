# Quang Lam

class BinarySearchTree:
    # This is a Node class that is internal to the BinarySearchTree class.
    class Node:
        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right

        def getVal(self):
            return self.val

        def setVal(self,newval):
            self.val = newval

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def setLeft(self,newleft):
            self.left = newleft

        def setRight(self,newright):
            self.right = newright

        # This method deserves a little explanation. It does an inorder traversal
        # of the nodes of the tree yielding all the values. In this way, we get
        # the values in ascending order.
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.val

            if self.right != None:
                for elem in self.right:
                    yield elem

        def __repr__(self):
            return "BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"

    # Below are the methods of the BinarySearchTree class.
    def __init__(self, root=None):
        self.root = root

    def insert(self,val):
        self.root = BinarySearchTree.__insert(self.root, val)

    def __insert(root, val):
        if root == None:
            return BinarySearchTree.Node(val)

        if val < root.getVal():
            root.setLeft(BinarySearchTree.__insert(root.getLeft(),val))
        else:
            root.setRight(BinarySearchTree.__insert(root.getRight(),val))

        return root

    def remove(self, val):
        self.root = BinarySearchTree.__remove(self.root, val)

    def __remove(root, val):
        if val == root.getVal():
            # Case 1 & 2
            if root.getLeft() == None:
                return root.getRight()
            if root.getRight() == None:
                return root.getLeft()

            # Case 3
            rightMostNode = BinarySearchTree.__getRightMost(root.getLeft())
            tmp = rightMostNode.getVal()
            root.setLeft(BinarySearchTree.__remove(root.getLeft(), tmp))
            root.setVal(tmp)

        if val < root.getVal():
            root.setLeft(BinarySearchTree.__remove(root.getLeft(), val))
        else:
            root.setRight(BinarySearchTree.__remove(root.getRight(), val))

        return root

    def __getRightMost(root):
        rightMostNode = root
        while rightMostNode.getRight() != None:
            rightMostNode = rightMostNode.getRight()
        return rightMostNode

    def __iter__(self):
        if self.root != None:
            return iter(self.root)
        else:
            return iter([])

    def __contains__(self, val):
        root = self.root

        while root != None:
            if root.getVal() == val:
                return True
            if val < root.getVal():
                root = root.getLeft()
            elif val > root.getVal():
                root = root.getRight()

        return False

    def __str__(self):
        return "BinarySearchTree(" + repr(self.root) + ")"

def main():
    lst = BinarySearchTree()

    print("Binary Search Program")
    print("---------------------")
    print("Make a choice...")
    print("1. Insert into tree.")
    print("2. Delete from tree.")
    print("3. Lookup value.")

    choice = 0
    while True:
        if choice < 1:
            try:
                choice = int(input("Choice? "))
                if choice < 1 or choice > 3:
                    break
            except ValueError:
                break
        else:
            if choice == 1:
                try:
                    num = int(input("Insert? "))
                    lst.insert(num)
                except ValueError:
                    choice = 0
            if choice == 2:
                try:
                    num = int(input("Value? "))

                    if num in lst:
                        lst.remove(num)
                        print(num, "has been deleted from the tree.")
                    else:
                        print(num, "was not in the tree.")

                except ValueError:
                    choice = 0
            if choice == 3:
                try:
                    num =int(input("Value? "))
                    if num in lst:
                        print("Yes,", num, "is in the tree.")
                    else:
                        print("No,", num, "is in the tree.")
                except ValueError:
                    choice = 0

    for item in lst:
        print(item)

if __name__ == "__main__":
    main()