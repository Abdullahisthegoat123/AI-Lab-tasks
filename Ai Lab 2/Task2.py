class CustomList:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def insert(self, value):
        if self.size == self.capacity:
            print("List full")
            return
        self.data[self.size] = value
        self.size += 1

    def delete(self, value):
        index = -1
        for i in range(self.size):
            if self.data[i] == value:
                index = i
                break
        if index == -1:
            print("Value not found")
            return
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1

    def search(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1

    def display(self):
        for i in range(self.size):
            print(self.data[i], end=" ")
        print()


class Stack:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def insert(self, value):
        if self.top == self.capacity - 1:
            print("Stack full")
            return
        self.top += 1
        self.data[self.top] = value

    def delete(self):
        if self.top == -1:
            print("Stack empty")
            return
        value = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return value

    def search(self, value):
        for i in range(self.top + 1):
            if self.data[i] == value:
                return i
        return -1

    def display(self):
        for i in range(self.top, -1, -1):
            print(self.data[i], end=" ")
        print()


class Queue:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = capacity

    def insert(self, value):
        if self.size == self.capacity:
            print("Queue full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = value
        self.size += 1

    def delete(self):
        if self.size == 0:
            print("Queue empty")
            return
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def search(self, value):
        idx = self.front
        for _ in range(self.size):
            if self.data[idx] == value:
                return idx
            idx = (idx + 1) % self.capacity
        return -1

    def display(self):
        idx = self.front
        for _ in range(self.size):
            print(self.data[idx], end=" ")
            idx = (idx + 1) % self.capacity
        print()


if __name__ == "__main__":
    cl = CustomList()
    cl.insert(5)
    cl.insert(8)
    cl.insert(11)
    print("Custom List:")
    cl.display()
    cl.delete(8)
    print("After deletion:")
    cl.display()
    print("Index of 11:", cl.search(11))

    s = Stack()
    print("Stack:")
    s.insert(10)
    s.insert(22)
    s.insert(33)
    s.display()
    s.delete()
    print("After deletion:")
    s.display()
    print("Index of 10:", s.search(10))

    q = Queue()
    print("Queue:")
    q.insert(2)
    q.insert(6)
    q.insert(9)
    q.display()
    q.delete()
    print("After deletion:")
    q.display()
    print("Index of 6:", q.search(6))