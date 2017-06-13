import unittest
import sys
sys.path.insert(0, sys.path[0].replace("/tests", ""))

from Hashtable.HashtableChaining import HashTableWithChaining, LinkedList, Node

class Test(unittest.TestCase):
    def setUp(self):
        self.table = HashTableWithChaining(5)

    def tearDown(self):
        self.table = None

    def testSearchInTable(self):
    	self.table.Insert(0)

    	self.assertTrue(self.table.Search(0)[0] is 0)
    	self.assertTrue(self.table.Search(0)[1] is 0)

    def testSearchNotInTable(self):
    	self.table.Insert(0)

    	self.assertTrue(self.table.Search(1) == "not there")

    def testInsertNotInTable(self):
    	self.table.Insert(0)

    	self.assertTrue(self.table.getSlot(0).head.getKey() == 0)
    	self.assertTrue(self.table.getSlot(0).head.getNext() is None)

    def testInsertInTable(self):
    	self.table.Insert(0)
    	self.assertTrue(self.table.Insert(0) == "already there")

    def testInsertToLinkedListInTableSlot(self):
    	self.table.Insert(0)
    	self.table.Insert(5)

    	self.assertTrue(self.table.getSlot(0).head.getKey() == 0)
    	self.assertTrue(self.table.getSlot(0).tail.getKey() == 5)

    def testDeleteInTable(self):
        self.table.Insert(0)
        self.table.Delete(0)

        self.assertTrue(self.table.getSlot(0).head == None)
        self.assertTrue(self.table.getSlot(0).tail == None)

    def testDeleteNotInTable(self):
        self.table.Insert(0)
        self.table.Insert(1)
        self.table.Insert(2)
        self.table.Delete(3)

        self.assertTrue(self.table.getSlot(3) == None)

    def testTableRemoveFirstElementFromLinkedList(self):
        self.table.Insert(0)
        self.table.Insert(1)
        self.table.Insert(5)
        self.table.Insert(10)
        self.table.Insert(11)
        self.table.Delete(0)

        self.assertTrue(self.table.getSlot(0).head.getKey() == 5)
        self.assertTrue(self.table.getSlot(0).head.getNext().getKey() == 10)
        self.assertTrue(self.table.getSlot(0).tail.getKey() == 10)
        self.assertTrue(self.table.getSlot(0).tail.getPrev().getKey() == 5)
        self.assertTrue(self.table.getSlot(1).head.getKey() == 1)
        self.assertTrue(self.table.getSlot(1).head.getNext().getKey() == 11)
        self.assertTrue(self.table.getSlot(1).tail.getKey() == 11)
        self.assertTrue(self.table.getSlot(1).tail.getPrev().getKey() == 1)

    def testTableRemoveLastElementFromLinkedList(self):
        self.table.Insert(0)
        self.table.Insert(1)
        self.table.Insert(5)
        self.table.Insert(10)
        self.table.Insert(11)
        self.table.Delete(10)

        self.assertTrue(self.table.getSlot(0).head.getKey() == 0)
        self.assertTrue(self.table.getSlot(0).head.getNext().getKey() == 5)
        self.assertTrue(self.table.getSlot(0).tail.getKey() == 5)
        self.assertTrue(self.table.getSlot(0).tail.getPrev().getKey() == 0)
        self.assertTrue(self.table.getSlot(1).head.getKey() == 1)
        self.assertTrue(self.table.getSlot(1).head.getNext().getKey() == 11)
        self.assertTrue(self.table.getSlot(1).tail.getKey() == 11)
        self.assertTrue(self.table.getSlot(1).tail.getPrev().getKey() == 1)

    def testTableRemoveMiddleElementFromLinkedList(self):
        self.table.Insert(0)
        self.table.Insert(1)
        self.table.Insert(5)
        self.table.Insert(10)
        self.table.Insert(11)
        self.table.Delete(5)

        self.assertTrue(self.table.getSlot(0).head.getKey() == 0)
        self.assertTrue(self.table.getSlot(0).head.getNext().getKey() == 10)
        self.assertTrue(self.table.getSlot(0).tail.getKey() == 10)
        self.assertTrue(self.table.getSlot(0).tail.getPrev().getKey() == 0)
        self.assertTrue(self.table.getSlot(1).head.getKey() == 1)
        self.assertTrue(self.table.getSlot(1).head.getNext().getKey() == 11)
        self.assertTrue(self.table.getSlot(1).tail.getKey() == 11)
        self.assertTrue(self.table.getSlot(1).tail.getPrev().getKey() == 1)

if __name__ == '__main__':
    unittest.main()