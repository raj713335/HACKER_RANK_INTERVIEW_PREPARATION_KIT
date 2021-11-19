s = input()
avail = {}
for c in s:
    avail[c] = avail.get(c, 0) + 1
need = {k: v//2 for k, v in avail.items()}
res = []
for c in s[::-1]:
    if need[c]:
        while res and res[-1] > c and need[res[-1]] != avail[res[-1]]:
            need[res[-1]] += 1
            res.pop()
        need[c] -= 1
        res.append(c)
    avail[c] -= 1
print("".join(res))
