'''
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.

The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''

def encode(string):
    if not string:
        return string
    lastSeenChar = string[0]
    charCount = 0
    encodedString = ''
    for char in string:
        if char != lastSeenChar:
            encodedString += str(charCount) + lastSeenChar
            charCount = 0
        lastSeenChar = char
        charCount += 1
    return encodedString + str(charCount) + lastSeenChar

if __name__ == "__main__":
    assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"
    assert encode("ABBBCCCLLJJJJJJJJJI") == "1A3B3C2L9J1I" 
    assert encode("A") == "1A"
    assert encode("") == ""
