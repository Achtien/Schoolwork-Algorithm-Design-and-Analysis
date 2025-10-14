def max_flow(C):
	'''
	Solve the max flow problem with Fork-Fulkerson algorithm.

	Args:
		G: graph dictionary {node: [neighbors]}, 0 for source, 1 for sink.
		C: capacity dictionary {(u, v): capacity}

	Returns:
		flow: max flow.
	'''
	
	# make function to find path, given C_residual. DFS.
	def search_path(C_residual):
		def exists_path():
			while stack:
				# pop out a node as v
				v = stack.pop()
				# find all edges in C_residule that edge[0] = v and c != 0
				edges = []
				for edge in C_residual.keys():
					if edge[0] == v and C_residual[edge] != 0:
						# if edge[1] == 1(sink): link to v and return
						if edge[1] == 1:
							parent[edge[1]] = v
							return 1
						# else: add node edge[1] to stack and link to v.
						else:
							stack.append(edge[1])
							parent[edge[1]] = v
			return None
		# make a stack
		stack = [0]
		# make a parent dictionary to record path
		parent = {}

		if exists_path():
			# have parent, make path like [(0,2),(2,3),(3,1)]
			# find parent[1], and add (parent[1],1) left of path
			path = [(parent[1], 1)]
			v = path[0][0]
			while v != 0:
				print(path)
				path.insert(0, (parent[v], v))
				v = parent[v]
			return path
		else:
			return None


	flow = 0
	C_residual = C.copy()
	# with a path, make a residual graph
	path = search_path(C_residual)
	while path:
		# for every edge in the path capacity minus 1 until a capacity down to 0, record it and stop outer loop after this inner loop.
		bottle_neck = False
		while not bottle_neck:
			for edge in path:
				# for edge in path, C_residual[edge] -= 1.
				C_residual[edge] -= 1
				if C_residual[edge] == 0:
					bottle_neck = True
			flow += 1
		# find another path and repeat
		path = search_path(C_residual)	
			
	return flow

if __name__ == '__main__':
	test1 = {
		(0, 2): 5,
	    (2, 1): 5
	}
	capacities_1 = {
    (0, 2): 10,
    (0, 3): 10,
    (2, 1): 10,
    (3, 1): 10
	}
	capacities_2 = {
    (0, 2): 15,
    (0, 3): 15,
    (2, 4): 10,  # 瓶颈
    (3, 4): 5,   # 瓶颈
    (4, 1): 15
	}
	capacities_3 = {
    (0, 2): 10,
    (0, 3): 5,
    (2, 3): 15,
    (2, 1): 10,
    (3, 1): 15
	}
	capacities_4 = {
    (0, 2): 8,
    (0, 3): 4,
    (0, 4): 6,
    (2, 5): 5,
    (3, 5): 3,
    (4, 5): 4,
    (5, 1): 12
	}
	capacities_5 = {
    (0, 2): 16,
    (0, 3): 13,
    (2, 3): 10,
    (3, 2): 4,
    (2, 4): 12,
    (3, 5): 14,
    (4, 3): 9,
    (4, 1): 20,
    (5, 4): 7,
    (5, 1): 4
	}
	capacities_6 = {
    (0, 2): 100,
    (0, 3): 100,
    (0, 4): 100,
    (2, 5): 50,  # 瓶颈
    (3, 5): 50,  # 瓶颈
    (4, 5): 50,  # 瓶颈
    (5, 1): 150
	}
	capacities_7 = {
    (0, 2): 10,
    (0, 3): 10,
    (4, 1): 10,
    (5, 1): 10
	}
	capacities_8 = {
    (0, 2): 5,
    (2, 3): 5,
    (3, 1): 5
	}
	print(max_flow(test1))
	print(max_flow(capacities_1))
	print(max_flow(capacities_2))
	print(max_flow(capacities_3))
	print(max_flow(capacities_4))
	print(max_flow(capacities_5))
	print(max_flow(capacities_6))
	print(max_flow(capacities_7))
	print(max_flow(capacities_8))


