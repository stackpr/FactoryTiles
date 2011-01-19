with open('validcombinations') as validfilenames:
    for line in validfilenames:

        # inflate templates

        # 0 stays 0, 1 stays 1, 2 stays 2, 3 stays 3
        if line[0] == '4': line = '24' + line[1] + line[2] + line[3]
        if line[0] == '5': line = '135' + line[1] + line[2] + line[3]

        # 0 stays 0, 1 stays 1, 2 stays 2, 3 stays 3
        if line[1] == '4': line = line[0] + '24' + line[2] + line[3]
        if line[1] == '5': line = line[0] + '135' + line[2] + line[3]

        # 0 stays 0, 1 stays 1, 2 stays 2, 3 stays 3
        if line[1] == '4': line = line[0] + line[1] + '24' + line[3]
        if line[1] == '5': line = line[0] + line[1] + '135' + line[3]

        line = 'scalable/' + line[:-1] + '.svg'
        open(line, 'w').close()
