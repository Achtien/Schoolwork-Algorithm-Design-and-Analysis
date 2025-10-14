def breadth_first_search(E):
	'''
	Find the shortest path in directed graph with breadth-first-search.

	Args:
		E(list): edges like (node1, node2). node1 to noden are integers. 0 for start, 1 for target.

	Return:
		path(list): nodes in path in order. None for not existing a path.
	'''
	def choose_edge(v):
		for e in E_remain:
			if v in e:
				v_ = [v_ for v_ in e if v_ != v][0]
				if v_ == 1:
					parent[v_] = v
					return 1
				elif v_ not in parent.values() and v_ not in parent.keys():
					parent[v_] = v
					queue.append(v_)
		return None

	queue = []
	E_remain = E[:]
	parent = {}
	exist = False

	choose_edge(0)
	while queue:
		v = queue.pop(0)
		if choose_edge(v): 
			exist = True
			break

	if exist:
		path = [1]
		while path[0] != 0:
			path.insert(0, parent[path[0]])
		return path

	else: return


def breadth_first_search_1(V):
	'''
	Find the shortest path in undirected graph with breadth-first-search.

	Args:
		V(list): Vertex like (node1, node2, ..., noden). node1 node2 ... are integers representing nodes could go from node<order>. 0 for start node, 1 for target node.

	Return:
		path(list): nodes in path in order.
	'''
	def exist_path():
		while queue:
			v = queue.pop(0)
			for end in V[v]:
				if end == 1:
					parent[end] = v
					return 1
				else:
					queue.append(end)
					parent[end] = v
		return

	parent = {}
	queue = [0]
	if exist_path():
		path = [1]
		while path[0] != 0:
			path.insert(0, parent[path[0]])
		return path
	else:
		return


if __name__ == '__main__':
	pass
	print(breadth_first_search([(0,2),(0,3),(0,4),(2,5),(3,6),(6,1),(4,7),(7,1)]))
	print(breadth_first_search_1([(2,3,4),(),(5,6),(6,),(7,),(),(1,),(1,)]))
