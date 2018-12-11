'''
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''


'''
O(1) Space Complexity
O(n) Time Complexity
'''
def rgbSort(rgbString):

    nextRIndex = 0
    nextBIndex = len(rgbString) - 1
    index = 0
    while(index < len(rgbString) and index <= nextBIndex):
        element = rgbString[index]
        if element == 'R':
            rgbString[nextRIndex], rgbString[index] = rgbString[index], rgbString[nextRIndex]
            nextRIndex += 1

        elif element == 'B':
            rgbString[nextBIndex], rgbString[index] = rgbString[index], rgbString[nextBIndex]
            nextBIndex -= 1
        
        if rgbString[index] == 'G':
            index += 1

    return rgbString


if __name__ == '__main__':
    print(rgbSort(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
    assert rgbSort(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
