"""
- rules
put adds an object to the buffer
    - if buffer full, replace oldest object
    - if buffer not full, just add

- algorithm

adding to the buffer

- if all None
 - add to zero
if not
- get the oldest index point

I have to track the oldest 

when i add an item:
    - Write is tracking the newest
    - Read is tracking the oldest

- When we add an item, write increments but read stays

- when we get an item, we get the one that read is looking at
- Then read goes to write if the other item is None

- Adding an item
- 



"""

class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None for i in range(size)]
        self.max_idx = size - 1
        self.oldest = [] #Oldest idx is last
        self.newest = 0 #tracks oldest

    def put(self, item):
        #Check for all None
        if all(x is None for x in self.buffer):
            self.buffer[0] = item
            self.oldest.insert(0, 0)
            return

        #Check for None with other values
        for idx, buffer_item in enumerate(self.buffer):
            if buffer_item == None:
                self.buffer[idx] = buffer_item
                self.newest = idx
                self.oldest.insert(0, idx)
                return
        
        #If no nones, replace at oldest
        self.buffer.insert(self.oldest.pop(), item)

    def get(self):
        #Return None if all None
        if all([item is None for item in self.buffer]):
            return None
        else:
            return self.buffer.pop(self.oldest.pop())

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.oldest)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.oldest)
print(buffer.get() == 2)             # True

# buffer.put(5)
# buffer.put(6)
# buffer.put(7)
# print(buffer.get() == 5)             # True
# print(buffer.get() == 6)             # True
# print(buffer.get() == 7)             # True
# print(buffer.get() is None)          # True

# buffer2 = CircularBuffer(4)

# print(buffer2.get() is None)         # True

# buffer2.put(1)
# buffer2.put(2)
# print(buffer2.get() == 1)            # True

# buffer2.put(3)
# buffer2.put(4)
# print(buffer2.get() == 2)            # True

# buffer2.put(5)
# buffer2.put(6)
# buffer2.put(7)
# print(buffer2.get() == 4)            # True
# print(buffer2.get() == 5)            # True
# print(buffer2.get() == 6)            # True
# print(buffer2.get() == 7)            # True
# print(buffer2.get() is None)         # True