import kotlin.test.assertFalse
import kotlin.test.assertTrue

/**
 * Write a function that returns whether two words are exactly "one edit" away
 *
 * An edit is:
 * Inserting one character anywhere in the word (including at the beginning and end)
 * Removing one character
 * Replacing one character
 *
 *
 * OneEditApart("cat", "dog") = false
 * OneEditApart("cat", "cats") = true
 * OneEditApart("cat", "cut") = true
 * OneEditApart("cat", "cast") = true
 * OneEditApart("cat", "at") = true
 * OneEditApart("cat", "act") = false
 *
 * 10:10
 */
class OneEditDistance {

    fun oneEditApart(s1: String, s2: String): Boolean {

        var distance = 0
        var index1 = 0
        var index2 = 0

        while (index1 < s1.length && index2 < s2.length) {
            if (s1[index1] != s2[index2]) {
                distance++

                if(distance > 1) {
                    return false
                }

                if (distance == 1 && s1.length != s2.length) {
                    if (s1.length > s2.length) {
                        index2--
                    } else {
                        index1--
                    }
                }
            }
            index1++
            index2++

        }

        //add remaining distance
        distance += s2.length - index2 + s1.length - index1

        return distance == 1

    }

}

fun main(args: Array<String>) {
    val a = OneEditDistance()
    assertFalse { a.oneEditApart("cat", "dog") }
    assertTrue { a.oneEditApart("cat", "cats") }
    assertTrue { a.oneEditApart("cat", "cut") }
    assertTrue { a.oneEditApart("cat", "cast") }
    assertTrue { a.oneEditApart("cat", "at") }
    assertFalse { a.oneEditApart("cat", "act") }
}
