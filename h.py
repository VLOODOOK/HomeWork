n = int(input())
r = [int(i) for i in input().split()]
galaxad = [int(i) for i in input().split()]

if galaxad[0] == n:
    pass
else:
    r = r[:galaxad[0]] + [galaxad[1]] + r[galaxad[0]:]

print(r)

n = 0
c = 0
c_1 = 0

while n < 10:
    rang = r[-1]
    index = -1

    for i in range(len(r)):

        if rang == r[i]:
            c += 1
            c_1 += 1
            if index == -1:
                c -= 1
                r.pop(-1)
                index = 0
            print(r)
            index = i
            break

        if c > 0:
            r[index] = rang + c_1
            for i in range(c - 1):
                r.remove(rang)

        index = i

        n += 1

print(r)


# 3
# 1 2 1
# 1 1



