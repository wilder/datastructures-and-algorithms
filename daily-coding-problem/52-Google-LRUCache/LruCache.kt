/*
This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
*/

import java.util.*

class LRUEntry(val key: Int, var value: Int)

class LRUCache(val capacity: Int) {
    
    val entries = HashMap<Int, LRUEntry>()
    val leastRecentUsed = LinkedList<LRUEntry>()
    
    fun get(key: Int): Int {
        if (!entries.contains(key)) {
            return -1
        }
        
        return evictEntry(key).value
    }
    
    private fun evictEntry(key: Int): LRUEntry {
        val entry = entries.get(key)!!
        leastRecentUsed.remove(entry)
        leastRecentUsed.add(entry)
        return entry
    }

    fun put(key: Int, value: Int) {
        if (entries.contains(key)) {
            val entry = evictEntry(key)!!
            entry.value = value
        } else if (entries.size < capacity) {
            addNewEntry(key, value)
        } else {
            replaceLeastUsedWithNewEntry(key, value)
        }
    }
    
    private fun replaceLeastUsedWithNewEntry(key: Int, value: Int) {
        val leastRecentEntry = leastRecentUsed.pollFirst()
        entries.remove(leastRecentEntry.key)
        addNewEntry(key, value)
    }
    
    private fun addNewEntry(key: Int, value: Int) {
        val entry = LRUEntry(key, value)
        entries.put(key, entry)
        leastRecentUsed.add(entry)
    }

}
