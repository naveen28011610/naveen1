#convert to list in dict with the help of zip class

'''l1 = [1, 2, 3]
l2 = [4, 5, 6]
d = {}
for item1, item2 in zip(l1, l2):
    d[item1] = (item2)
print(d)'''

'''l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(dict(zip(l1, l2)))'''



'''temperature={"bangalore":(26,32),"chennai":(26,32),"delhi":(31,36)}
print(list(temperature.items()))
print(str(temperature.items()))'''


'''temperature={"bangalore":(26,32),"chennai":(26,32),"delhi":(31,36)}
l=[]
for i in temperature.items():
    l.append(i)
print(l)'''

'''temperature={"bangalore":(26,32),"chennai":(26,32),"delhi":(31,36)}
l=[]
for key,value in temperature.items():
    l.append((key,value))
print(l)'''









