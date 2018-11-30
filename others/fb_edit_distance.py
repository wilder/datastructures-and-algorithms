def one_edit_apart(string1, string2):

    if len(string1) - len(string2) > 1:
        return False

    smaller_string, bigger_string = sorted([string1, string2] , key = len)

    a_index = 0
    b_index = 0
    editted = False
    while a_index < len(smaller_string):
        if smaller_string[a_index] != bigger_string[b_index]:
            if editted:
                return False
            editted = True
            if len(smaller_string) != len(bigger_string):
                a_index -= 1
        a_index += 1
        b_index += 1
    return True

if __name__ == '__main__':
    assert one_edit_apart("cat", "dog") == False
    assert one_edit_apart("cat", "cats") == True
    assert one_edit_apart("cat", "cut") == True
    assert one_edit_apart("cat", "cast") == True
    assert one_edit_apart("cat", "at") == True
    assert one_edit_apart("cat", "act") == False
