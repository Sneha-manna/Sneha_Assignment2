class Node:
    """Represents a single node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Manages the singly linked list."""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Adds a node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Prints all elements in the linked list."""
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Deletes the nth node (1-based index) from the list."""
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise ValueError("Index must be a positive integer.")

        if n == 1:
            print(f"Deleting node at position {n} with value: {self.head.data}")
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 1

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError("Index out of range. Cannot delete.")

        print(f"Deleting node at position {n} with value: {current.data}")
        prev.next = current.next


# ----------------- TEST CASE -----------------

if __name__ == "__main__":
    # Create a linked list
    ll = LinkedList()

    # Add nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Initial Linked List:")
    ll.print_list()

    # Delete the 3rd node
    try:
        ll.delete_nth_node(3)
    except Exception as e:
        print("Error:", e)

    print("\nLinked List after deleting 3rd node:")
    ll.print_list()

    # Try to delete an out-of-range node
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print("Error:", e)

    # Try to delete from an empty list
    empty_list = LinkedList()
    try:
        empty_list.delete_nth_node(1)
    except Exception as e:
        print("Error:", e)
