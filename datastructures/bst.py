class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.parent = None
        self.right = None

    def childcount(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None or self.right is None:
            return 1
        return 2

    def get_only_child(self):
        assert self.childcount() == 1
        if self.left is None:
            return self.right
        return self.left
    
    def _is_child_value(self, value):
        if self.right and self.right.value == value:
            return True
        if self.left and self.left.value == value:
            return True
        return False

    def replace_child(self, to_replace, new_node):
        if not self._is_child_value(to_replace):
            raise ValueError('Replaced value must be value of one child.')
        if self.left and self.left.value == to_replace:
            self.left = new_node
        else:
            self.right = new_node

        if new_node:
            new_node.parent = self

class BinarySearchTree:
    def __init__(self):
        self.root = None 
        self.size = 0

    def __len__(self):
        return self.size

    def add(self, element):
        if self.root is None:
            self.root = Node(element)
            self.size += 1
        else:
            self._add(self.root, element)

    def _add(self, current, element):
        if element == current.value:
            return
        elif element < current.value:
            if current.left is None:
                current.left = Node(element)
                current.left.parent = current
                self.size += 1
            else:
                self._add(current.left, element)
        else: 
            if current.right is None:
                current.right = Node(element)
                current.right.parent = current
                self.size += 1
            else:
                self._add(current.right, element)

    def delete(self, element):
        node = self.get(element) 
        if node is None:
            return
        if node.childcount() == 0:
            self._update_parent(node, None)
        elif node.childcount() == 1:
            self._update_parent(node, node.get_only_child())
        else:
            successor_value = self.get_successor(node).value
            # Can not lead to endless loop since successor has at most 1 child
            self.delete(successor_value)
            # Increase size becuase successor is not deleted but moved
            self.size += 1
            successor = Node(successor_value)
            successor.right = node.right
            successor.left = node.left
            self._update_parent(node, successor)
        self.size -= 1

    def _update_parent(self, node, new_node):
        if self.root == node:
            self.root = new_node
        else:
            node.parent.replace_child(node.value, new_node)

    def get_successor(self, node):
        current = node.right
        while current.left is not None:
            current = current.left
        return current

    def contains(self, element):
        return self.get(element) is not None

    def get(self, element):
        current = self.root
        while current is not None:
            if current.value == element:
                return current
            if current.value < element:
                current = current.right
            else:
                current = current.left
        return None



