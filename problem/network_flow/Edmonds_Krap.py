import numpy as np
from collections import deque

def max_flow(C):
	'''
	Solve the max flow problem with Edmonds-Krap algorithm.

	Args:
		G: graph dictionary {node: [neighbors]}, 0 for source, 1 for sink.
		C: capacity dictionary {(u, v): capacity}

	Returns:
		flow: max flow.
	'''
	
	# make function to find path, given C_residual. BFS.
	def search_path(C_residual, adj_list, delta):
		def exists_path():
			while queue:
				# pop out a node as v
				v = queue.popleft()
				# find all edges in C_residule that edge[0] = v and c != 0
				if v in adj_list:
					for end in adj_list[v]:
						edge = (v, end)	
						if edge in C_residual:
							if C_residual[edge] >= delta:
								# if edge[1] == sink: link to v and return
								if end == 1:
									parent[end] = v
									return True
								# else: add node to stack and link to v.
								elif end not in checked:
									queue.append(end)
									parent[end] = v
									checked.add(end)
			return False
		# make a queue
		queue = deque()
		queue.append(0)
		checked = {0}
		# make a parent dictionary to record path
		parent = {}
		if exists_path():
			# have parent, make path like [(0,2),(2,3),(3,1)].reverse()
			# find parent[1], and append (parent[1],1) to path
			path = [(parent[1], 1)]
			min_capacity = C_residual[path[0]]
			v = path[0][0]
			while v != 0:
				path.append((parent[v], v))
				v = parent[v]
				if C_residual[path[-1]] < min_capacity:
					min_capacity = C_residual[path[-1]]
			path.reverse()
			return path, min_capacity
		else:
			return None, None


	flow = 0
	C_residual = C.copy()

	# make a adjacency list
	adj_list = {}
	for (u, v) in C_residual.keys():
		if u not in adj_list:
			adj_list[u] = []
		if v not in adj_list:
			adj_list[v] = []
		adj_list[u].append(v)
		adj_list[v].append(u)

	# traverse C_residual and find delata
	max_c = -float('inf')
	for c in C_residual.values():
		if c > max_c:
			max_c = c
	delta = 2 ** int(np.log2(max_c))


	# with a path, make a residual graph
	while delta >= 1:	
		path, min_capacity = search_path(C_residual, adj_list, delta)
		while path:
			# for every edge in the path capacity minus min_capacity. 
			for edge in path:
				# for edge in path, C_residual[edge] -= min_capacity.
				C_residual[edge] -= min_capacity
				# create residual edge.
				residual_edge = (edge[1], edge[0])
				if residual_edge not in C_residual:
					C_residual[residual_edge] = 0
				C_residual[residual_edge] += min_capacity
	
			flow += min_capacity
			# find another path and repeat
			path, min_capacity = search_path(C_residual, adj_list, delta)
			
		delta /= 2
			
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
	capacities_9 = {
	(0, 3): 1,
	(0, 2): 1,
	(2, 4): 1,
	(2, 5): 1,
	(4, 1): 1,
	(3, 5): 1,
	(5, 1): 1,
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
	print(max_flow(capacities_9))


