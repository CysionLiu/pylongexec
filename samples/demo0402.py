def yanghui():
    p = [1]
    while True:
        yield p
        p.append(0)
        p = [p[i - 1] + p[i] for i in range(len(p))]


i = 0;
for x in yanghui():
    print(x)
    i = i + 1
    if i > 10:
        break
X = [3,5,6,7,12,16,20]
print(X[-1])
Y = tuple(X)
print(len(X))
for z in [y for y in Y if y%2==0]:
    print(z)