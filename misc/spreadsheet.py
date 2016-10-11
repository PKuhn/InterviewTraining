from collections import defaultdict 

class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __str__(self):
        return str(self._as_pair())

    def __hash__(position):
        return hash(position._as_pair())
    
    def _as_pair(self):
        return self.row, self.column


class SpreadSheet:
    def __init__(self):
        self.cells = {}
        self.target_to_summands = {}
        self.summand_to_target = defaultdict(set)
        self.cache = {}

    def get(self, position):
        if position in self.cells:
            return self.cells[position]
        if position in self.cache:
            return self.cache[position]
        if position in self.target_to_summands:
            try:
                result = sum([self.get(pos) for pos in self.target_to_summands[position]])
                self.cache[position] = result
                return result
            except ValueError:
                raise ValueError('One of the subfields not set')
        raise ValueError('Value is not set set')

    def set(self, position, value):
        if position in self.target_to_summands:
            raise ValueError('Sum fields can not be set.')
        self.cells[position] = value
        self._invalidate_cache(position)
        
    def add_sum(self, first, second, target):
        if not self._is_valid_sum(first, target):
            raise ValueError('Circular sum is invalid')
        if not self._is_valid_sum(second, target):
            raise ValueError('Circular sum is invalid')
        if target not in self.target_to_summands:
            self.target_to_summands[target] = set()
        self.target_to_summands[target].add(first)
        self.target_to_summands[target].add(second)
        self.summand_to_target[first].add(target)
        self.summand_to_target[second].add(target)
    
    def _invalidate_cache(self, position):
        if position in self.cache:
            del self.cache[position] 
        for target in self.summand_to_target[position]:
            self._invalidate_cache(target)

    def _is_valid_sum(self, summand, target):
        seen = set()
        summands = [summand]
        while len(summands) > 0:
            current = summands.pop()
            if current == target:
                return False
            if not current in seen:
                seen.add(current)
                if current in self.target_to_summands:
                    summands.extend(self.target_to_summands[current])
        return True
