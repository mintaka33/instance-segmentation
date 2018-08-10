import sys

step = 10

def scale_map(infile, outfile):
    scale = []
    with open(infile, 'r') as fin:
        data = fin.readlines()
    fin.close()

    for line in data[::step]:
        row = ""
        for d in line[::step]:
            row = row + d
        scale.append(row)

    with open(outfile, "w") as fout:
        fout.write('\n'.join(scale))
    fout.close()

scale_map("mask_person_0.txt", "scale_0.txt")
scale_map("mask_bicycle_1.txt", "scale_1.txt")
