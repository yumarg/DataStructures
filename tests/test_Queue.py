import unittest
import sys
sys.path.insert(0, sys.path[0].replace("/tests", ""))

from StackAndQueue.StacksAndQueues import Queue

class Test(unittest.TestCase):
	def setUp(self):
		self.queue = Queue()

	def tearDown(self):
		self.queue = None

	def testEnqueueToEmptyQueue(self):
		self.queue.enqueue(1)

		string = self.queue.toString()

		self.assertTrue(string == "Queue with the following elements from least recent to most recent:\n1")

	def testEnqueueToNonEmptyQueue(self):
		self.queue.enqueue(1)
		self.queue.enqueue(2)

		string = self.queue.toString()
		
		self.assertTrue(string == "Queue with the following elements from least recent to most recent:\n1, 2")

	def testDequeueFromEmptyQueue(self):
		self.assertTrue(self.queue.dequeue() == "ERROR")

	def testDequeueFromNonEmptyQueue(self):
		self.queue.enqueue(1)
		self.queue.enqueue(2)
		self.queue.enqueue(3)

		dequeued = self.queue.dequeue()

		string = self.queue.toString()

		self.assertTrue(dequeued == 1)
		self.assertTrue(string == "Queue with the following elements from least recent to most recent:\n2, 3")

	def testEmptyOnEmptyQueue(self):
		self.assertTrue(self.queue.empty())

	def testEmptyOnNonEmptyQueue(self):
		self.queue.enqueue(1)
		self.assertFalse(self.queue.empty())

if __name__ == '__main__':
    unittest.main()