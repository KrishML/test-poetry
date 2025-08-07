import unittest
from main import average, median, sum_numbers, print_hi, TreeNode, BinaryTree

class TestMain(unittest.TestCase):
    def test_average(self):
        """Test the average function."""
        input_data = [1, 2, 3, 4, 5]
        expected_output = 3
        self.assertEqual(average(input_data), expected_output)
        
        # Test empty list
        self.assertEqual(average([]), 0)
        
        # Test single element
        self.assertEqual(average([10]), 10)

    def test_median(self):
        """Test the median function."""
        # Test odd number of elements
        self.assertEqual(median([1, 3, 5, 7, 9]), 5)
        
        # Test even number of elements
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        
        # Test empty list
        self.assertEqual(median([]), 0)
        
        # Test single element
        self.assertEqual(median([5]), 5)

class TestTreeNode(unittest.TestCase):
    def test_treenode_creation(self):
        """Test TreeNode creation and attributes."""
        node = TreeNode(10)
        self.assertEqual(node.val, 10)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)
        
        # Test with children
        left_child = TreeNode(5)
        right_child = TreeNode(15)
        node = TreeNode(10, left_child, right_child)
        self.assertEqual(node.val, 10)
        self.assertEqual(node.left, left_child)
        self.assertEqual(node.right, right_child)

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.tree = BinaryTree()
    
    def test_empty_tree(self):
        """Test empty tree operations."""
        self.assertIsNone(self.tree.root)
        self.assertTrue(self.tree.is_bst())
        self.assertEqual(self.tree.inorder_traversal(), [])
    
    def test_single_node_tree(self):
        """Test tree with single node."""
        self.tree.root = TreeNode(5)
        self.assertTrue(self.tree.is_bst())
        self.assertEqual(self.tree.inorder_traversal(), [5])
    
    def test_valid_bst_creation(self):
        """Test creating a valid BST."""
        values = [5, 3, 7, 1, 4, 6, 8]
        for val in values:
            self.tree.insert_bst(val)
        
        self.assertTrue(self.tree.is_bst())
        self.assertEqual(self.tree.inorder_traversal(), [1, 3, 4, 5, 6, 7, 8])
    
    def test_invalid_bst_detection(self):
        """Test detection of invalid BST."""
        # Create an invalid BST: root=5, left=6, right=3
        self.tree.root = TreeNode(5)
        self.tree.root.left = TreeNode(6)  # Left child > parent
        self.tree.root.right = TreeNode(3)  # Right child < parent
        
        self.assertFalse(self.tree.is_bst())
        self.assertEqual(self.tree.inorder_traversal(), [6, 5, 3])
    
    def test_another_invalid_bst(self):
        """Test another invalid BST case."""
        # Create a tree that looks like a BST but isn't
        # Root: 10, Left: 5, Right: 15, Left.Left: 7 (should be <= 5)
        self.tree.root = TreeNode(10)
        self.tree.root.left = TreeNode(5)
        self.tree.root.right = TreeNode(15)
        self.tree.root.left.left = TreeNode(7)  # 7 > 5, invalid
        
        self.assertFalse(self.tree.is_bst())
    
    def test_complex_valid_bst(self):
        """Test a more complex valid BST."""
        # Create a complex but valid BST
        self.tree.root = TreeNode(10)
        self.tree.root.left = TreeNode(5)
        self.tree.root.right = TreeNode(15)
        self.tree.root.left.left = TreeNode(3)
        self.tree.root.left.right = TreeNode(7)
        self.tree.root.right.left = TreeNode(12)
        self.tree.root.right.right = TreeNode(18)
        
        self.assertTrue(self.tree.is_bst())
        self.assertEqual(self.tree.inorder_traversal(), [3, 5, 7, 10, 12, 15, 18])
    
    def test_duplicate_values(self):
        """Test BST with duplicate values (should be invalid by strict definition)."""
        # Create BST with duplicates
        self.tree.root = TreeNode(5)
        self.tree.root.left = TreeNode(3)
        self.tree.root.right = TreeNode(5)  # Duplicate value
        
        # Current implementation doesn't allow duplicates (uses < and >)
        # This test documents the current behavior
        self.assertFalse(self.tree.is_bst())
    
    def test_insert_methods(self):
        """Test both insert methods."""
        # Test regular insert (level-order)
        tree1 = BinaryTree()
        values = [5, 3, 7, 1, 4]
        for val in values:
            tree1.insert(val)
        
        # Test BST insert
        tree2 = BinaryTree()
        for val in values:
            tree2.insert_bst(val)
        
        # Both should be valid BSTs in this case due to the specific values
        self.assertTrue(tree1.is_bst())
        self.assertTrue(tree2.is_bst())
    
    def test_edge_cases(self):
        """Test edge cases for BST validation."""
        # Test with negative values
        self.tree.root = TreeNode(0)
        self.tree.root.left = TreeNode(-5)
        self.tree.root.right = TreeNode(5)
        
        self.assertTrue(self.tree.is_bst())
        
        # Test with float values
        self.tree.root = TreeNode(3.5)
        self.tree.root.left = TreeNode(1.2)
        self.tree.root.right = TreeNode(7.8)
        
        self.assertTrue(self.tree.is_bst())
    
    def test_large_bst(self):
        """Test a larger BST to ensure scalability."""
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
        for val in values:
            self.tree.insert_bst(val)
        
        self.assertTrue(self.tree.is_bst())
        expected_inorder = sorted(values)
        self.assertEqual(self.tree.inorder_traversal(), expected_inorder)


class TestMainFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3)
        self.assertEqual(average([]), 0)
        self.assertEqual(average([10]), 10)
        self.assertAlmostEqual(average([1, 2]), 1.5)

    def test_median(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([]), 0)
        self.assertEqual(median([7]), 7)
        self.assertEqual(median([2, 1]), 1.5)

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_numbers([]), 0)
        self.assertEqual(sum_numbers([10]), 10)

    def test_print_hi(self):
        # Test print_hi by capturing stdout
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_hi('Tester')
        sys.stdout = sys.__stdout__
        self.assertIn('Hi, Tester', captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()