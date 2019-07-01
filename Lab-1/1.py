tp = [('John', ('Physics', 80)), ('Daniel', ('Science', 90)), ('John', ('Science', 95)), ('Mark', ('Maths', 100)),
         ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]

d = dict()
for x, y in enumerate(tp):
    for i in range(x + 1,len(tp)):
                #checks if the same value is present in the list
                if tp[x][0] in tp[i]:
                    d[tp[x][0]] = [y[1], tp[i][1]]

print(d)