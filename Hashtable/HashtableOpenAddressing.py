class HashTableWithOpenAddressing:
	def __init__(self, capacity):
		self.capacity = capacity
		self.slots = [None] * capacity

	def h(self, k):
		return [((k % self.capacity) + i) % self.capacity for i in range(self.capacity)]

	def Insert(self, k):
		probeSequence = self.h(k)
		if self.Search(k) == "not there":
			for slot in probeSequence:
				if self.slots[slot] is None or self.slots[slot] == "DELETED":
					self.slots[slot] = k
					break
		else:
			return "already there"

	def Delete(self, k):
		if self.Search(k) == "not there":
			return "not there"
		else:
			self.slots[self.Search(k)] = "DELETED"

	def Search(self, k):
		probeSequence = self.h(k)
		for slot in probeSequence:
			if self.slots[slot] == k:
				return slot
		return "not there"

	def getSlot(self, slot):
		return self.slots[slot]