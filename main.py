def average(nums):
    """Calculate the average of a list of nums."""
    if not nums:
        return 0
    return sum(nums) / len(nums)

def median(nums):
    """Calculate the median of a list of integers."""
    n = len(nums)
    if n == 0:
        return 0
    nums_sorted = sorted(nums)
    mid = n // 2
    if n % 2 == 0:
        return (nums_sorted[mid - 1] + nums_sorted[mid]) / 2
    else:
        return nums_sorted[mid]

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


class TreeNode:
    """Node class for binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    """Binary Tree implementation with BST validation."""
    
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, val):
        """Insert a value into the binary tree (not necessarily BST order)."""
        if not self.root:
            self.root = TreeNode(val)
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = TreeNode(val)
                return
            if not node.right:
                node.right = TreeNode(val)
                return
            queue.append(node.left)
            queue.append(node.right)
    
    def insert_bst(self, val):
        """Insert a value into the binary search tree maintaining BST property."""
        if not self.root:
            self.root = TreeNode(val)
            return
        
        def _insert_recursive(node, val):
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    _insert_recursive(node.left, val)
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    _insert_recursive(node.right, val)
        
        _insert_recursive(self.root, val)
    
    def is_bst(self):
        """Check if the binary tree is a valid Binary Search Tree."""
        def _is_bst_helper(node, min_val=float('-inf'), max_val=float('inf')):
            if node is None:
                return True
            
            # Check if current node's value is within valid range
            if not (min_val < node.val < max_val):
                return False
            
            # Recursively check left and right subtrees
            return (_is_bst_helper(node.left, min_val, node.val) and 
                    _is_bst_helper(node.right, node.val, max_val))
        
        return _is_bst_helper(self.root)
    
    def inorder_traversal(self):
        """Perform inorder traversal of the tree."""
        result = []
        
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.val)
                _inorder(node.right)
        
        _inorder(self.root)
        return result
    
    def print_tree(self):
        """Print the tree structure (simple level-order representation)."""
        if not self.root:
            print("Empty tree")
            return
        
        queue = [self.root]
        level = 0
        while queue:
            level_size = len(queue)
            print(f"Level {level}: ", end="")
            for _ in range(level_size):
                node = queue.pop(0)
                if node:
                    print(f"{node.val} ", end="")
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    print("None ", end="")
            print()
            level += 1
            if all(node is None for node in queue):
                break


def test_bst_validation():
    """Test function to demonstrate BST validation."""
    print("=== Testing BST Validation ===")
    
    # Test 1: Create a valid BST
    print("\nTest 1: Valid BST")
    bst = BinaryTree()
    values = [5, 3, 7, 1, 4, 6, 8]
    for val in values:
        bst.insert_bst(val)
    
    print("Tree structure:")
    bst.print_tree()
    print(f"Inorder traversal: {bst.inorder_traversal()}")
    print(f"Is BST: {bst.is_bst()}")
    
    # Test 2: Create an invalid BST (regular binary tree)
    print("\nTest 2: Invalid BST (regular binary tree)")
    invalid_bst = BinaryTree()
    values = [5, 3, 7, 1, 4, 6, 8]
    for val in values:
        invalid_bst.insert(val)  # Using regular insert, not BST insert
    
    print("Tree structure:")
    invalid_bst.print_tree()
    print(f"Inorder traversal: {invalid_bst.inorder_traversal()}")
    print(f"Is BST: {invalid_bst.is_bst()}")
    
    # Test 3: Create another invalid BST with wrong structure
    print("\nTest 3: Invalid BST with wrong structure")
    invalid_bst2 = BinaryTree()
    invalid_bst2.root = TreeNode(5)
    invalid_bst2.root.left = TreeNode(6)  # Left child > parent
    invalid_bst2.root.right = TreeNode(3)  # Right child < parent
    
    print("Tree structure:")
    invalid_bst2.print_tree()
    print(f"Inorder traversal: {invalid_bst2.inorder_traversal()}")
    print(f"Is BST: {invalid_bst2.is_bst()}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm says hello')
    numbers = [10, 20, 30, 40, 50]
    # avg = average(numbers)
    # print(f'The average of {numbers} is {avg}')
    med = median(numbers)
    print(f'The median of {numbers} is {med}')
    
    # Run BST validation tests
    test_bst_validation()