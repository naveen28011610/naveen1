s="today i have playing the football"
d={}
for i in range (len(s)):
    if s[i] not in d:
        d[s[i]]=[i]
    else:
        d[s[i]].append(i)
print(d)