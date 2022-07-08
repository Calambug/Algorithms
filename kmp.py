# Алгоритм Кнута-Морриса-Пратта, сложность: O(n+m)
t = "лилила"
p = [0]*len(t)
j = 0
i = 1
while i < len(t):
    if t[j] == t[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]
# print(p)

a = "лилилось лилилась"
i = 0
j = 0
while i < len(a):
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == len(t):
            print("Образ найден")
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1
if i == len(a):
    print("Образ не найден")


