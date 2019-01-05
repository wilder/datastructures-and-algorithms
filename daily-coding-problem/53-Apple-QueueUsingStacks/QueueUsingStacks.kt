/*
This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

Leetcode: https://leetcode.com/problems/implement-queue-using-stacks
*/

import java.util.*

class MyQueue() {

    /** Initialize your data structure here. */
    val auxQueue = LinkedList<Int>()
    val fifoQueue = LinkedList<Int>()    

    /** Push element x to the back of queue. */
    fun push(x: Int) {
        moveToAux()
        auxQueue.add(x)
        moveToFifoQueue()
    }

    /** Removes the element from in front of queue and returns that element. */
    fun pop(): Int {
        return fifoQueue.removeLast()
    }

    /** Get the front element. */
    fun peek(): Int {
        return fifoQueue.peekLast()
    }

    /** Returns whether the queue is empty. */
    fun empty(): Boolean {
        return fifoQueue.isEmpty()
    }
    
    private fun moveToAux() {
        while(!fifoQueue.isEmpty()) {
            auxQueue.add(fifoQueue.pollLast())
        }
    }
    
    private fun moveToFifoQueue() {
        while(!auxQueue.isEmpty()) {
            fifoQueue.add(auxQueue.pollLast())
        }
    }

}
