import operator

class Heap:
    def __init__(self, capacity=10, compare=operator.lt):
        self.capacity = 10
        self.elements = [None] * self.capacity
        self.compare = compare
        self.size = 0

    def __len__(self):
        return self.size

    def add(self, element):
        self.elements[self.size] = element
        self._bubble_up(self.size)
        self.size += 1
        if self.capacity == self.size:
            self._increase_size() 

    def _bubble_up(self, pos):
        if pos == 0:
            return
        parent = (pos - 1) // 2
        if not self._is_valid_parent(parent, pos):
            self._swap(parent, pos)
            self._bubble_up(parent)

    def poll(self):
        tmp = self.elements[0]
        self.elements[0] = self.elements[self.size - 1]
        self.elements[self.size - 1] = None
        self.size -= 1
        self._bubble_down(0)
        return tmp

    def _bubble_down(self, pos):
        if self._is_leaf(pos):
            return
        left_child_pos = 2 * pos + 1
        right_child_pos = 2 * pos + 2
        # Only left child is defined
        if right_child_pos == self.size:
            if self.compare(self.elements[left_child_pos], self.elements[pos]):
                self._swap(left_child_pos, pos)
                self._bubble_down(left_child_pos)
        else:
            left_child = self.elements[left_child_pos] 
            right_child = self.elements[right_child_pos]
            if self.compare(left_child, right_child):
                if not self._is_valid_parent(pos, left_child_pos):
                    self._swap(left_child_pos, pos)
                    self._bubble_down(left_child_pos)
            else:
                if not self._is_valid_parent(pos, right_child_pos):
                    self._swap(right_child_pos, pos)
                    self._bubble_down(right_child_pos)

    def _is_valid_parent(self, parent_pos, child_pos):
        return self.compare(self.elements[parent_pos], self.elements[child_pos])

    def _is_leaf(self, pos):
        return pos * 2 + 1 >= self.size 

    def _swap(self, first, second):
        tmp = self.elements[first]
        self.elements[first] = self.elements[second]
        self.elements[second] = tmp 

    def contains(self, element):
        return element in self.elements 

    def _increase_size(self):
        for _ in range(self.size):
            self.elements.append(None)
        self.capacity += self.size

    def _decrease_size(self):
        # TODO implement
        pass
