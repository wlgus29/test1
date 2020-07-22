l = [3, 1, 1, 2, 0, 0, 2, 3, 3]

d = {}
for elem in l:
    if elem in d:
        d[elem] += 1
    else:
        d[elem] = 1
print(d)



#set 참고
#s = set()
#type(s)
#s.add("A")

