class HashMap:
    """
    A basic hashmap using separate chaining to resolve collisions.
    
    🔹 Demonstrates Abstraction: hides details of hashing and bucket management.
    🔹 Ready for Inheritance: you can subclass this to add resizing, etc.
    """

    def __init__(self):
        # Attributes: hold the internal state of the object
        self._bucket_count = 8                          # 🔐 Encapsulation: internal configuration, not exposed directly
        self._buckets = [[] for _ in range(self._bucket_count)]  # Array of buckets for chaining

    def _hash(self, key):
        """
        Private method to compute hash index.
        
        🔐 Encapsulation: implementation hidden from outside.
        🔹 Abstraction: user doesn't need to know hashing details.
        """
        return hash(key) % self._bucket_count

    def put(self, key, value):
        """
        Inserts or updates the value associated with the key.

        🔹 Method: acts on object data, uses 'self'.
        🔹 Polymorphism-ready: can be overridden by a subclass to add resizing or logging.
        """
        index = self._hash(key)
        for pair in self._buckets[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self._buckets[index].append([key, value])  # Add new key-value pair

    def get(self, key):
        """
        Retrieves the value for the given key, raises KeyError if not found.

        🔹 Abstraction: handles collision search internally.
        🔹 Polymorphic behavior possible: override to add default fallback.
        """
        index = self._hash(key)
        for pair in self._buckets[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"{key} not found")

    def remove(self, key):
        """
        Removes the key-value pair if it exists.

        🔹 Demonstrates encapsulated logic for deletion from buckets.
        🔹 Could be overridden (Polymorphism) in subclass with logging or resize-down feature.
        """
        index = self._hash(key)
        self._buckets[index] = [
            pair for pair in self._buckets[index] if pair[0] != key
        ]

class HashSet:
    """
    A set data structure implemented using a HashMap (composition).
    
    🔹 Demonstrates Composition: uses an instance of another class (HashMap).
    🔹 Abstraction: hides value association logic, only keys matter.
    🔹 Inheritance-ready: could extend this class to add features like union, intersection, etc.
    """

    def __init__(self):
        self._map = HashMap()  # 🔐 Encapsulation + Composition: internal map, not exposed to user

    def add(self, key):
        """
        Adds a key to the set.
        
        🔹 Method: interfaces with internal HashMap.
        🔹 Abstraction: hides the value (always True) from the user.
        """
        self._map.put(key, True)

    def remove(self, key):
        """
        Removes a key from the set.
        
        🔹 Method: delegates behavior to internal object.
        """
        self._map.remove(key)

    def contains(self, key):
        """
        Checks whether the set contains the given key.
        
        🔹 Encapsulation: internally calls `get()` from HashMap.
        🔹 Could use @property for read-only behavior (e.g., is_empty).
        """
        try:
            self._map.get(key)
            return True
        except KeyError:
            return False
