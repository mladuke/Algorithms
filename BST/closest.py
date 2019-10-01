def findClosestValueInBst(tree, target):
    # Write your code here.
	node = tree
	delta = 1000000000000000
	closest = None
	path = True
	while (path):
		path = False
		current = node.value
		if (current == target):
			return target
		elif (current < target):
			if ((target-current)<delta):
				delta = target-current
				closest = current
			if (node.right!=None):
				node = node.right
				path = True
		elif (current > target):
			if ((current-target)<delta):
				delta = current-target
				closest = current
			if (node.left !=None):
				node = node.left
				path = True
	return closest

    def findClosestValueInBst(tree, target):
        # Write your code here.
	node = tree
	delta = 1000000000000000
	closest = None
	path = True
	while (path):
		path = False
		current = node.value
		if (current == target):
			return target
		elif (current < target):
			if ((target-current)<delta):
				delta = target-current
				closest = current
			if (node.right!=None):
				node = node.right
				path = True
		elif (current > target):
			if ((current-target)<delta):
				delta = current-target
				closest = current
			if (node.left !=None):
				node = node.left
				path = True
	return closest