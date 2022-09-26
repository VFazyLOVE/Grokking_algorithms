from collections import deque 

graph = {}
graph['you'] = ['bob', 'alice', 'clar']
graph['bob'] = ['anuj', 'peggie']
graph['alice'] = ['peggie']
graph['clar'] = ['tom','jonny']
graph['anuj'] = []
graph['peggie'] = []
graph['tom'] = []
graph['jonny'] = []

search_query = deque()
search_query += graph['you']
pop_people = []

def person_is_seller(name):
	return name[-1] == 'm'

while search_query:
	person = search_query.popleft()
	if len(search_query):
		if person not in pop_people:
			if person_is_seller(person):
				print(f'You found a right person: {person}')
				break
			else:
				pop_people.append(person)
				search_query += graph[person]
		else:
			continue
	else:
		break

