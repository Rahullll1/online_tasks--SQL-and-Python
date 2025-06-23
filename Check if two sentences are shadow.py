def shadowword(s, s1):
    f1 = s.split(' ')
    f2 = s1.split(' ')
    if len(f1) != len(f2):
        return False
    for w1, w2 in zip(f1, f2):
        if (set(w1) & set(w2)) or len(w1) != len(w2):
            return False
    return True

print(shadowword("his friends", "our company"))