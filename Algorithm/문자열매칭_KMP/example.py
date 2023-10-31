

def KMPTable(pattern):
    pattern_length = len(pattern)
    table = [0] * pattern_length

    j = 0
    for i in range(1, pattern_length):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    
    return table

def KMP(target, pattern):
    table = KMPTable(pattern)
    target_length = len(target)
    pattern_length = len(pattern)

    j = 0
    for i in range(target_length):
        while j > 0 and target[i] != pattern[j]:
            j = table[j-1]
        
        if target[i] == pattern[j]:
            if j == pattern_length-1:
                print(f"index:{i-pattern_length+2}")
                j = table[j]
            else:
                j += 1

print(KMPTable("abacaaba"))