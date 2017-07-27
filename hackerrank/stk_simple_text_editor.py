# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
1. append - Append string  to the end of .
2. delete - Delete the last  characters of .
3. print - Print the  character of .
4. undo - Undo the last (not previously undone) operation of type  or , reverting  to the state it was in prior to that operation.

'''
def undo(command_stack, text):
    command, value = command_stack.pop()
    if command == '1':
        #removing the appended string
        return text[:len(value)*-1]
    else:
        return text+value

def process_command(command, arg, text, command_stack):
    if command == '1':
        command_stack.append((command, arg))
        return text+arg
    elif command == '2':
        t = text[int(arg)*-1:]
        command_stack.append((command, t))
        return text[:int(arg)*-1]
    elif command == '3':
        print text[int(arg)-1]
        return text
    else:
        return undo(command_stack, text)

def main():
    if __name__ == "__main__":
        n = int(raw_input())
        command_stack = []
        text = ''
        for _ in range(n):
            inp = raw_input()
            if inp[0] != '4':
                command, arg = inp.split()
            else:
                command = inp
                arg = None

            text = process_command(command, arg, text, command_stack)

main()
