from bst import BinarySearchTree

def test_multiple_adds():
    tree = BinarySearchTree()
    tree.add(3)
    tree.add(1)
    tree.add(9)
    tree.add(6)
    assert(len(tree) == 4)

def test_add_to_empty_tree():
    tree = BinarySearchTree()
    tree.add(3)
    assert(len(tree) == 1)
    assert(tree.contains(3))

def test_element_only_added_once():
    tree = BinarySearchTree()
    tree.add(3)
    tree.add(3)
    assert(len(tree) == 1)

def test_delete_two_children():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(3)
    tree.add(6)
    tree.add(2)
    tree.delete(3)
    assert(tree.contains(3) is False)
    assert(len(tree) == 3)

def test_delete_root():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(3)
    tree.add(6)
    tree.add(2)
    tree.delete(1)
    assert(tree.root.value == 3)

def test_parent_pointer_after_delete():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(3)
    tree.add(6)
    tree.delete(3)
    assert(tree.get(6).parent.value == 1)

def test_delete_without_children():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(3)
    tree.add(6)
    tree.delete(6)
    assert(tree.get(3).childcount() == 0)

def test_delete_successor_with_children():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(5)
    tree.add(4)
    tree.add(10)
    tree.add(9)
    tree.add(7)
    tree.add(8)
    tree.delete(5)
    assert(tree.get(9).get_only_child().value == 8)
