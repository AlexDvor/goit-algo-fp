class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Додати елемент у кінець списку"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        """Вивести список"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """Реверсування списку"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        """Сортування списку злиттям"""

        def merge_sort(head):
            if not head or not head.next:
                return head

            # Пошук середини списку
            def get_middle(node):
                slow = node
                fast = node.next
                while fast and fast.next:
                    slow = slow.next
                    fast = fast.next.next
                return slow

            middle = get_middle(head)
            next_to_middle = middle.next
            middle.next = None

            left = merge_sort(head)
            right = merge_sort(next_to_middle)

            return merge(left, right)

        def merge(left, right):
            dummy = Node(0)
            tail = dummy
            while left and right:
                if left.data < right.data:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next

            tail.next = left or right
            return dummy.next

        self.head = merge_sort(self.head)


def merge_sorted_lists(list1, list2):
    """Об’єднує два відсортовані списки"""
    dummy = Node(0)
    tail = dummy

    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data < current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    tail.next = current1 or current2

    result = SinglyLinkedList()
    result.head = dummy.next
    return result


# Створення та заповнення списків
list1 = SinglyLinkedList()
for value in [1, 3, 5]:
    list1.append(value)

list2 = SinglyLinkedList()
for value in [2, 4, 6]:
    list2.append(value)

# Об'єднання
merged = merge_sorted_lists(list1, list2)
print("Об'єднаний відсортований список:")
merged.print_list()

# Реверс
merged.reverse()
print("Реверсований список:")
merged.print_list()

# Несортований список і його сортування
unsorted = SinglyLinkedList()
for value in [4, 1, 3, 2]:
    unsorted.append(value)
print("До сортування:")
unsorted.print_list()

unsorted.sort()
print("Після сортування:")
unsorted.print_list()
