out = ''

with open('allcombinations') as infile:
    for line in infile:

        # Validity of combinations for walls with a common corner
        #          12345
        #          =====
        #          1   1
        #           2 2
        #            3 3
        #             4
        #              5
        #
        # 1|1      -+++-
        # 2| 2     +-+-+
        # 3|  3    ++-+-
        # 4| 2 4   +-+-+
        # 5|1 3 5  -+-+-

        # north + east
        if line[0] == '1' and line[1] == '1': continue
        if line[0] == '1' and line[1] == '4': continue
        if line[0] == '1' and line[1] == '5': continue
        if line[0] == '2' and line[1] == '2': continue
        if line[0] == '3' and line[1] == '3': continue
        if line[0] == '3' and line[1] == '5': continue
        if line[0] == '4' and line[1] == '2': continue
        if line[0] == '4' and line[1] == '4': continue
        if line[0] == '5' and line[1] == '1': continue
        if line[0] == '5' and line[1] == '3': continue
        if line[0] == '5' and line[1] == '5': continue

        # east + south
        if line[1] == '1' and line[2] == '1': continue
        if line[1] == '1' and line[2] == '4': continue
        if line[1] == '1' and line[2] == '5': continue
        if line[1] == '2' and line[2] == '2': continue
        if line[1] == '3' and line[2] == '3': continue
        if line[1] == '3' and line[2] == '5': continue
        if line[1] == '4' and line[2] == '2': continue
        if line[1] == '4' and line[2] == '4': continue
        if line[1] == '5' and line[2] == '1': continue
        if line[1] == '5' and line[2] == '3': continue
        if line[1] == '5' and line[2] == '5': continue

        # south + west
        if line[2] == '1' and line[3] == '1': continue
        if line[2] == '1' and line[3] == '4': continue
        if line[2] == '1' and line[3] == '5': continue
        if line[2] == '2' and line[3] == '2': continue
        if line[2] == '3' and line[3] == '3': continue
        if line[2] == '3' and line[3] == '5': continue
        if line[2] == '4' and line[3] == '2': continue
        if line[2] == '4' and line[3] == '4': continue
        if line[2] == '5' and line[3] == '1': continue
        if line[2] == '5' and line[3] == '3': continue
        if line[2] == '5' and line[3] == '5': continue

        # west + north
        if line[3] == '1' and line[0] == '1': continue
        if line[3] == '1' and line[0] == '4': continue
        if line[3] == '1' and line[0] == '5': continue
        if line[3] == '2' and line[0] == '2': continue
        if line[3] == '3' and line[0] == '3': continue
        if line[3] == '3' and line[0] == '5': continue
        if line[3] == '4' and line[0] == '2': continue
        if line[3] == '4' and line[0] == '4': continue
        if line[3] == '5' and line[0] == '1': continue
        if line[3] == '5' and line[0] == '3': continue
        if line[3] == '5' and line[0] == '5': continue

        # Pusher may not oppose each other, because each requires a wall to be
        # mounted on and that would block the opposing pusher
        if line[0] != '0' and line[2] != '0' or \
           line[1] != '0' and line[3] != '0':
            continue

        # at least one side needs to be open
        if not line[0] == '0' and not line[1] == '0' and \
           not line[2] == '0' and not line[3] == '0':
            continue

        # the empty combination does not require a graphic
        if line[0] == '0' and line[1] == '0' and \
           line[2] == '0' and line[3] == '0':
            continue

        out += line

with open('validcombinations', 'w') as outfile:
    outfile.write(out)
