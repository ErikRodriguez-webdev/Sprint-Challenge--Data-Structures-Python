class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.length = 0

    def append(self, item):
        print(self.capacity, self.length, self.storage)
        # if len(storage) is < capacity then append item to back. Add 1 to length
        if len(self.storage) < self.capacity:
            self.length += 1
            self.storage.append(item)
    # if length >= 0  and length <= capacity - 1 then insert(length, item). Add 1 to length
        # elif self.length >= 1 and self.length <= self.capacity - 1:
        #     self.length += 1
        #     self.storage.pop(self.length)
        #     self.storage.insert(self.length - 1, item)
    # if capacity == len(storage) then set length to 0 and overwrite storage[0]
        elif self.length == self.capacity:
            self.length = 0
            self.storage.pop(self.length)
            self.storage.insert(self.length, item)
            self.length += 1
        else:
            self.storage.pop(self.length)
            self.storage.insert(self.length, item)
            self.length += 1

    def get(self):
        return self.storage
