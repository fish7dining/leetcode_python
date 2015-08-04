

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    a = list(s)
    b = list(t)
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i]!=b[i]:
            return False
    return True


print isAnagram("anagram","nagram")
print isAnagram("ab","ba")
