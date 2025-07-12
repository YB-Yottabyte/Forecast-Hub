class QuadraticProbingHashTable:
    def __init__(self, table, m, c1=1, c2=3):
        self.T = table[:]
        self.m = m
        self.c1 = c1
        self.c2 = c2
        self.DELETED = "DELETED"
        self.NIL = None

    def h(self, k, i):
        return (k % self.m + self.c1 * i + self.c2 * i * i) % self.m

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


if __name__ == "__main__":
    initial_table = [
        10, "DELETED", 9, "DELETED", "DELETED",
        8, 7, 6, 5, 4, 3, 2, 1
    ]
    m = 13
    ht = QuadraticProbingHashTable(initial_table, m)
    ht.insert(9)
