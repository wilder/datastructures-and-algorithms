/**
 * This problem was asked by Twitter.
 * You run an e-commerce website and want to record the last N order ids in a log.
 * Implement a data structure to accomplish this, with the following API:
 * record(order_id): adds the order_id to the log
 * get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
 * You should be as efficient with time and space as possible.
 */

class OrdersLog(val size: Int) {
    var nextIndex = 0
    val bucket: MutableList<Int?> = MutableList(size, {null})

    fun record(orderId: Int) {
        if (nextIndex == size) {
            nextIndex = 0
        }
        bucket[nextIndex] = orderId
        nextIndex++
    }

    fun getLast(index: Int): Int {
        if (index >= size || index < 0) return -1
        var last = nextIndex + index

        if (last >= size) last -= size

        return bucket[last]!!
    }
}

fun main(args: Array<String>) {
    val ordersLog = OrdersLog(4)
    ordersLog.record(1)
    ordersLog.record(2)
    ordersLog.record(3)
    ordersLog.record(4)
    ordersLog.record(5)
    assert(ordersLog.getLast(0) == 2)
    assert(ordersLog.getLast(1) == 3)
    assert(ordersLog.getLast(2) == 4)
    assert(ordersLog.getLast(3) == 5)
}