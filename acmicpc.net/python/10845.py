#  https://www.acmicpc.net/problem/10845


from typing import Optional


class Node:
    def __init__(self, val: int, next: Optional["Node"] = None) -> None:
        self.val = val
        self.next = next

class Queue:
    def __init__(self) -> None:
        self.head = self.tail = None
        self._size = 0

    def push(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def pop(self) -> int:
        if not self.head:
            return -1
        return_val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self._size -= 1
        return return_val

    def empty(self) -> int:
        return 0 if self._size else 1

    def front(self) -> int:
        return self.head.val if self.head else -1

    def back(self) -> int:
        return self.tail.val if self.tail else -1

    def size(self) -> int:
        return self._size


q = Queue()
ans = []
n = int(input())
for _ in range(n):
    command = input().split()
    if len(command) == 2:
        q.push(int(command[1]))
    else:
        ans.append(str(getattr(q, command[0])()))

print("\n".join(ans))

