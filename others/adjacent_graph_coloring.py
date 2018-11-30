def can_color(node, color, graph, colored):
    
    adjacents = graph[node]
    
    for i, v in enumerate(adjacents):
        if i != node and v == 1:
            if colored[i] == color:
                return False
    return True

def color_node(node, color, colored):
    colored[node] = color

def uncolor(node, colored):
    colored[node] = 0

def backtrack(node, graph, colored, colors):
    
    if not 0 in colored:
        return True

    if node >= len(graph):
        print 'parou aqui: node>=len'
        return False

    for color in colors:
        if not can_color(node, color, graph, colored):
            continue

        color_node(node, color, colored)
        return backtrack(node+1, graph, colored, colors)
        uncolor(node, colored) 
    return False


def main():
    graph = [[1,1,0,1,0],
            [1,1,1,0,0],
            [0,1,1,1,0],
            [1,0,1,1,1],
            [0,0,0,1,1]] 
        
    colors = [-1, -2, -3]
    colored = [0] * 5
    print backtrack(0, graph, colored, colors)
    print colored


if __name__ == "__main__":
    main()
