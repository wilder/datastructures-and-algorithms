
#https://www.hackerearth.com/pt-br/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/agitated-chandan/description/
from collections import defaultdict
class Node:
    def __init__(self, value):
        self.value = value
        self.distance = 0 # used to check if it has been visited
        self.edge_weight = {} #key: child, value: distance to child
        self.children = [] #children nodes - leaves

    def add_child(self, child, distance):
        self.children.append(child)
        self.edge_weight[child.value] = distance

'''
creates an edge between the two nodes 
sets the distance between them
and adds/modifies the nodes in the graph_dict
'''
def create_node(a, b, distance, graph_dict):
	node_a = graph_dict[a]
	node_b = graph_dict[b]

	#checks if they don't exist to create a new Node object
	if not node_a:
		node_a = Node(a)
	if not node_b:
		node_b = Node(b)

	#ads the node to the child list and an edge with the distance to that node
	node_a.add_child(node_b, distance)
	node_b.add_child(node_a, distance)

	#ads the nodes to the graph dict
	graph_dict[a] = node_a
	graph_dict[b] = node_b


def main ():
    #read input
    test_cases = int(raw_input())

    #used to access any node from the graph in O(1)
    graph_dict = defaultdict(lambda: None)

    for t in range(test_cases):
        number_of_nodes = int(raw_input())
        for i in range(number_of_nodes-1):
            node1, node2, distance = map(int, raw_input().split())
            create_node(node1, node2, distance, graph_dict)

        # getting the further node...
        # gets the further node from a random node
       	#parent = graph_dict[1]
        further_distance = -1
        further_node = -1
        graph_dict[1].distance = -1 #marking as visited
        adjacents = [graph_dict[1]] # just for it to enter the loop
    
        while adjacents:
            queue = []
            actual = adjacents[0]
            adjacents = adjacents[1:] #pop_first
            print 'actual: ',actual.value
            for a in actual.children:
                if a.distance == 0: #has not been visited
                    a.distance = a.edge_weight[actual.value] + actual.distance
                    print 'a.distance ', a.distance
                    if a.distance > further_distance: 
                        further_distance, further_node = a.distance, a.value
                    adjacents.append(a)
        further_distance += 1 # because it is initialized with -1
        print 'further node: ', further_node
        print 'further distance: ', further_distance
if __name__ == '__main__':
    main()


    
