def hack_the_aliens(shield_max_value, program):
    bean = 1
    shield = shield_max_value
    hack_count = 0
    tried_hacking = 0

    i = 0
    while i < len(program):
        
        if program[i] == 'S':
            shield -= bean
        else:
            bean *= 2
        
        if shield < 0:
            for j in range(0, len(program) - 1):
                if program[j] == 'C' and program[j+1] == 'S':
                    program[j], program[j+1] = program[j+1], program[j]
                    hack_count += 1
                    bean = 1
                    shield = shield_max_value
                    i = 0
                    tried_hacking += 1
                    break
            
        if tried_hacking == len(program):
            return 'IMPOSSIBLE'
        
        i += 1
    return str(hack_count)

def main():
    t = int(raw_input()) # read a line with a single integer
    for i in xrange(1, t + 1):
        shield, program = raw_input().split(' ')
        result = hack_the_aliens(int(shield), program)
        print "Case #{}: {}".format(i, result)

def test():
    assert hack_the_aliens(1, "CS") == '1'
    assert hack_the_aliens(2, "CS") == '0'
    assert hack_the_aliens(1, "SS") == 'IMPOSSIBLE'
    assert hack_the_aliens(6, "SCCSSC") == "2"
    assert hack_the_aliens(2, "CC") == "0"
    assert hack_the_aliens(3, "CSCSS") == "5"

if __name__ == '__main__':
    #main()
    test()
