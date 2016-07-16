import unittest
import sys
sys.path.insert(0, sys.path[0].replace("/tests", ""))

from LinkedList.LinkedLists import DoublyLinkedList

class Test(unittest.TestCase):
	def setUp(self):
		self.linkedList = DoublyLinkedList()

	def tearDown(self):
		self.linkedList = None

	def testEmptyOnEmptyLinkedList(self):
		isEmpty = self.linkedList.empty()

		string = self.linkedList.toString()

		self.assertTrue(isEmpty is True)
		self.assertTrue(string == "empty Doubly Linked List")		

	def testEmptyOnNonEmptyLinkedList(self):
		self.linkedList.append(1)
		isEmpty = self.linkedList.empty()

		string = self.linkedList.toString()

		self.assertTrue(isEmpty is False)
		self.assertTrue(string == "Doubly Linked List with the following nodes:\n\t - [Node with key: 1]\n")		

	def testAppendToEmptyLinkedList(self):
		self.linkedList.append(1)

		string = self.linkedList.toString()

		self.assertTrue(self.linkedList.getHead().getKey() == 1)
		self.assertTrue(self.linkedList.getTail().getKey() == 1)
		self.assertTrue(string == "Doubly Linked List with the following nodes:\n\t - [Node with key: 1]\n")

	def testAppendToNonEmptyLinkedList(self):
		self.linkedList.append(1)
		self.linkedList.append(2)
		self.linkedList.append(3)

		string = self.linkedList.toString()

		self.assertTrue(self.linkedList.getHead().getKey() == 1)
		self.assertTrue(self.linkedList.getTail().getKey() == 3)
		self.assertTrue(string == "Doubly Linked List with the following nodes:\n\t - [head]\t[Node with key: 1]\n\t - [Node with key: 2]\n\t - [tail]\t[Node with key: 3]\n")

	def testPrependToEmptyLinkedList(self):
		self.linkedList.prepend(1)

		string = self.linkedList.toString()

		self.assertTrue(self.linkedList.getHead().getKey() == 1)
		self.assertTrue(self.linkedList.getTail().getKey() == 1)
		self.assertTrue(string == "Doubly Linked List with the following nodes:\n\t - [Node with key: 1]\n")

	def testPrependToNonEmptyLinkedList(self):
		self.linkedList.append(2)
		self.linkedList.append(3)
		self.linkedList.prepend(1)

		string = self.linkedList.toString()	

		self.assertTrue(self.linkedList.getHead().getKey() == 1)
		self.assertTrue(self.linkedList.getTail().getKey() == 3)
		self.assertTrue(string == "Doubly Linked List with the following nodes:\n\t - [head]\t[Node with key: 1]\n\t - [Node with key: 2]\n\t - [tail]\t[Node with key: 3]\n")

	def testInsertAfterEmptyLinkedList(self):
		self.linkedList.insertAfter(1, 0)

		string = self.linkedList.toString()

		self.assertTrue(self.linkedList.empty() is True)
		self.assertTrue(string == "empty Doubly Linked List")		

	def testInsertAfterNonEmptyLinkedList(self):
		self.linkedList.append(1)
		self.linkedList.insertAfter(2, 1)
		self.linkedList.insertAfter(3, 2)

		string = self.linkedList.toString()

		self.assertTrue(self.linkedList.getHead().getKey() == 1)
		self.assertTrue(self.linkedList.getTail().getKey() == 3)
		self.assertTrue(string == "Doubly Linked List with the following nodes:\n\t - [head]\t[Node with key: 1]\n\t - [Node with key: 2]\n\t - [tail]\t[Node with key: 3]\n")

	def testInsertBeforeEmptyLinkedList(self):
		self.linkedList.insertBefore(0, 1)

		string = self.linkedList.toString()

		self.assertTrue(self.linkedList.empty() is True)
		self.assertTrue(string == "empty Doubly Linked List")

	def testInsertBeforeNonEmptyLinkedList(self):
		self.linkedList.append(3)
		self.linkedList.insertBefore(1, 3)
		self.linkedList.insertBefore(2, 3)

		string = self.linkedList.toString()

		self.assertTrue(self.linkedList.getHead().getKey() == 1)
		self.assertTrue(self.linkedList.getTail().getKey() == 3)
		self.assertTrue(string == "Doubly Linked List with the following nodes:\n\t - [head]\t[Node with key: 1]\n\t - [Node with key: 2]\n\t - [tail]\t[Node with key: 3]\n")	

	def testDeleteFromEmptyLinkedList(self):
		self.linkedList.delete(1)

		string = self.linkedList.toString()

		self.assertTrue(self.linkedList.empty() is True)
		self.assertTrue(string == "empty Doubly Linked List")		

	def testDeleteHeadFromNonEmptyLinkedList(self):
		self.linkedList.append(0)
		self.linkedList.append(1)
		self.linkedList.insertAfter(3, 1)
		self.linkedList.insertBefore(2, 3)
		self.linkedList.delete(0)

		string = self.linkedList.toString()

		self.assertTrue(self.linkedList.getHead().getKey() == 1)
		self.assertTrue(self.linkedList.getTail().getKey() == 3)
		self.assertTrue(string == "Doubly Linked List with the following nodes:\n\t - [head]\t[Node with key: 1]\n\t - [Node with key: 2]\n\t - [tail]\t[Node with key: 3]\n")

	def testDeleteMiddleNodeFromEmptyLinkedList(self):
		self.linkedList.prepend(2)
		self.linkedList.insertBefore(1, 2)
		self.linkedList.insertAfter(4, 1)		
		self.linkedList.append(3)		
		self.linkedList.delete(4)

		string = self.linkedList.toString()

		self.assertTrue(self.linkedList.getHead().getKey() == 1)
		self.assertTrue(self.linkedList.getTail().getKey() == 3)
		self.assertTrue(string == "Doubly Linked List with the following nodes:\n\t - [head]\t[Node with key: 1]\n\t - [Node with key: 2]\n\t - [tail]\t[Node with key: 3]\n")

	def testDeleteTailFromNonEmptyLinkedList(self):
		self.linkedList.append(2)
		self.linkedList.prepend(1)
		self.linkedList.insertAfter(4, 2)
		self.linkedList.append(3)
		self.linkedList.delete(4)

		string = self.linkedList.toString()

		self.assertTrue(self.linkedList.getHead().getKey() == 1)
		self.assertTrue(self.linkedList.getTail().getKey() == 3)
		self.assertTrue(string == "Doubly Linked List with the following nodes:\n\t - [head]\t[Node with key: 1]\n\t - [Node with key: 2]\n\t - [tail]\t[Node with key: 3]\n")

	def testFindFromEmptyLinkedList(self):
		self.linkedList.find(1)

		string = self.linkedList.toString()

		self.assertTrue(self.linkedList.empty() is True)
		self.assertTrue(string == "empty Doubly Linked List")

	def testFindFromNonEmptyLinkedList(self):
		self.linkedList.append(3)
		self.linkedList.prepend(1)
		self.linkedList.insertAfter(2, 1)

		self.assertTrue(self.linkedList.find(2).toString() == "[Node with key: 2]")

if __name__ == '__main__':
    unittest.main()