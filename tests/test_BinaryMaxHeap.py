import unittest
import sys
sys.path.insert(0, sys.path[0].replace("/tests", ""))

from BinaryHeap.binaryheap import BinaryMaxHeap

class Test(unittest.TestCase):
	def setUp(self):
		self.binaryHeap = BinaryMaxHeap(8)

	def tearDown(self):
		self.binaryHeap = None

	def testGetSizeOnEmptyHeap(self):
		size = self.binaryHeap.getSize()

		self.assertTrue(size == 0)

	def testGetSizeOnNonEmptyHeap(self):
		self.binaryHeap.insert(3)
		self.binaryHeap.insert(2)
		self.binaryHeap.insert(1)

		string = self.binaryHeap.toString()

		self.assertTrue(self.binaryHeap.getSize() == 3)
		self.assertTrue(string == "Binary Max Heap with elements:\n 3\n 2 1")

	def testInsertToEmptyHeap(self):
		self.binaryHeap.insert(3)

		string = self.binaryHeap.toString()

		self.assertTrue(self.binaryHeap.getSize() == 1)
		self.assertTrue(string == "Binary Max Heap with elements:\n 3")

	def testInsertToNonEmptyHeap(self):	
		self.binaryHeap.insert(4)
		self.binaryHeap.insert(3)
		self.binaryHeap.insert(5)
		self.binaryHeap.insert(1)
		self.binaryHeap.insert(6)
		self.binaryHeap.insert(7)
		self.binaryHeap.insert(0)
		self.binaryHeap.insert(2)

		string = self.binaryHeap.toString()

		self.assertTrue(self.binaryHeap.getSize() == 8)
		self.assertTrue(string == "Binary Max Heap with elements:\n 7\n 5 6\n 2 3 4 0\n 1")

	def testExtractMaxFromEmptyHeap(self):
		self.assertTrue(self.binaryHeap.getSize() == 0)
		self.assertTrue(self.binaryHeap.extractMax() == "ERROR")

	def testExtractMaxFromNonEmptyHeap(self):
		self.binaryHeap.insert(4)
		self.binaryHeap.insert(3)
		self.binaryHeap.insert(1)
		self.binaryHeap.insert(2)

		maxE = self.binaryHeap.extractMax()

		string = self.binaryHeap.toString()

		self.assertTrue(self.binaryHeap.getSize() == 3)
		self.assertTrue(maxE == 4)
		self.assertTrue(string == "Binary Max Heap with elements:\n 3\n 1 2")

	def testDeleteFromEmptyHeap(self):
		self.assertTrue(self.binaryHeap.getSize() == 0)
		self.assertTrue(self.binaryHeap.delete(1) == "ERROR")

	def testDeleteFromNonEmptyHeap(self):
		self.binaryHeap.insert(4)
		self.binaryHeap.insert(3)
		self.binaryHeap.insert(1)
		self.binaryHeap.insert(2)

		self.binaryHeap.delete(3)

		string = self.binaryHeap.toString()

		self.assertTrue(self.binaryHeap.getSize() == 3)
		self.assertTrue(string == "Binary Max Heap with elements:\n 4\n 1 2")

	def testIncreaseKeyFromEmptyHeap(self):
		self.binaryHeap.increaseKey(1, 3)

		self.assertTrue(self.binaryHeap.getSize() == 0)

	def testIncreaseKeyFromNonEmptyHeap(self):
		self.binaryHeap.insert(1)
		self.binaryHeap.insert(2)
		self.binaryHeap.insert(3)
		self.binaryHeap.increaseKey(1, 4)

		string = self.binaryHeap.toString()

		self.assertTrue(self.binaryHeap.getSize() == 3)
		self.assertTrue(string == "Binary Max Heap with elements:\n 4\n 3 2")

if __name__ == '__main__':
    unittest.main()