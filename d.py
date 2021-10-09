a = [int(i) for i in input().split()]
c = sorted(a)[2]
a.remove(c)
flag = False

for i in range(4):
    for j in range(4):
        for k in range(4):
            for d in range(4):
                if i != j and j != k and k != d and k != i and d != j and d != i:
                    if c < a[j] + a[i] and a[i] < a[j] + c and a[j] < a[i] + c and c < a[k] + a[d] \
                            and a[d] < a[k] + c and a[k] < a[d] + c:
                        n_1, n_2, n_3, n_4, = a[i], a[j], a[k], a[d]
                        flag = True

if flag:
    print(c)
    print(n_1, n_2)
    print(n_3, n_4)
else:
    print(0)
