def step(k, lab, null_lab):
    for i in range(len(null_lab)):
        for j in range(len(null_lab[i])):
            if null_lab[i][j] == k:
                if i > 0 and null_lab[i - 1][j] == 0 and lab[i - 1][j] == 0:
                    null_lab[i - 1][j] = k + 1
                if j > 0 and null_lab[i][j - 1] == 0 and lab[i][j - 1] == 0:
                    null_lab[i][j - 1] = k + 1
                if i < len(null_lab) - 1 and null_lab[i + 1][j] == 0 and lab[i + 1][j] == 0:
                    null_lab[i + 1][j] = k + 1
                if j < len(null_lab[i]) - 1 and null_lab[i][j + 1] == 0 and lab[i][j + 1] == 0:
                    null_lab[i][j + 1] = k + 1
    return k, lab, null_lab


lab = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

start = [1, 1]
end = [2, 5]
null_lab = []
for i in range(len(lab)):
    null_lab.append([])
    for j in range(len(lab[i])):
        null_lab[-1].append(0)
i, j = start
null_lab[i][j] = 1

k = 0
while null_lab[end[0]][end[1]] == 0:
    k += 1
    step(k, lab, null_lab)

i, j = end
k = null_lab[i][j]
path = [(i, j)]
while k > 1:
    if i > 0 and null_lab[i - 1][j] == k - 1:
        i, j = i - 1, j
        path.append((i, j))
        k -= 1
    elif j > 0 and null_lab[i][j - 1] == k - 1:
        i, j = i, j - 1
        path.append((i, j))
        k -= 1
    elif i < len(null_lab) - 1 and null_lab[i + 1][j] == k - 1:
        i, j = i + 1, j
        path.append((i, j))
        k -= 1
    elif j < len(null_lab[i]) - 1 and null_lab[i][j + 1] == k - 1:
        i, j = i, j + 1
        path.append((i, j))
        k -= 1

for i in range(len(path)):
    q, w = path[i]
    lab[q][w] = 2
for i in range(len(lab)):
    print(lab[i])