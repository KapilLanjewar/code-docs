# *************************************************************************
# APPROACHES
# *************************************************************************
# 1. Using set and new nodes
#
# 2. Using set and existing node
#
# 3. Using set and different list
#
# 4. Using nested loop
# *************************************************************************

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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

    # O(n)
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

    # O(1) for first index
    # O(n) for indexes other than first
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

    # O(1) for first index
    # O(n) for indexes other than first
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

    # O(n)
    # Edge cases:
    #   1. If list is empty
    #   2. If list has only one element
    #   3. If sublist indexes are out of bounds
    def sublist(self, start_index, end_index):
        if self.length <= 1:
            return None
        if start_index < 0 or start_index > self.length:
            return None
        if end_index < 0 or end_index > self.length:
            return None

        if start_index != end_index:
            current = self.head
            prev = None
            for count in range(self.length):
                if count > end_index:
                    prev.next = None
                    self.tail = prev
                    break
                if count == start_index:
                    self.head = current
                    if prev:
                        prev.next = None

                prev = current
                current = current.next

    # *************************************************************************
    # SOLUTION
    # *************************************************************************

    # O(n)
    # Edge cases:
    #   1. If list is empty
    #   2. If list has only one element
    def remove_duplicates_using_new_nodes_with_set(self):
        if not self.head or not self.head.next:
            return None

        current = self.head
        s = set()
        while current:
            if current.value not in s:
                s.add(current.value)
            current = current.next

        n = Node(0)
        t = n
        for item in s:
            n.next = Node(item)
            n = n.next

        self.head = t.next
        self.tail = n

        self.length = len(s)
        t = None

    # O(n)
    # Edge cases:
    #   1. If list is empty
    #   2. If list has only one element
    def remove_duplicates_using_existing_nodes_with_set(self):
        if not self.head or not self.head.next:
            return None

        current = self.head
        s = set()
        n = Node(0)
        t = n
        while current:
            after = current.next
            current.next = None
            if current.value not in s:
                s.add(current.value)
                n.next = current
                n = current
            current = after

        self.head = t.next
        self.tail = n

        self.length = len(s)
        t = None

    # O(n)
    # Edge cases:
    #   1. If list is empty
    #   2. If list has only one element
    def remove_duplicates_using_different_list_with_set(self):
        if not self.head or not self.head.next:
            return None

        current = self.head
        s = set()
        while current:
            if current.value not in s:
                s.add(current.value)
            current = current.next

        new_list = LinkedList()
        for item in s:
            new_list.append(item)

        self.head = new_list.__get_node(0)
        self.tail = new_list.__get_node(self.length - 1)

    # O(n²) - For each element from outer loop cycle,
    #         how many duplicates are present,
    #         those are discovered and bridged using inner loop
    #
    # Edge cases:
    #   1. If list is empty
    #   2. If list has only one element
    def remove_duplicates(self):
        if not self.head or not self.head.next:
            return None

        current = self.head
        prev = None
        while current:
            inner = current.next
            prev = current
            while inner:
                if current.value == inner.value:
                    # prev will be preserved
                    # and used to bridge the duplicates
                    # until different next item is found
                    # otherwise it will eventually point to None via next
                    prev.next = inner.next
                    self.length -= 1
                    self.tail = prev
                else:
                    prev = inner
                    self.tail = inner
                inner = inner.next
            prev = current
            current = current.next
