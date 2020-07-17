class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.length = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.length += 1
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
