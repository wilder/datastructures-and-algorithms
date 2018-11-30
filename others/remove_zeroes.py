def remove(s):
    i = 0
    j = 0

    while i < len(s):
        if s[i] == 0:
            i+=1
        else:
            s[j] = s[i]
            i+=1
            j+=1

    while j < len(s):
        s[j] = 0
        j+=1
    
    return s

#a = [0,1,0,0,3,4,5]
#print remove(a)
