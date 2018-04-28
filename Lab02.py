class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hash(key)

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            self.data[hashvalue] = data

    def hash(self, key):
        sum = 0
        for counter, char in enumerate(key):
            sum += ord(char)*counter
        return sum%self.size

    def get(self, key):
        starthash = self.hash(key)
        if self.slots[starthash] is None:
            return None
        return self.data[starthash]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

if __name__ == '__main__':
    n, m = input().split()
    hash_table = HashTable(int(n))
    keys = []
    for _ in range(int(n)):
        key, value = input().split()
        hash_table[key] = value
    for _ in range(int(m)):
        keys.append(input())
    for key in keys:
        print(hash_table[key])