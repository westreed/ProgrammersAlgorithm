
def find(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    table = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
    
    max_comp = 0
    last_idx = 0

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if str1[i-1] == str2[j-1]: table[i][j] = table[i-1][j-1]+1
            if max_comp < table[i][j]:
                max_comp = table[i][j]
                last_idx = i
    
    ans = ""
    while max_comp:
        max_comp -= 1
        last_idx -= 1
        ans = str1[last_idx] + ans
    
    print(ans)

if __name__ == "__main__":
    str1 = "BCBBBC"
    str2 = "CBBBCC"

    find(str1, str2)