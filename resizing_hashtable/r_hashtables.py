

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.original_capacity = capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = ((hash << 5) + hash) + ord(char)

    return (hash & 0xFFFFFFFF) % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hashed = hash(key, hash_table.capacity)
    if hash_table.storage[hashed] == None:
        hash_table.storage[hashed] = LinkedPair(key, value)
    else:
        collided = LinkedPair(key, value)
        collided.next = hash_table.storage[hashed]
        hash_table.storage[hashed] = collided


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashed = hash(key, hash_table.capacity)

    if hash_table.storage[hashed] == None:
        print(f"{key} doesn't exist")
    else:
        current = hash_table.storage[hashed]
        if current.key == key:
            hash_table.storage[hashed] = current.next
        else:
            while(current != None):
                if current.next.key == key:
                    current.next = current.next.next
                current = current.next


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hashed = hash(key, hash_table.capacity)

    if hash_table.storage[hashed] == None:
        return None
    else:
        current = hash_table.storage[hashed]
        if current.key == key:
            return current.value
        else:
            while(current != None):
                if current.next.key == key:
                    return current.next.value
                current = current.next

            return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    resized = HashTable(hash_table.capacity * 2)
    for item in hash_table.storage:
        current = item
        while(current != None):
            hash_table_insert(resized, current.key, current.value)
            current = current.next
    return resized


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
