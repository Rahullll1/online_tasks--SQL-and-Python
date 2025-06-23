def rmv_extra(s, s1):
    for i in s1:
        if i not in s:
            return i
s = "eueiieo"
s1 = "iieoedue"
print(rmv_extra(s, s1))