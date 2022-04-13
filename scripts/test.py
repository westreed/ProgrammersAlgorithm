from urllib import parse

def isPercentEncoding(s):
    s = ord(s)
    if 97 <= s <= 122:  return False
    if 65 <= s <= 90:   return False
    if 48 <= s <= 57:   return False
    if s == 45 or s == 95 or s == 46 or s == 126: return False
    return True


string  = '파이썬 좋아.py'
teststr = parse.quote(string)
print(teststr)
string_ = ''
for s in string:
    if isPercentEncoding(s):
        if s == ' ':
            string_ += '%20'
        else:
            a = str(s.encode("UTF-8")).upper().replace('B\'','').replace('\'','').replace('\X', '%')
            string_ += a
    else:
        string_ += s
print(string_)


#%EC%98%88%EC%82%B0
print(ord('a'), ord('z'), ord('A'),ord('Z'),ord('0'),ord('9'))
print(ord('-'), ord('_'), ord('.'), ord('~'))

# a 97 z 122 A 65 Z 90
# 0 48 9 57
# - 45
# _ 95
# . 46
# ~ 126