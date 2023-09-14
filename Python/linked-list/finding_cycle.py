# *************************************************************************
# APPROACHES
# *************************************************************************
# 1. Floyd’s cycle detection algorithm
#
# 2. By using set
#
# 3. By using flag with nodes
# *************************************************************************

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.is_visited = False


class LinkedList:
    def __init__(self, value=0):
        if value != 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    # O(n)
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # O(1)
    # Edge case - If the list is empty
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # O(n)
    # Edge cases:
    #   1. If the list is empty
    #   2. If list contains only one element
    def pop(self):
        if self.length == 0:
            return None

        first = self.head
        second = None
        while first.next is not None:
            second = first
            first = first.next

        self.length -= 1

        if self.length == 0:
            second = None
            self.head = None
            self.tail = None
            return first.value

        self.tail = second
        self.tail.next = None
        second = None
        return first.value

    # O(1)
    # Edge case - If the list is empty
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # O(1)
    # Edge cases:
    #   1. If the list is empty
    #   2. If list contains only one element
    def pop_first(self):
        if self.length == 0:
            return None

        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp.value

    # O(n)
    # Edge cases:
    #   1. If the list is empty
    #   2. If specified index is out of bound
    def get_value(self, index):
        if index < 0 or index >= self.length or self.length == 0:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    # O(n)
    # Edge cases:
    #   1. If the list is empty
    #   2. If specified index is out of bound
    def __get_node(self, index):
        if index < 0 or index >= self.length or self.length == 0:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # O(n)
    # Edge cases - If specified index is out of bound
    def set_value(self, index, value):
        temp = self.__get_node(index)
        if temp:
            temp.value = value
            return True
        return False

    # O(1) for 1st and last index
    # O(n) for indexes other than 1st and last index
    # Edge cases:
    #   1. If specified index is out of bound
    #   2. If the list is empty then the index must be 0
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if self.length == 0 and index != 0:
            return False
        if index == 0:
            result = self.prepend(value)
            return result
        if index == self.length - 1:
            result = self.append(value)
            return result

        new_node = Node(value)
        temp = self.__get_node(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    # O(1) for 1st and last index
    # O(n) for indexes other than 1st and last index
    # Edge cases:
    #   1. If specified index is out of bound
    #   2. If the list is empty
    def remove(self, index):
        if self.length == 0:
            return None
        if index < 0 or index > self.length:
            return None
        if index == 0:
            result = self.pop_first()
            return result
        if index == self.length - 1:
            result = self.pop()
            return result

        prev = self.__get_node(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

    # O(n)
    # Edge cases:
    #   1. If list is empty
    #   2. If list has only one element
    def reverse(self):
        if self.length == 0 or self.length == 1:
            return False

        self.tail = self.head

        current = self.head
        front = current.next
        behind = None

        while current is not None:
            front = current.next
            self.head = current
            current.next = behind
            behind = current
            current = front
        return True

    # *************************************************************************
    # SOLUTION
    # *************************************************************************

    # Floyd's Cycle Detection Algorithm
    # O(n)
    # Edge cases:
    #   1. If list is empty
    #   2. If list has only one element
    def has_loop_floyds_algorithm(self):
        if self.head is None or self.head.next is None:
            return False

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    # Using set
    # O(n)
    # Python set operations uses hashing with O(1)
    #
    # Edge cases:
    #   1. If list is empty
    #   2. If list has only one element
    def has_loop_using_set(self):
        if self.head is None or self.head.next is None:
            return False

        current = self.head
        s = set()

        while current:
            if current.value in s:
                return True
            else:
                s.add(current.value)

            current = current.next
        return False

    # O(n)
    # Edge cases:
    #   1. If list is empty
    #   2. If list has only one element
    def has_loop_by_recording_node_visit(self):
        if self.head is None or self.head.next is None:
            return False

        current = self.head
        while current:
            if current.is_visited:
                return True
            else:
                current.is_visited = True
            current = current.next
        return False
