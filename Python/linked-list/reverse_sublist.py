# *************************************************************************
# APPROACHES
# *************************************************************************
# 1. By combining loops
#
# 2. In a single loop
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

    # O(n) + O(n) = O(2n) ≈ O(n)
    # Edge cases:
    #   1. If list is empty
    #   2. If list has only one element
    #   3. If sublist indexes are out of bounds
    def reverse_between_by_combining_loops(self, start_index, end_index):
        if self.length <= 1:
            return None
        if start_index < 0 or start_index > self.length:
            return None
        if end_index < 0 or end_index > self.length:
            return None

        dummy_node = Node(0)
        dummy_node.next = self.head

        previous_node = dummy_node

        for i in range(start_index):
            previous_node = previous_node.next

        current_node = previous_node.next
        self.tail = current_node if self.length == end_index + 1 else self.tail

        for i in range(end_index - start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move

        self.head = dummy_node.next

    # O(n)
    # Edge cases:
    #   1. If list is empty
    #   2. If list has only one element
    #   3. If sublist indexes are out of bounds
    def reverse_between_in_single_loop(self, start_index, end_index):
        if self.length <= 1:
            return None
        if start_index < 0 or start_index > self.length:
            return None
        if end_index < 0 or end_index > self.length:
            return None

        if start_index != end_index:
            current = self.head
            prev = None

            join_pointer = None
            final_tail = None

            prev_tail = None
            flag = False
            for count in range(self.length):
                if start_index <= count <= end_index:
                    if count == start_index:
                        prev_tail = prev
                        flag = True
                        prev = None
                    if count >= start_index and flag:
                        if count == start_index:
                            final_tail = current
                        temp = prev
                        prev = current
                        current = current.next
                        prev.next = temp
                        join_pointer = current if count < end_index else join_pointer
                if count > end_index and flag:
                    flag = False
                if not flag:
                    if count == end_index + 1:
                        final_tail.next = current
                    prev = current
                    current = current.next

            if end_index + 1 == self.length:
                self.tail = final_tail
            if prev_tail:
                prev_tail.next = join_pointer
            else:
                self.head = join_pointer
