class SinglyLinkedList:
    """
    Singly linked list: Each node links to the next.
    
    🔹 Abstraction: Hides the internal link/node logic from external code.
    🔹 Inheritance-ready: Can be extended for more functionality (e.g., reverse, size).
    """

    class Node:
        """
        Inner Node class to represent elements of the list.
        
        🔹 Encapsulation: Node is hidden inside the main list class.
        🔹 Abstraction: External code interacts with the list, not with Node directly.
        """
        def __init__(self, data):
            self.data = data         # 🔸 Attribute: node's data
            self.next = None         # 🔸 Attribute: reference to next node

    def __init__(self):
        self._head = None  # 🔐 Encapsulation: list head is hidden using underscore

    def insert_front(self, data):
        """
        Insert at the head (O(1)).
        
        🔹 Method (instance method): modifies the object’s state.
        🔹 Encapsulates how nodes are linked.
        """
        new_node = self.Node(data)
        new_node.next = self._head
        self._head = new_node

    def delete_front(self):
        """
        Remove from head (O(1)).
        
        🔹 Abstraction: Hides pointer manipulation from user.
        🔹 Encapsulation: protects against invalid deletion.
        """
        if self._head is None:
            raise IndexError("List is empty")  # 🔸 Optional polymorphism: can override error behavior
        self._head = self._head.next

    def traverse(self):
        """
        Print all nodes (O(n)).

        🔹 Method for external interaction (abstraction).
        🔹 Could be overridden in a subclass to customize traversal (polymorphism).
        """
        current = self._head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class DoublyLinkedList:
    """
    Doubly linked list with forward and backward traversal.
    
    🔹 Abstraction: user doesn’t manage node links manually.
    🔹 Inheritance-ready: extend to add reverse traversal, insertion at position, etc.
    """

    class Node:
        """
        Node for doubly linked list. Stores data and two pointers.
        
        🔹 Encapsulation: defined inside parent class.
        🔹 Attributes: `data`, `prev`, `next` hold state.
        """
        def __init__(self, data):
            self.data = data         # 🔸 Attribute: stores node's data
            self.prev = None         # 🔸 Attribute: points to previous node
            self.next = None         # 🔸 Attribute: points to next node

    def __init__(self):
        self._head = None  # 🔐 Encapsulation: restricts direct external access
        self._tail = None  # 🔐 Hidden tail pointer for O(1) tail ops

    def insert_end(self, data):
        """
        Add a new node to the tail (O(1)).

        🔹 Instance method: modifies object state.
        🔹 Abstraction: simplifies logic for external usage.
        """
        new_node = self.Node(data)
        if self._tail is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node

    def delete_end(self):
        """
        Remove from tail (O(1)).

        🔹 Encapsulation: manages safe deletion internally.
        🔹 Polymorphic potential: could override for custom behavior/logging.
        """
        if self._tail is None:
            raise IndexError("List is empty")
        if self._tail.prev is None:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None

    def traverse_forward(self):
        """
        Traverse from head to tail (O(n)).

        🔹 Instance method: exposes list content in human-readable form.
        🔹 Polymorphism-ready: could customize display logic via override.
        """
        current = self._head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")