class MyHashSet:
    def __init__(self):
        self.hash_set = {}
        self.values = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hash_set[key] = key

    def remove(self, key: int) -> None:
        if self.contains(key):
            del self.hash_set[key]

    def contains(self, key: int) -> bool:
        return False if key not in self.hash_set else True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
