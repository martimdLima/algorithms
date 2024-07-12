class Node:
    def __init__(self, value, level):
        self.value = value
        self.next = [None] * (level + 1)


class Skiplist:
    def __init__(self):
        self.p = 1 // 2
        self.max_level = 5
        self.header = self.create_node(self.max_level, None)
        self.level = 0

    def create_node(self, level, value):
        return Node(value, level)

    def random_level(self):
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def add(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].value < value:
                current = current.next[i]
            update[i] = current

        level = self.random_level()

        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.header
            self.level = level

        new_node = self.create_node(level, value)

        for i in range(level + 1):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def search(self, target: int) -> bool:
        current = self.header
        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].value < target:
                current = current.next[i]
        current = current.next[0]
        if current and current.value == target:
            return True
        return False

    def erase(self, value) -> bool:
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].value < value:
                current = current.next[i]
            update[i] = current

        current = current.next[0]

        if current and current.value == value:
            for i in range(self.level + 1):
                if update[i].next[i] != current:
                    break
                update[i].next[i] = current.next[i]

            while self.level > 0 and self.header.next[self.level] is None:
                self.level -= 1

            return True

        return False


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
