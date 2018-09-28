def calculate_next(sequence):
    generated_sequence = ''
    current_str = ''
    for char in sequence:
        if len(current_str) == 0 or char == current_str[0]:
            current_str += char
        else:
            generated_sequence += str(len(current_str)) + current_str[0]
            current_str = char

    if current_str:
        generated_sequence += str(len(current_str)) + current_str[0]

    return generated_sequence


def looq_and_say(count):
    current_iteration = 0
    current_sequence = '1'
    sequence = [current_sequence]

    while current_iteration < count:
        current_sequence = calculate_next(current_sequence)
        sequence.append(current_sequence)
        current_iteration += 1

    return sequence

if __name__ == '__main__':
    assert calculate_next('112221') == '213211'
    assert calculate_next('1111251') == '41121511'
    print(looq_and_say(10))
