from heap import MinHeap

def test_add():
    heap = MinHeap()
    heap.add(2)
    heap.add(3)
    heap.add(1)
    assert heap.contains(1)
    assert heap.contains(2)
    assert heap.contains(3)

def test_heap_ordered():
    heap = MinHeap()
    heap.add(2)
    heap.add(7)
    heap.add(1)
    heap.add(8)
    heap.add(3)
    heap.add(0)
    heap.add(4)
    heap.add(6)
    heap.add(5)
    extracted = [] 
    while len(heap) > 0:
        extracted.append(heap.poll())
    assert extracted == sorted(range(9))
