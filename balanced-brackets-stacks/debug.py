file1 = open('./output09.txt', 'r')
file2 = open('./main-results.txt', 'r')
file3 = open('./input09.txt', 'r')

lines1 = file1.readlines()
lines2 = file2.readlines()
lines3 = file3.readlines()

diff_lines = []
for (idx, (x, y)) in enumerate(zip(lines1, lines2)):
    if x != y:
        diff_lines.append(idx + 1)
        print('reference ', x)
        print('main ', y)
        print(lines3[idx + 1])
        print('-------')

    
print(diff_lines)

