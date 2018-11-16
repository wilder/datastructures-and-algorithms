import kotlin.test.assertEquals

/**
 * A class that represents a node of a Trie
 */
data class Node(
        val value: Char,
        var isWord: Boolean = false,
        val children: MutableMap<Char, Node> = mutableMapOf(),
        var word: String = ""
)

class Trie {
    val nodes: MutableMap<Char, Node> = mutableMapOf()

    companion object {
        fun from(words: List<String>) : Trie {
            val trie = Trie()
            words.forEach { addWord(trie, it) }
            return trie
        }

        private fun addWord(trie: Trie, word: String) {
            var currentNode = trie.nodes.computeIfAbsent(word[0], { Node(it) })
            for (i in 1 until word.length) {
                currentNode = currentNode.children.computeIfAbsent(word[i], { Node(it) })
            }
            currentNode.isWord = true
            currentNode.word = word
        }

    }
    
    fun getFromPrefix(prefix: String) : List<String> {
        var currentNode: Node? = nodes.getOrDefault(prefix[0], null)
        if (currentNode == null) return emptyList()

        for (i in 1 until prefix.length) {
            if (!currentNode!!.children.containsKey(prefix[i])) {
                return getAllWordsFrom(currentNode)
            }
            currentNode = currentNode.children.get(prefix[i])
        }
        return getAllWordsFrom(currentNode!!)
    }

    fun getAllWordsFrom(node: Node, result: MutableList<String> = mutableListOf()) : List<String> {
        if (node.isWord) result.add(node.word)
        if (node.children.isEmpty()) return result
        
        node.children.forEach { _, currentNode ->
            getAllWordsFrom(currentNode, result)
        }
        return result
    }
}

fun main(args: Array<String>) {
    val trie = Trie.from(listOf("dog", "dear", "deal"))
    assertEquals(listOf("dear", "deal"), trie.getFromPrefix("de"))

    val trie2 = Trie.from(listOf("dog", "dear", "deal"))
    assertEquals(listOf("dog"), trie2.getFromPrefix("do"))

    val trie3 = Trie.from(listOf("dog", "dear", "deal"))
    assertEquals(listOf("dog", "dear", "deal"), trie3.getFromPrefix("d"))

    val trie4 = Trie.from(listOf("dog", "dear", "deal"))
    assertEquals(listOf("dog"), trie4.getFromPrefix("dog"))

    val trie5 = Trie.from(listOf("dog", "dear", "deal"))
    assertEquals(listOf(), trie4.getFromPrefix("a"))
}
