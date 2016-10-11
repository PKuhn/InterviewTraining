class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__
    
    def _as_pair(self):
        return self.row, self.column

    def __hash__(position):
        return hash(position._as_pair())

class SpreadSheet:
    def __init__(self):
        self.cells = {}
        self.sums = {}

    def get(self, position):
        if position in self.cells:
            return self.cells[position]
        if position in self.sums:
            try:
                return sum([self.get(pos) for pos in self.sums[position]])
            except ValueError:
                raise ValueError('One of the subfields not set')
        raise ValueError('Value is not set set')

    def set(self, position, value):
        if position in self.sums:
            raise ValueError('Sum fields can not be set.')
        self.cells[position] = value
        
    def add_sum(self, first, second, target):
        if not self._is_valid_sum(first, target):
            raise ValueError('Circular sum is invalid')
        if not self._is_valid_sum(second, target):
            raise ValueError('Circular sum is invalid')
        if target not in self.sums:
            self.sums[target] = set()
        self.sums[target].add(first)
        self.sums[target].add(second)
    
    def _is_valid_sum(self, summand, target):
        seen = set()
        summands = [summand]
        while len(summands) > 0:
            current = summands.pop()
            if current == target:
                return False
            if not current in seen:
                seen.add(current)
                if current in self.sums:
                    summands.extend(self.sums[current])
        return True
