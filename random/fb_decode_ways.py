'''
 the letters of the alphabet are mapped like this:  1 -> a, 2 -> b etc
 your job is to tell the number of messages that can be decoded from
 a message in the following format:

 message = "41"
 # of decoded messages: 1
decoded_messages = ["da"]

message = "12"
decoded_messages = ["ab", "l"]
# of decoded messages: 2

'''

def num_in_map(num):
    return int(num) <= 26

def num_ways(encoded_message):

    if not encoded_message:
        return 1

    if encoded_message[0] == '0':
        return 0

    ways = num_ways(encoded_message[1:])
    if len(encoded_message) >= 2 and num_in_map(encoded_message[:2]):
        ways += num_ways(encoded_message[2:])
    return ways


if __name__ == '__main__':
    print("num_ways('123') = " + str(num_ways('123')))
    assert num_ways('123') == 3
    print("num_ways('111') = " + str(num_ways('111')))
    assert num_ways('111') == 3
    print("num_ways('1035') = " + str(num_ways('1035')))
    assert num_ways('1035') == 1
    print("num_ways('0') = " + str(num_ways('0')))
    assert num_ways('0') == 0
    print("num_ways('27') = " + str(num_ways('27')))
    assert num_ways('27') == 1
    print("num_ways('270') = " + str(num_ways('270')))
    assert num_ways('270') == 0
