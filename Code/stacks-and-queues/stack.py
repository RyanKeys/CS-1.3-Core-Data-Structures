#!python
from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        count = 0
        for i in range(self.list.length()):
            count += 1
        return count

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Push given item
        self.list.prepend(item)
        print(self.list)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.is_empty():
            return None
        else:
            return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        if self.is_empty():
            raise ValueError("Stack Empty")
        else:
            item = self.list.head.data
            self.list.delete(self.list.head.data)
            return item

# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests


class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if len(self.list) != 0:
            return False
        return True

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        self.list.insert(0, item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        return self.list[0]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        return self.list.pop(0)

# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests


def linked_stack_test():
    Stack = LinkedStack()
    print(Stack.length())
    print(Stack.is_empty())
    Stack.push("YO")
    print(Stack.is_empty())
    print(Stack.length())
    print(Stack.peek())
    Stack.push("REE")
    print(Stack.length())
    print(Stack.peek())
    print(Stack.pop())
    print(Stack.list)
# Stack = ArrayStack


def array_stack_test():
    Stack = ArrayStack()
    print(Stack.length())
    print(Stack.is_empty())
    Stack.push("YO")
    print(Stack.is_empty())
    print(Stack.length())
    print(Stack.peek())
    Stack.push("REE")
    print(Stack.length())
    print(Stack.peek())
    print(Stack.pop())
    print(Stack.list)


if __name__ == "__main__":
    linked_stack_test()
    print("\n")
    array_stack_test()
