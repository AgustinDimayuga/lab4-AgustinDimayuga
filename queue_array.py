class QueueArray:
    """Implements an efficient first-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates an empty queue with a capacity"""
        self.capacity = capacity  # Capacity of your queue
        self.items = [None] * capacity  # initializing the queue
        self.num_items = 0  # number of elements in the queue
        self.head = 0
        self.tail = 0

    def is_empty(self):
        """Returns true if the queue self is empty and false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """Returns true if the queue self is full and false otherwise"""
        return self.num_items == self.capacity

    def enqueue(self, item):
        """Adds item to the queue"""
        if self.is_full():
            raise QueueFull("Queue is full")
        self.items[self.tail] = item
        self.num_items += 1
        self.tail += 1
        if self.tail > self.capacity - 1:
            self.tail = 0

    def dequeue(self):
        """Returns the current front of the queue"""
        if self.is_empty():
            raise QueueEmpty("Queue is empty")
        curr = self.items[self.head]
        self.items[self.head] = None
        self.head += 1
        if self.head > self.capacity - 1:
            self.head = 0
        self.num_items -= 1
        return curr

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        if self.is_empty():
            raise QueueFull("Queue is empty")
        return self.items[self.head]

    def size(self):
        return self.num_items
