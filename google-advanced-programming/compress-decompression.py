def decompress(compressed_str):

    decompressed = ''
    num_str = ''
    num_queue = []
    curr_str = ''

    index = 0
    while index < len(compressed_str):
        while compressed_str[index].isdigit():
            num_str += compressed_str[index]
            index += 1
        
        if compressed_str[index] == '[':
            num_queue.append(int(num_str))
            num_str = ''

        elif compressed_str[index] == ']':
            decompressed += curr_str * num_queue.pop()
            curr_str = ''

        else:
            curr_str += compressed_str[index]

        index += 1

    return decompressed + curr_str

if __name__ == "__main__":
    print decompress('3[abc]4[ab]c')
    assert decompress('3[abc]4[ab]c') == 'abcabcabcababababc'

    print decompress('2[3[a]b]')
    assert decompress('2[3[a]b]') == 'aaabaaab'
