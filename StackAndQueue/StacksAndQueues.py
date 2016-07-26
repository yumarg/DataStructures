class Stack:
	def __init__(self):
		self.stack = []

	def push(self, key):
		self.stack.append(key)

	def top(self):
		if (not self.empty()):
			return self.stack[len(self.stack)-1]
		return "ERROR"

	def pop(self):
		if (not self.empty()):
			last = self.stack[len(self.stack)-1]
			del self.stack[-1]
			return last
		return "ERROR"

	def empty(self):
		return (len(self.stack) == 0)

	def toString(self):
		string = "Stack with the following elements from least recent to most recent:\n"
		for e in self.stack:
			string += str(e) + ", "
		string = string[:-2]
		return string

class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, key):
		self.queue.append(key)

	def dequeue(self):
		if (not self.empty()):
			first = self.queue[0]
			del self.queue[0]
			return first
		return "ERROR"

	def empty(self):
		return (len(self.queue) == 0)

	def toString(self):
		string = "Queue with the following elements from least recent to most recent:\n"
		for e in self.queue:
			string += str(e) + ", "
		string = string[:-2]
		return string