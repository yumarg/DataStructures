import unittest
import sys
sys.path.insert(0, sys.path[0].replace("/tests", ""))

from Hashtable.HashtableOpenAddressing import HashTableWithOpenAddressing

class Test(unittest.TestCase):
    def setUp(self):
        self.table = HashTableWithOpenAddressing(5)

    def tearDown(self):
        self.table = None

    def testSearchInTable(self):
    	self.table.Insert(0)

    	self.assertTrue(self.table.Search(0) is 0)

    def testSearchNotInTable(self):
    	self.table.Insert(0)

    	self.assertTrue(self.table.Search(1) == "not there")

    def testInsertNotInTable(self):
    	self.table.Insert(0)

    	self.assertTrue(self.table.getSlot(0) == 0)

    def testInsertInTable(self):
    	self.table.Insert(0)
    	self.assertTrue(self.table.Insert(0) == "already there")

    def testDeleteInTable(self):
        self.table.Insert(0)
        self.table.Delete(0)

        self.assertTrue(self.table.getSlot(0) == "DELETED")
        self.assertTrue(self.table.Search(0) == "not there")

    def testDeleteNotInTable(self):
        self.table.Insert(0)
        self.table.Insert(1)
        self.table.Insert(2)
        self.table.Delete(3)
        self.table.Insert(8)

        self.assertTrue(self.table.getSlot(3) == 8)

if __name__ == '__main__':
    unittest.main()