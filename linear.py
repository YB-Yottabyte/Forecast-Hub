class LinearProbingHashTable:
    def __init__(self, table, m):
        self.T = table[:]
        self.m = m
        self.DELETED = "DELETED"
        self.NIL = None

    def h(self, k, i):
        return (k % self.m + i) % self.m

    def insert(self, k):
        print(f"\nInsert {k}:")
        for i in range(self.m):
            q = self.h(k, i)
            print(f"  Probe {i+1} → index {q} → {self.status(q)}")
            if self.T[q] is None or self.T[q] == self.DELETED:
                self.T[q] = k
                self.summary(k, i + 1)
                return
        print("  → Table full, could not insert.")

    def delete(self, k):
        print(f"\nDelete {k}:")
        for i in range(self.m):
            q = self.h(k, i)
            print(f"  Probe {i+1} → index {q} → {self.status(q)}")
            if self.T[q] is None:
                print("  → Key not found.")
                return
            if self.T[q] == k:
                self.T[q] = self.DELETED
                print(f"  → Deleted key {k} at index {q}")
                return
        print("  → Key not found.")

    def search(self, k):
        print(f"\nSearch {k}:")
        for i in range(self.m):
            q = self.h(k, i)
            print(f"  Probe {i+1} → index {q} → {self.status(q)}")
            if self.T[q] is None:
                print("  → Key not found.")
                return
            if self.T[q] == k:
                print(f"  → Key {k} found at index {q}")
                return
        print("  → Key not found.")

    def status(self, index):
        if self.T[index] is None:
            return "empty"
        elif self.T[index] == self.DELETED:
            return "DELETED"
        else:
            return f"occupied ({self.T[index]})"

    def summary(self, key, probes):
        print("\nSummary:")
        print(f"{'First probed':<15} | {'Key':<5} | {'Number of probes'}")
        print("-" * 45)
        print(f"{key % self.m:<15} | {key:<5} | {probes}")
        print("\nUpdated table:")
        print(self.T)


# Example usage
if __name__ == "__main__":
    initial_table = [
        10, "DELETED", 9, "DELETED", "DELETED",
        8, 7, 6, 5, 4, 3, 2, 1
    ]
    m = 13
    ht = LinearProbingHashTable(initial_table, m)
    ht.search(10)



class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return key % self.size

    def insert(self, key):
        for i in range(self.size):
            idx = (self._hash(key) + i) % self.size
            if self.table[idx] is None or self.table[idx] == "DELETED":
                self.table[idx] = key
                return
        print("Hash Table is full")

    def search(self, key):
        for i in range(self.size):
            idx = (self._hash(key) + i) % self.size
            if self.table[idx] is None:
                return False
            if self.table[idx] == key:
                return True
        return False

    def delete(self, key):
        for i in range(self.size):
            idx = (self._hash(key) + i) % self.size
            if self.table[idx] == key:
                self.table[idx] = "DELETED"
                return
        print("Key not found")

    def display(self):
        print(self.table)
