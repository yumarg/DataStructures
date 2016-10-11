import unittest
import sys
sys.path.insert(0, sys.path[0].replace("/tests", ""))

from BinaryHeap.binaryheap import BinaryMinHeap

class Test(unittest.TestCase):
	def setUp(self):
		self.binaryHeap = BinaryMinHeap(8)

	def tearDown(self):
		self.binaryHeap = None

	def testGetSizeOnEmptyHeap(self):
		size = self.binaryHeap.getSize()

		self.assertTrue(size == 0)

	def testGetSizeOnNonEmptyHeap(self):
		self.binaryHeap.insert(1)
		self.binaryHeap.insert(2)
		self.binaryHeap.insert(3)

		string = self.binaryHeap.toString()

		self.assertTrue(self.binaryHeap.getSize() == 3)
		self.assertTrue(string == "Binary Min Heap with elements:\n 1\n 2 3")

	def testInsertToEmptyHeap(self):
		self.binaryHeap.insert(3)

		string = self.binaryHeap.toString()

		self.assertTrue(self.binaryHeap.getSize() == 1)
		self.assertTrue(string == "Binary Min Heap with elements:\n 3")

	def testInsertToNonEmptyHeap(self):	
		self.binaryHeap.insert(1)
		self.binaryHeap.insert(4)
		self.binaryHeap.insert(5)
		self.binaryHeap.insert(3)
		self.binaryHeap.insert(6)
		self.binaryHeap.insert(7)
		self.binaryHeap.insert(0)
		self.binaryHeap.insert(2)

		string = self.binaryHeap.toString()
		print(string)

		self.assertTrue(self.binaryHeap.getSize() == 8)
		self.assertTrue(string == "Binary Min Heap with elements:\n 0\n 2 1\n 3 6 7 5\n 4")

	def testExtractMinFromEmptyHeap(self):
		self.assertTrue(self.binaryHeap.getSize() == 0)
		self.assertTrue(self.binaryHeap.extractMin() == "ERROR")

	def testExtractMinFromNonEmptyHeap(self):
		self.binaryHeap.insert(4)
		self.binaryHeap.insert(3)
		self.binaryHeap.insert(1)
		self.binaryHeap.insert(2)

		minE = self.binaryHeap.extractMin()

		string = self.binaryHeap.toString()

		self.assertTrue(self.binaryHeap.getSize() == 3)
		self.assertTrue(minE == 1)
		self.assertTrue(string == "Binary Min Heap with elements:\n 2\n 3 4")

	def testDeleteFromEmptyHeap(self):
		self.assertTrue(self.binaryHeap.getSize() == 0)
		self.assertTrue(self.binaryHeap.delete(1) == "ERROR")

	def testDeleteFromNonEmptyHeap(self):
		self.binaryHeap.insert(2)
		self.binaryHeap.insert(3)
		self.binaryHeap.insert(4)
		self.binaryHeap.insert(1)

		self.binaryHeap.delete(3)

		string = self.binaryHeap.toString()

		self.assertTrue(self.binaryHeap.getSize() == 3)
		self.assertTrue(string == "Binary Min Heap with elements:\n 1\n 4 2")

	def testDecreaseKeyFromEmptyHeap(self):
		self.binaryHeap.decreaseKey(1, 3)

		self.assertTrue(self.binaryHeap.getSize() == 0)

	def testDecreaseKeyFromNonEmptyHeap(self):
		self.binaryHeap.insert(4)
		self.binaryHeap.insert(2)
		self.binaryHeap.insert(3)
		self.binaryHeap.decreaseKey(4, 1)

		string = self.binaryHeap.toString()

		self.assertTrue(self.binaryHeap.getSize() == 3)
		self.assertTrue(string == "Binary Min Heap with elements:\n 1\n 2 3")

if __name__ == '__main__':
    unittest.main()