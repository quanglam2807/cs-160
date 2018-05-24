# Quang Lam

class LinkedList:

    # The __Node class is used internally by the LinkedList class. It is
    # invisible from outside this class due to the two underscores
    # that precede the class name. Python mangles names so that they
    # are not recognizable outside the class when two underscores
    # precede a name but aren't followed by two underscores at the
    # end of the name (i.e. an operator name).
    class __Node:
        def __init__(self,item,next=None):
            self.item = item
            self.next = next

        def getItem(self):
            return self.item

        def getNext(self):
            return self.next

        def setItem(self, item):
            self.item = item

        def setNext(self,next):
            self.next = next

    def __init__(self,contents=[]):
        # Here we keep a reference to the first node in the linked list
        # and the last item in the linked list. The both point to a
        # dummy node to begin with. This dummy node will always be in
        # the first position in the list and will never contain an item.
        # Its purpose is to eliminate special cases in the code below.
        self.first = LinkedList.__Node(None,None)
        self.last = self.first
        self.numItems = 0
        for e in contents:
            self.append(e)

    def __getitem__(self,index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            return cursor.getItem()

        raise IndexError("LinkedList index out of range")

    def __setitem__(self,index,val):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            cursor.setItem(val)
            return

        raise IndexError("LinkedList assignment index out of range")

    def insert(self,index,item):
        cursor = self.first

        if index < self.numItems:
            for i in range(index):
                cursor = cursor.getNext()

            node = LinkedList.__Node(item, cursor.getNext())
            cursor.setNext(node)
            self.numItems += 1
        else:
            self.append(item)


    def __add__(self,other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + \
                str(type(self)) + " + " + str(type(other)))
        result = LinkedList()

        cursor = self.first.getNext()

        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        cursor = other.first.getNext()

        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        return result


    def __contains__(self,item):
        # This is left as an exercise for the reader.
        pass

    def __delitem__(self,index):
        # This is left as an exercise for the reader.
        cursor = self.first

        if index < self.numItems:
            for i in range(index):
                cursor = cursor.getNext()

            cursor.setNext(cursor.getNext().getNext())

            self.numItems -= 1
            if self.numItems == 0:
                self.last = self.first
        else:
            raise Exception("Index out of bounds")

    def __eq__(self,other):
        if type(other) != type(self):
            return False

        if self.numItems != other.numItems:
            return False

        cursor1 = self.first.getNext()
        cursor2 = other.first.getNext()
        while cursor1 != None:
            if cursor1.getItem() != cursor2.getItem():
                return False
            cursor1 = cursor1.getNext()
            cursor2 = cursor2.getNext()

        return True

    def __iter__(self):
        # This is left as an exercise for the reader.
        pass

    def __len__(self):
        # This is left as an exercise for the reader.
        return self.numItems
    def append(self,item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1

    def __str__(self):
        # This is left as an exercise for the reader.
        result = "LinkedList(["

        cursor = self.first.getNext()

        while cursor != None:
            result += str(cursor.getItem()) + ","
            cursor = cursor.getNext()

        if self.numItems > 0:
            result = result[:-1]
        result += "])"
        return result

class Stack:
    def __init__(self):
        self.data = LinkedList()

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to pop an empty stack")

        item = self.data[0]
        del self.data[0]
        return item

    def push(self,item):
        self.data.insert(0,item)

    def top(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to get top of empty stack")

        return self.data[0]

    def isEmpty(self):
        return len(self.data) == 0

    def clear(self):
        self.data = LinkedList()

    def __str__(self):
        return "Stack(" + str(self.data) + ")"

    def __getitem__(self,index):
        return self.data[index]

def getPrecendence(operator):
    if operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return 0

def main():
    exprStr = input("Please enter an inflix expression: ")

    expr = exprStr.split(' ')
    expr.insert(0, '(')
    expr.append(')')

    operators = Stack()
    operands = Stack()

    for o in expr:
        if o in ['+', '-', '*', '\\', '(', ')']:
            if o == '(':
                operators.push(o)
            else:
                while getPrecendence(o) <= getPrecendence(operators.top()):
                    topOp = operators.pop()
                    if topOp in ['+', '-', '*', '\\']:
                        b = operands.pop()
                        a = operands.pop()
                        if topOp == '+': operands.push(a + b)
                        if topOp == '-': operands.push(a - b)
                        if topOp == '*': operands.push(a * b)
                        if topOp == '/': operands.push(a / b)
                    elif topOp == '(':
                        break
                if o != ')': operators.push(o)
        else:
            operands.push(float(o))

    print("The answer is {0:g}.".format(operands[0]))

if __name__ == "__main__":
    main()