#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        self.list.append(item)
        return item

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.list.is_empty():
            return None
        return self.list.get_at_index(0)

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return front item, if any
        if self.list.is_empty():
            raise ValueError("Unable to dequeue. Queue is empty")
        item = self.list.get_at_index(0)
        self.list.delete(item)
        return item
        # Implement ArrayQueue below, then change the assignment at the bottom
        # to use this Queue implementation to verify it passes all tests


class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new  QGSDKl
        # x  .ist (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        if len(self.list) > 0:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        self.list.append(item)
        return self.list

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        return self.list[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return front item, if any
        item = self.list[0]
        self.list.remove(item)
        return self.list

# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests


def linked_queue_test():
    Queue = LinkedQueue()
    print(f"Is queue empty? {Queue.is_empty()}")
    print(f"Queue length: {Queue.length()}")
    print(f"Adding A to Queue {Queue.enqueue('A')}")
    print(Queue.list)
    print(f"Adding D to Queue {Queue.enqueue('D')}")
    print(Queue.list)
    print(f"Leader of Queue: {Queue.front()}")
    print(f"Dequeuing front of List: {Queue.dequeue()}")
    print(Queue.list)
    print(f"Queue length: {Queue.length()}")
    print(f"Front is: {Queue.front()}")


def array_queue_test():
    Queue = ArrayQueue()
    print(f"Is queue empty? {Queue.is_empty()}")
    print(f"Queue length: {Queue.length()}")
    print(f"Adding A to Queue {Queue.enqueue('A')}")
    print(Queue.list)
    print(f"Adding D to Queue {Queue.enqueue('D')}")
    print(Queue.list)
    print(f"Leader of Queue: {Queue.front()}")
    print(f"Dequeuing front of List: {Queue.dequeue()}")
    print(Queue.list)
    print(f"Queue length: {Queue.length()}")
    print(f"Front is: {Queue.front()}")


if __name__ == "__main__":
    linked_queue_test()
    print("\n")
    array_queue_test()
