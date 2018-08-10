class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
    
    def getKey(self):
        return self.key
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

    def setKey(self, newKey):
    	self.key = newKey
    
    def setLeft(self, newLeft):
        self.left = newLeft
    
    def setRight(self, newRight):
        self.right = newRight

    def toString(self):
        string = "[Node with key: " + str(self.key) + "]"
        return string

class BinarySearchTree:
	def __init__(self, root=None):
		self.root = root

	def getMinNode(self, node):
		if not node.getLeft():
			return node
		return self.getMinNode(node.getLeft())

	# Worst case O(n), Best case O(log(n))
	def insert(self, key):
		def insertHelper(curr, key):
			if not curr:
				curr = Node(key)
				if not self.root:
					self.root = curr
			# insert in left subtree
			elif key < curr.getKey():
				curr.setLeft(insertHelper(curr.getLeft(), key))
			# insert in right subtree
			else:
				curr.setRight(insertHelper(curr.getRight(), key))
			return curr
		insertHelper(self.root, key)

	# Worst case O(n), Best case O(log(n))
	def find(self, key):
		def findHelper(curr, key):
			if not curr:
				return False
			# found
			if key == curr.getKey():
				return True
			# find in left subtree
			if key < curr.getKey():
				return findHelper(curr.getLeft(), key)
			# find in right subtree
			else:
				return findHelper(curr.getRight(), key)
		return findHelper(self.root, key)

	# Worst case O(n), Best case O(log(n))
	def delete(self, key):
		def deleteHelper(curr, key):
			# if empty
			if not curr:
				return curr
			# if delete in left subtree
			if key < curr.getKey():
				curr.setLeft(deleteHelper(curr.getLeft(), key))
			# if delete in right subtree
			elif key > curr.getKey():
				curr.setRight(deleteHelper(curr.getRight(), key))
			# if node to delete
			else:
				# if no right child
				if not curr.getRight():
					return curr.getLeft()
				# no left child
				if not curr.getLeft():
					return curr.getRight()
				# two children
				minValNode = self.getMinNode(curr.getRight())
				curr.setKey(minValNode.getKey())
				curr.setRight(deleteHelper(curr.getRight(),curr.getKey()))
			return curr
		deleteHelper(self.root, key)

	# O(n)
	def traverseInOrder(self):
		def traverseInOrderHelper(curr, nodes):
			if curr:
				# get left subtree
				traverseInOrderHelper(curr.getLeft(), nodes)
				# get current node
				nodes.append(curr.getKey())
				# get right subtree
				traverseInOrderHelper(curr.getRight(), nodes)
				return nodes
		return str(traverseInOrderHelper(self.root, []))

	# O(n)
	def isBST(self):
		def isBSTHelper(curr, minVal, maxVal):
			# empty
			if not curr:
				return True
			# curr violates min / max constraint
			if minVal > curr.getKey() or maxVal < curr.getKey():
				return False
			# check subtrees
			return isBSTHelper(curr.getLeft(), minVal, curr.getKey()-1) and isBSTHelper(curr.getRight(), curr.getKey()+1, maxVal)
		return isBSTHelper(self.root, -float("inf"), float("inf"))

	def toString(self):
		if not self.root:
			return "empty Binary Search Tree"
		return "Binary Search Tree with the root " + self.root.toString() + " and following nodes:\n" + self.traverseInOrder()