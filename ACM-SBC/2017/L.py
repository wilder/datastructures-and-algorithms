letter_map = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r': 18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

def get_weight(st):
    #TODO: Improve - find a way that doesnt use a for loop
    weight = 0
    for i in st:
        weight += letter_map[i]
    return weight

def solution(st):
    
    dif_subs = set()
    rang = 0
    i = 0

    while rang < len(st):
        if i + rang >= len(st):
            rang += 1
            i = 0
        dif_subs.add(get_weight(st[i:rang+i+1]))
        i += 1

    return len(dif_subs)

print solution("abbab")
print solution("adbbabdcdbcbacdabbaccdac")

