# initialization of graph hash table
graph = {}
# initialization of the first node and it's directions to another with values
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

# initialization of the second node and it's direction to finish node with value
graph['a'] = {}
graph['a']['fin'] = 1

# initialization of the second node and it's directions to A-node and finish node with values
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

# intialization of the last(finish) node without any directions
graph['fin'] = {}

# initialization of costs hash table
infinity = float('inf')

costs = {}
costs['a'] = 6 # Time to reach node A from the beggining in one step
costs['b'] = 2 # Time to reach node B from the beggining in one step
costs['fin'] = infinity # Why infinity? 'Cause you cannot reach finish node in one step

# initialization of parents hash table
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = [] # to collect processed nodes

def find_lowest_cost_node(costs):
	lowest_cost = float('inf')
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node

def algorithms(costs = costs):
	node = find_lowest_cost_node(costs)
	while node is not None:
		print(node)
		cost = costs[node]
		neighbors = graph[node]
		for n in neighbors.keys():
			new_cost = cost + neighbors[n]
			if costs[n] > new_cost:
				costs[n] = new_cost
				parents[n] = node
		processed.append(node)
		node = find_lowest_cost_node(costs)

algorithms()