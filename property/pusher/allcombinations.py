with open('allcombinations', 'w') as outfile:
    out = ''
    for i in range(0,6):
        for j in range(0,6):
            for k in range(0,6):
                for l in range(0,6):
                    out += str(i) + str(j) + str(k) + str(l) + '\n'

    outfile.write(out)
