
class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    # Hash function is calculated as follows:
    # (First letter ASCII) * 100 + (Second letter ASCII)
    def calculate_hash_value(self, string):
        hash_value = ord(string[0]) * 100 + ord(string[1])
        return hash_value

    def lookup(self, string):
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] == None or string not in self.table[hash_value]:
            return -1
        return hash_value

    def store(self, string):
        hash_value = self.calculate_hash_value(string)
        if self.lookup(string) == -1:
            self.table[hash_value] = []
        self.table[hash_value].append(string)

# Tests
hash_table = HashTable()
print(hash_table.calculate_hash_value('UDACITY'))
hash_table.store('UDACIOUS')
print(hash_table.lookup('UDACIOUS'))
print(hash_table.lookup('UDACITY'))