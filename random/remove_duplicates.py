def remove(s):
    i = 0
    j = 0

    while i < len(s)-1:
        if s[i] == s[i+1]:
            i+=1
        else:
            s[j] = s[i]
            i+=1
            j+=1
    while j < len(s):
        s[j] = None
        j+=1
    return s

#a = [0,1,0,0,3,3,3,3,3,3,3,4,3,4,4,4,2,1,3,4,5,5]
#print remove(a)
