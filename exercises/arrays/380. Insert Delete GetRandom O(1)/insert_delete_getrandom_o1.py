class RandomizedSet:
    def __init__(self):
        self.data = set()
        # self.data = []

    def insert(self, val: int) -> bool:
        if val not in self.data:
            # self.data.append(val)
            self.data.add(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            self.data.discard(val)
            return True

        return False

    def getRandom(self) -> int:
        tmp_lst = list(self.data)
        if len(self.data) <= 2:
            return tmp_lst[0]

        random.shuffle(tmp_lst)
        random_element = tmp_lst[0]

        return random_element

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
