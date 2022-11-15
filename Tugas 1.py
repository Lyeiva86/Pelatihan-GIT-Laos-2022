huruf = []
for i in range(int(input())):
    huruf.append(input())

for i in huruf:
    print('\nHasil :\n')
    for j, y in enumerate(i):
        if not j == len(i) - 1:
            a = ord(y)
            b = ord(i[j + 1])
            selisih = abs(a - b)

            if a < b:
                print(f'{y} kurang dari {i[j + 1]}, selisihnya {selisih}')
            elif a > b:
                print(f'{y} lebih dari {i[j + 1]}, selisihnya {selisih}')
            else:
                print(f'{y} sama dengan {i[j + 1]}, selisihnya {selisih}')

#

