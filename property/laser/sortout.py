out = ''

with open('allcombinations') as infile:
    for line in infile:
        if line[1] == '1' and line[3] == '1': continue
        if line[1] == '1' and line[3] == '3': continue
        if line[1] == '2' and line[3] == '2': continue
        if line[1] == '2' and line[3] == '3': continue
        if line[1] == '3' and line[3] == '1': continue
        if line[1] == '3' and line[3] == '2': continue
        if line[1] == '3' and line[3] == '3': continue

        if line[0] == '1' and line[2] == '1': continue
        if line[0] == '1' and line[2] == '3': continue
        if line[0] == '2' and line[2] == '2': continue
        if line[0] == '2' and line[2] == '3': continue
        if line[0] == '3' and line[2] == '1': continue
        if line[0] == '3' and line[2] == '2': continue
        if line[0] == '3' and line[2] == '3': continue

        if not line[0] == '0' and not line[1] == '0' and
            not line[2] == '0' and not line[3] == '0':
            continue

        if line[0] == '0' and line[1] == '0' and
            line[2] == '0' and line[3] == '0':
            continue

        out += line

with open('validcombinations', 'w') as outfile:
    outfile.write(out)

with open('validcombinations') as validfilenames:
    for filename in validfilenames:
        filename = 'scalable/' + filename[:-1] + '.svg'
        print filename
        try:
            open(filename, 'r').close()
        except:
            open(filename, 'w').close()
