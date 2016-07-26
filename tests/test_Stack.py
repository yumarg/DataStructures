import unittest
import sys
sys.path.insert(0, sys.path[0].replace("/tests", ""))

from StackAndQueue.StacksAndQueues import Stack

class Test(unittest.TestCase):
	def setUp(self):
		self.stack = Stack()

	def tearDown(self):
		self.stack = None

	def testPushToEmptyStack(self):
		self.stack.push(1)

		string = self.stack.toString()

		self.assertTrue(string == "Stack with the following elements from least recent to most recent:\n1")

	def testPushToNonEmptyStack(self):
		self.stack.push(1)
		self.stack.push(2)

		string = self.stack.toString()
		
		self.assertTrue(string == "Stack with the following elements from least recent to most recent:\n1, 2")

	def testTopOfEmptyStack(self):
		self.assertTrue(self.stack.top() == "ERROR")

	def testTopOfNonEmptyStack(self):
		self.stack.push(1)
		self.stack.push(2)

		string = self.stack.toString()

		self.assertTrue(self.stack.top() == 2)
		self.assertTrue(string == "Stack with the following elements from least recent to most recent:\n1, 2")

	def testPopFromEmptyStack(self):
		self.assertTrue(self.stack.pop() == "ERROR")

	def testPopFromNonEmptyStack(self):
		self.stack.push(1)
		self.stack.push(2)
		self.stack.push(3)

		popped = self.stack.pop()

		string = self.stack.toString()

		self.assertTrue(popped == 3)
		self.assertTrue(string == "Stack with the following elements from least recent to most recent:\n1, 2")

	def testEmptyOnEmptyStack(self):
		self.assertTrue(self.stack.empty())

	def testEmptyOnNonEmptyStack(self):
		self.stack.push(1)
		self.assertFalse(self.stack.empty())

if __name__ == '__main__':
    unittest.main()