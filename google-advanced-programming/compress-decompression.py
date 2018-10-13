def decompress(compressed_str):

    num_str = ''
    num_queue = []
    decompressed = ''
    curr_str = ''

    brackets = []
    results = []

    index = 0
    while index < len(compressed_str):
        while compressed_str[index].isdigit():
            num_str += compressed_str[index]
            index += 1

        if compressed_str[index] == '[':
            num_queue.append(int(num_str))
            num_str = ''
            brackets.append(compressed_str[index])

        elif compressed_str[index] == ']':
            brackets.pop()
            decompressed += curr_str * num_queue.pop()
            curr_str = ''

            if not brackets:
                results.append(decompressed)
                decompressed = ''

        else:
            curr_str += compressed_str[index]

        index += 1

    return ''.join(results) + curr_str

if __name__ == "__main__":
    print decompress('3[abc]4[ab]c')
    assert decompress('3[abc]4[ab]c') == 'abcabcabcababababc'

    print decompress('2[3[a]b]')
    assert decompress('2[3[a]b]') == 'aaabaaab'
