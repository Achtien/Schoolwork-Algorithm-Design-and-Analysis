def depth_first_search(V):
	'''
	Find a path in directed graph with depth-first-search.

	Args:
		V(list): vertexes like (node1, node2, ..., noden). node1 to node n are integers. 0 for start, 1 for target.

	Return:
		path(list): nodes in path in order. None for not existing a path.
	'''
	def exist_path():
		while stack:
			v = stack.pop()
			for end in V[v]:
				if end == 1:
					parent[end] = v
					return 1
				elif end not in checked:	
					stack.append(end)
					parent[end] = v
		return
			
	parent = {}
	checked = [0]
	stack = [0]
	if exist_path():
		path = [1]
		while path[0] != 0:
			path.insert(0, parent[path[0]])
		return path
	else:
		return

if __name__ == '__main__':
	print(depth_first_search([(2,3,4),(),(5,),(6,),(7,),(1,),(1,),(6,)]))
