import math

class BinaryMaxHeap:
	def __init__(self, capacity):
		self.maxSize = capacity
		self.heap = []

	def getParent(self, i):
		return int(math.floor(float(i-1)/2))

	def getLeftChild(self, i):
		return 2*i+1

	def getRightChild(self, i):
		return 2*i+2

	def getMax(self):
		return self.heap[0]

	def getSize(self):
		return len(self.heap)

	def swap(self, i1, i2):
		temp = self.heap[i1]
		self.heap[i1] = self.heap[i2]
		self.heap[i2] = temp

	def insert(self, p):
		size = self.getSize()
		if size == self.maxSize:
			return "ERROR"
		self.heap.append(p)
		self.maxHeapify(size)

	def maxHeapify(self, i):
		if (self.getParent(i) >= 0):
			if (self.heap[self.getParent(i)] < self.heap[i]):
				self.swap(self.getParent(i), i)
				self.maxHeapify(self.getParent(i))

	def extractMax(self):
		if (self.getSize() == 0):
			return "ERROR"
		return self.heap.pop(0)

	def delete(self, p):
		if (p not in self.heap):
			return "ERROR"
		index = self.heap.index(p)
		self.heap[index] = float('inf')
		self.maxHeapify(index)
		self.extractMax()

	def increaseKey(self, p, newp):
		if (p in self.heap):
			index = self.heap.index(p)
			self.heap[index] = newp
			self.maxHeapify(index)

	def toString(self):
		string = "Binary Max Heap with elements:\n"
		expCount = 1
		indexCount = 0
		while (expCount <= int(math.floor(math.log(self.getSize(), 2)))+1):
			while(indexCount < min(pow(2, expCount)-1, self.getSize())):
				string += " " + str(self.heap[indexCount])
				indexCount += 1
			string += "\n"
			expCount += 1
		string = string[:-1]
		return string

class BinaryMinHeap:
	def __init__(self, capacity):
		self.maxSize = capacity
		self.heap = []

	def getParent(self, i):
		return int(math.floor(float(i-1)/2))

	def getLeftChild(self, i):
		return 2*i+1

	def getRightChild(self, i):
		return 2*i+2

	def getMin(self):
		return self.heap[0]

	def getSize(self):
		return len(self.heap)

	def swap(self, i1, i2):
		temp = self.heap[i1]
		self.heap[i1] = self.heap[i2]
		self.heap[i2] = temp

	def insert(self, p):
		size = self.getSize()
		if size == self.maxSize:
			return "ERROR"
		self.heap.append(p)
		self.minHeapify(size)

	def minHeapify(self, i):
		if (self.getParent(i) >= 0):
			if (self.heap[self.getParent(i)] > self.heap[i]):
				self.swap(self.getParent(i), i)
				self.minHeapify(self.getParent(i))

	def extractMin(self):
		if (self.getSize() == 0):
			return "ERROR"
		return self.heap.pop(0)

	def delete(self, p):
		if (p not in self.heap):
			return "ERROR"
		index = self.heap.index(p)
		self.heap[index] = float('-inf')
		self.minHeapify(index)
		self.extractMin()

	def decreaseKey(self, p, newp):
		if (p in self.heap):
			index = self.heap.index(p)
			self.heap[index] = newp
			self.minHeapify(index)

	def toString(self):
		string = "Binary Min Heap with elements:\n"
		expCount = 1
		indexCount = 0
		while (expCount <= int(math.floor(math.log(self.getSize(), 2)))+1):
			while(indexCount < min(pow(2, expCount)-1, self.getSize())):
				string += " " + str(self.heap[indexCount])
				indexCount += 1
			string += "\n"
			expCount += 1
		string = string[:-1]
		return string