/**
 *
 * 1002. Find Common Characters
 * https://leetcode.com/problems/find-common-characters/
 *
 */
class Solution {
    fun commonChars(wordList: Array<String>): List<String> {
      val commonChars = mutableListOf<String>()
      val wordsCharOcurrence: MutableList<IntArray> = mutableListOf()

      wordList.forEach { word ->
          wordsCharOcurrence.add(IntArray(26))
          val currentCharOccurrences = wordsCharOcurrence[wordsCharOcurrence.size - 1]
          word.forEach { letter ->
              currentCharOccurrences[letter - 'a'] += 1
          }
      }

      for (index in 0 until 26) {
          var minOccurrences = Integer.MAX_VALUE
          wordsCharOcurrence.forEach {charOcurrences ->
              val currentLetterCount = charOcurrences[index]
              minOccurrences = Math.min(currentLetterCount, minOccurrences)
          }

          if (minOccurrences > 0) {
              commonChars.addAll(CharArray(minOccurrences)
                  { _ -> (index.toChar() + 'a'.toInt())}
                  .map { it.toString() })
          }
      }

      return commonChars
  }
}
