import java.lang.Exception
import java.util.*
import kotlin.test.assertEquals

/*
This problem was asked by Google.

In a directed graph, each node is assigned an uppercase letter.
We define a path's value as the number of most frequently-occurring letter along that path.

For example, if a path in the graph goes through "ABACA",
the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges,
return the largest value path of the graph.
If the largest value is infinite, then return null.

The graph is represented with a string and an edge list.
The i-th character represents the uppercase letter of the i-th node.
Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node.
Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A
[(0, 0)]
Should return null, since we have an infinite loop.

 */

fun maxFrequentLetterPathCount(letters: String, graph: List<Pair<Int, Int>>): Int? {

    val adjacencyMap: Map<Int, List<Int>> = buildAdjacencyMap(graph)

    try {
        val biggestPath = getBiggestPath(adjacencyMap)
        val pathString = buildPathString(letters, biggestPath)
        return calculateLargestValuePath(pathString)
    } catch (e: Exception) {
        print("loop")
        return null
    }

}

fun buildAdjacencyMap(graph: List<Pair<Int, Int>>): Map<Int, List<Int>> {
    val adjacencyMap = mutableMapOf<Int, MutableList<Int>>()
    graph.forEach {
        adjacencyMap.getOrPut(it.first) {arrayListOf()}
            .add(it.second)
    }
    return adjacencyMap.toMap()
}

fun updateMax(currentPath: String, biggestPath: String): String {
    if (currentPath > biggestPath) {
        return currentPath
    }
    return biggestPath
}

fun getBiggestPath(adjacencyMap: Map<Int, List<Int>>): String {
    var biggestPath = ""
    val visitedNodes = hashSetOf<Int>()

    adjacencyMap.forEach { k, _ ->
        if (k !in visitedNodes) {
            val dfsStack = LinkedList<Int>(mutableListOf(k))
            val startPath = "$k"
            var currentPath = ""
            while (dfsStack.isNotEmpty()) {
                val current = dfsStack.pop()
                currentPath += current.toString()
                visitedNodes.add(current)

                val children = adjacencyMap[current]

                if (children != null && children.contains(k)) {
                    // TODO: refactor
                    throw Exception("Loop exception")
                }

                if (children == null) {
                    biggestPath = updateMax(currentPath, biggestPath)
                    currentPath = startPath
                } else {
                    dfsStack.addAll(children)
                }
            }
        }
    }

    return biggestPath
}

fun buildPathString(letters: String, biggestPath: String): String {
    var pathString = ""
    biggestPath.forEach {
        pathString += letters[Integer.parseInt(it.toString())]
    }
    return pathString
}

fun calculateLargestValuePath(pathString: String): Int {
    return pathString.groupingBy { it }.eachCount().map { it.value }.max()!!
}

fun main(args: Array<String>) {
    assertEquals(
        3,
        maxFrequentLetterPathCount(
            "ABACA",
            listOf(
                Pair(0, 1),
                Pair(0, 2),
                Pair(2, 3),
                Pair(3, 4)
            )
        )
    )

    assertEquals(
        null,
        maxFrequentLetterPathCount(
            "A",
            listOf(
                Pair(0, 0)
            )
        )
    )
}
