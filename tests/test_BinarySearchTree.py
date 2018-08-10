import unittest
import sys
sys.path.insert(0, sys.path[0].replace("/tests", ""))

from BinarySearchTree.BinarySearchTree import BinarySearchTree

class Test(unittest.TestCase):
	def setUp(self):
		self.binarySearchTree = BinarySearchTree()

	def tearDown(self):
		self.binarySearchTree = None

	def testInsertToEmptyBinarySearchTree(self):
		self.binarySearchTree.insert(5)

		string = self.binarySearchTree.toString()

		self.assertTrue(self.binarySearchTree.root.getKey() == 5)
		self.assertTrue(string == "Binary Search Tree with the root [Node with key: 5] and following nodes:\n[5]")

	def testInsertToNonEmptyBinarySearchTree(self):
		self.binarySearchTree.insert(5)
		self.binarySearchTree.insert(2)
		self.binarySearchTree.insert(1)
		self.binarySearchTree.insert(3)
		self.binarySearchTree.insert(9)
		self.binarySearchTree.insert(4)
		self.binarySearchTree.insert(7)
		self.binarySearchTree.insert(8)
		self.binarySearchTree.insert(6)

		string = self.binarySearchTree.toString()

		self.assertTrue(self.binarySearchTree.root.getKey() == 5)
		self.assertTrue(string == "Binary Search Tree with the root [Node with key: 5] and following nodes:\n[1, 2, 3, 4, 5, 6, 7, 8, 9]")

	def testDeleteFromEmptyBinarySearchTree(self):
		self.binarySearchTree.delete(4)

		string = self.binarySearchTree.toString()

		self.assertTrue(string == "empty Binary Search Tree")		

	def testDeleteLeafNodeFromNonEmptyBinarySearchTree(self):
		self.binarySearchTree.insert(5)
		self.binarySearchTree.insert(2)
		self.binarySearchTree.insert(1)
		self.binarySearchTree.insert(3)
		self.binarySearchTree.insert(9)
		self.binarySearchTree.insert(4)
		self.binarySearchTree.insert(7)
		self.binarySearchTree.insert(8)
		self.binarySearchTree.insert(6)
		self.binarySearchTree.delete(1)

		string = self.binarySearchTree.toString()

		self.assertTrue(self.binarySearchTree.root.getKey() == 5)
		self.assertTrue(string == "Binary Search Tree with the root [Node with key: 5] and following nodes:\n[2, 3, 4, 5, 6, 7, 8, 9]")

	def testDeleteOneChildNodeFromNonEmptyBinarySearchTree(self):
		self.binarySearchTree.insert(5)
		self.binarySearchTree.insert(2)
		self.binarySearchTree.insert(1)
		self.binarySearchTree.insert(3)
		self.binarySearchTree.insert(9)
		self.binarySearchTree.insert(4)
		self.binarySearchTree.insert(7)
		self.binarySearchTree.insert(8)
		self.binarySearchTree.insert(6)
		self.binarySearchTree.delete(1)
		self.binarySearchTree.delete(2)

		string = self.binarySearchTree.toString()

		self.assertTrue(self.binarySearchTree.root.getKey() == 5)
		self.assertTrue(string == "Binary Search Tree with the root [Node with key: 5] and following nodes:\n[3, 4, 5, 6, 7, 8, 9]")

	def testDeleteTwoChildrenNodeFromNonEmptyBinarySearchTree(self):
		self.binarySearchTree.insert(5)
		self.binarySearchTree.insert(2)
		self.binarySearchTree.insert(1)
		self.binarySearchTree.insert(3)
		self.binarySearchTree.insert(9)
		self.binarySearchTree.insert(4)
		self.binarySearchTree.insert(7)
		self.binarySearchTree.insert(8)
		self.binarySearchTree.insert(6)
		self.binarySearchTree.delete(1)
		self.binarySearchTree.delete(2)
		self.binarySearchTree.delete(7)

		string = self.binarySearchTree.toString()

		self.assertTrue(self.binarySearchTree.root.getKey() == 5)
		self.assertTrue(string == "Binary Search Tree with the root [Node with key: 5] and following nodes:\n[3, 4, 5, 6, 8, 9]")

	def testDeleteRootNodeFromNonEmptyBinarySearchTree(self):
		self.binarySearchTree.insert(5)
		self.binarySearchTree.insert(2)
		self.binarySearchTree.insert(1)
		self.binarySearchTree.insert(3)
		self.binarySearchTree.insert(9)
		self.binarySearchTree.insert(4)
		self.binarySearchTree.insert(7)
		self.binarySearchTree.insert(8)
		self.binarySearchTree.insert(6)
		self.binarySearchTree.delete(1)
		self.binarySearchTree.delete(2)
		self.binarySearchTree.delete(7)
		self.binarySearchTree.delete(5)

		string = self.binarySearchTree.toString()

		self.assertTrue(self.binarySearchTree.root.getKey() == 6)
		self.assertTrue(string == "Binary Search Tree with the root [Node with key: 6] and following nodes:\n[3, 4, 6, 8, 9]")

	def testFindFromEmptyBinarySearchTree(self):

		self.assertTrue(self.binarySearchTree.find(3) == False)

	def testFindFromNonEmptyBinarySearchTree(self):
		self.binarySearchTree.insert(5)
		self.binarySearchTree.insert(2)
		self.binarySearchTree.insert(1)
		self.binarySearchTree.insert(3)
		self.binarySearchTree.insert(9)
		self.binarySearchTree.insert(4)
		self.binarySearchTree.insert(7)
		self.binarySearchTree.insert(8)
		self.binarySearchTree.insert(6)
		self.binarySearchTree.delete(1)
		self.binarySearchTree.delete(2)
		self.binarySearchTree.delete(7)
		self.binarySearchTree.delete(5)

		self.assertTrue(self.binarySearchTree.find(3) == True)
		self.assertTrue(self.binarySearchTree.find(10) == False)

if __name__ == '__main__':
    unittest.main()