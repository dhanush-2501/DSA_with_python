class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def prepend(self, value) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def append(self, value) -> bool:
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def pop_first(self) -> None:
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def pop(self):
        if not self.head:
            return None
        if self.head == self.tail:
            removed = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            removed = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        return removed

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return True

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

    def has_loop(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False

    def print_list(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def remove_duplicates(self):
        seen = set()
        curr = self.head
        prev = None
        while curr:
            if curr.value in seen:
                prev.next = curr.next
                self.length -= 1
            else:
                seen.add(curr.value)
                prev = curr
            curr = curr.next

    def binary_to_decimal(self):
        temp = self.head
        count = -1
        while temp:
            count += 1
            temp = temp.next
        temp = self.head
        sum = 0
        while temp:
            sum += 2 ** count * temp.value
            count -= 1
            temp = temp.next
        return sum
    
    def reverse_between(self, m, n):
        if self.length <= 1:
            return
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for i in range(m):
            prev = prev.next
        current = prev.next
        for i in range(n - m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        self.head = dummy.next

    def bubble_sort(self):
        # Initialize the outer and inner pointers
        outer = self.head

        while outer:
            inner = self.head
            swapped = False

            while inner and inner.next:
                if inner.value > inner.next.value:
                    inner.value, inner.next.value = inner.next.value, inner.value
                    swapped = True
                inner = inner.next

            if not swapped:
                # If no swaps were made in this pass, the list is sorted
                break

            outer = outer.next

    def selection_sort(self):
        outer = self.head
        while outer:
            inner = outer.next
            while inner:
                if outer.value > inner.value:
                    outer.value, inner.value = inner.value, outer.value
                inner = inner.next
            outer = outer.next


def find_kth_from_end(self, k):
    slow_ptr = self.head
    fast_ptr = self.head
    for _ in range(k):
        if fast_ptr is None:
            return None
        fast_ptr = fast_ptr.next
    while fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    return slow_ptr


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()

   