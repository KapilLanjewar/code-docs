# *************************************************************************
# APPROACHES
# *************************************************************************
# 1. By creating new nodes
#
# 2. By using same nodes
#
# 3. By creating different LinkedLists
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
    def partition_list_with_new_nodes(self, e):
        if not self.head or not self.head.next:
            return None

        left = Node(0)
        right = Node(0)

        left_pointer = left
        right_pointer = right

        current = self.head

        while current:
            if current.value < e:
                temp = Node(current.value)
                left_pointer.next = temp
                left_pointer = temp
            else:
                temp = Node(current.value)
                right_pointer.next = temp
                right_pointer = temp
            current = current.next

        self.head = left.next
        self.tail = right_pointer

        left_pointer.next = right.next

        left = None
        right = None

    # O(n)
    # Edge cases:
    #   1. If list is empty
    #   2. If list has only one element
    def partition_list_with_same_nodes(self, e):
        if not self.head or not self.head.next:
            return None

        left = Node(0)
        right = Node(0)

        left_pointer = left
        right_pointer = right

        current = self.head

        after = None

        while current:
            after = current.next
            current.next = None

            if current.value < e:
                left_pointer.next = current
                left_pointer = current
            else:
                right_pointer.next = current
                right_pointer = current

            current = after

        self.head = left.next
        self.tail = right_pointer

        left_pointer.next = right.next

        left = None
        right = None

    # O(n²) - Expensive - Each cycle of while loop calls
    #         LinkedList __get_node() method which is already O(n)
    #
    # Edge cases:
    #   1. If list is empty
    #   2. If list has only one element
    def partition_list_by_creating_different_lists(self, e):
        if not self.head or not self.head.next:
            return None

        left = LinkedList()
        right = LinkedList()

        current = self.head

        while current:
            if current.value < e:
                left.append(current.value)
            else:
                right.append(current.value)

            current = current.next

        self.head = left.__get_node(0)
        self.tail = right.__get_node(right.length - 1)

        left_end = left.__get_node(left.length - 1)
        right_start = right.__get_node(0)
        left_end.next = right_start

        left = None
        right = None
