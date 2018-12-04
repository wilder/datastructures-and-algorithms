/**
 * This problem was asked by Palantir.
 *
 * Write an algorithm to justify text.
 *
 * Given a sequence of words and an integer line length k,
 * return a list of strings which represents each line, fully justified.
 *
 * More specifically, you should have as many words as possible in each line.
 * There should be at least one space between each word.
 *
 * Pad extra spaces when necessary so that each line has exactly length k.
 * Spaces should be distributed as equally as possible, with the extra spaces,
 * if any, distributed starting from the left.
 *
 * If you can only fit one word on a line, then you should pad the right-hand side with spaces.
 *
 * Each word is guaranteed not to be longer than k.
 *
 * For example, given the list of words
 * ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
 * and k = 16, you should return the following:
 *
 * ["the  quick brown", # 1 extra space on the left
 * "fox  jumps  over", # 2 extra spaces distributed evenly
 * "the   lazy   dog"] # 4 extra spaces distributed evenly
 */

fun justify(words: List<String>, maxLineLength: Int): List<String> {

    val wordsPerLine = getWordsPerLine(words, maxLineLength)
    val justifiedLines = mutableListOf<String>()

    wordsPerLine.forEach { line ->
        addPadding(line, maxLineLength, justifiedLines)
    }

    return justifiedLines
}

private fun addPadding(line: List<String>, maxLineLength: Int, justifiedLines: MutableList<String>) {
    val wordCount = line.size
    val missingSpaces = maxLineLength - wordCount
    val numberOfGaps = wordCount - 1
    val firstSpaceCount = Math.ceil(missingSpaces / numberOfGaps.toDouble()).toInt()
    val otherSpaceCount = missingSpaces / numberOfGaps

    if (numberOfGaps == 0) {
        val leftSpaceCount = Math.ceil(missingSpaces / 2.toDouble()).toInt()
        val rightSpaceCount = missingSpaces / 2

        var wordWithPadding = addSpaces(leftSpaceCount, "")
        wordWithPadding += line[0]
        wordWithPadding = addSpaces(rightSpaceCount, wordWithPadding)
        justifiedLines.add(wordWithPadding)
    } else {
        var wordWithPadding = ""
        line.forEachIndexed { index, word ->
            wordWithPadding += word
            var spaceCount = otherSpaceCount
            if (index == 1) spaceCount = firstSpaceCount
            if (index == line.size - 1) spaceCount = 0
            wordWithPadding = addSpaces(spaceCount, wordWithPadding)
        }
        justifiedLines.add(wordWithPadding)
    }
}

private fun addSpaces(spaceCount: Int, wordWithPadding: String): String {
    var wordWithPadding1 = wordWithPadding
    for (i in 0..spaceCount) {
        wordWithPadding1 += " "
    }
    return wordWithPadding1
}

private fun getWordsPerLine(words: List<String>, lineLength: Int): MutableList<List<String>> {
    val lines = mutableListOf<List<String>>()
    var currentLine = mutableListOf<String>()

    var currentLineLength = 0
    words.forEach {
        var currentWordLength = it.length
        if (currentLine.isNotEmpty()) {
            currentWordLength += 1
        }
        currentLineLength += currentWordLength

        if (currentLineLength >= lineLength) {
            lines.add(currentLine.toList())
            currentLineLength = it.length
            currentLine.clear()
        }
        currentLine.add(it)
    }

    return lines
}

fun main(args: Array<String>) {
    val sentence = listOf("the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog")
    println(justify(sentence, 17))
}
