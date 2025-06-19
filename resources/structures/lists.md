
class DynamicArray:
    """
    A simplified version of a dynamic array, similar to Python's built-in list.
    
    🔹 Demonstrates Abstraction by hiding the complexity of resizing.
    🔹 Can be used as a base class for inheritance, enabling Polymorphism (e.g., extending with bounds checking).
    """

    def __init__(self):
        # Attributes (instance variables): these hold the object's state
        self._capacity = 2       # 🔐 Encapsulation: protected by convention (underscore)
        self._size = 0           # 🔐 Encapsulation: internal counter for number of items
        self._data = [None] * self._capacity  # Underlying static array

    def append(self, item):
        """
        Adds an item to the end of the array. Automatically resizes if needed.

        🔹 Method (instance method): requires 'self' to access instance data.
        🔹 Demonstrates Abstraction: caller doesn’t need to manage capacity.
        """
        if self._size == self._capacity:
            self._resize()  # Call to internal logic (encapsulation)
        self._data[self._size] = item
        self._size += 1

    def _resize(self):
        """
        Internal/private method to double the array capacity.

        🔐 Encapsulation: internal logic not exposed to the user.
        🔹 Conventionally private (underscore prefix).
        🔹 Can be overridden in a subclass (Polymorphism).
        """
        self._capacity *= 2
        new_data = [None] * self._capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data  # 🔁 Abstraction: dynamic growth hidden from caller

    def __getitem__(self, index):
        """
        Special method to support bracket notation (arr[0]).

        🔹 Method Overriding (Polymorphism): enables operator overloading.
        🔹 Encapsulation of bounds checking.
        """
        if 0 <= index < self._size:
            return self._data[index]
        raise IndexError('Index out of bounds')

    def __len__(self):
        """
        Returns number of elements using len(array).

        🔹 Special method: supports built-in len().
        🔹 Demonstrates Python’s Duck Typing / Polymorphism.
        """
        return self._size

    @property  # 🔹 Decorator: turns method into a read-only attribute
    def capacity(self):
        """
        Public getter for capacity.

        🔐 Encapsulation: underlying _capacity is protected but accessible.
        🔹 Property: cleaner, attribute-style access to methods.
        """
        return self._capacity

    @property  # 🔹 Decorator: another example of using @property
    def size(self):
        """
        Public getter for size.

        🔹 Method turned into attribute-like access.
        🔹 Keeps internal attribute _size private, following encapsulation.
        """
        return self._size

