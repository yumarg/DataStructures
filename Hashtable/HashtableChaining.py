class Node:
	def __init__(self, k, position, prev=None, next=None):
		self.key = k
		self.position = position
		self.prev = prev
		self.next = next

	def getKey(self):
		return self.key

	def getPrev(self):
		return self.prev

	def setPrev(self, newPrev):
		self.prev = newPrev

	def getPos(self):
		return self.position

	def setPos(self, newPos):
		self.position = newPos

	def getNext(self):
		return self.next

	def setNext(self, newNext):
		self.next = newNext

class LinkedList:
	def __init__(self, location = 0, head=None, tail=None):
		self.location = location
		self.head = head
		self.tail = tail
		self.length = 0

	def add(self, k):
		if (self.find(k) == "not there"):
			newNode = Node(k, self.length, self.tail, None)
			if (self.length == 0):
				self.head = newNode
			else:
				self.tail.setNext(newNode)
			self.tail = newNode
			self.tail.setPos(self.length)
			self.length += 1
		else:
			return "already there"

	def remove(self, k):
		if (self.find(k) != "not there"):
			current = self.head
			previous = None
			current_position = 0
			while (current != None):
				if (current.getKey() == k):
					if previous is None and current.getNext() is None:
						# print "nothing in slot"
						self.head = None
						self.tail = None
					elif current.getNext() is None and previous is not None:
						# print "last element removed"
						previous.setNext(current.getNext())
						self.tail = current.getPrev()
					elif previous is None and current.getNext() is not None:
						# print "first element removed"
						current.getNext().setPos(0)
						self.head = current.getNext()
						current.getNext().setPrev(previous)
						node = current.getNext()
						while (node != None):
							node.setPos(node.getPos() - 1)
							node = node.getNext()
					else:
						current.getNext().setPos(current_position)
						current.getNext().setPrev(previous)						
						previous.setNext(current.getNext())
						node = current.getNext()
						while (node != None):
							node.setPos(node.getPos() - 1)
							node = node.getNext()
					self.length -= 1
					break
				else:
					current_position += 1
					previous = current
					current = current.getNext()
		else:
			return "not there"

	def find(self, k):
		current = self.head
		while (current != None):
			if (current.getKey() == k):
				return current
			else:
				current = current.getNext()
		if (current == None):
			return "not there"


class HashTableWithChaining:
	def __init__(self, capacity):
		self.capacity = capacity
		self.slots = [None] * self.capacity

	def h(self, k):
		return k % self.capacity

	def Insert(self, k):
		slot = self.h(k)
		found = self.Search(k)
		if (found == "not there"):
			if (self.slots[slot] == None):
				self.slots[slot] = LinkedList(slot)
			self.slots[slot].add(k)
		else:
			return "already there"

	def Delete(self, k):
		slot = self.h(k)
		if (self.Search(k) == "not there"):
			return "not there"
		else:
			self.slots[slot].remove(k)

	def Search(self, k):
		slot = self.h(k)
		location = self.slots[slot]
		if (location is None or location.find(k) == "not there"):
			return "not there"
		else:
			return (slot, location.find(k).position)

	def getSlot(self, slot):
		return self.slots[slot]