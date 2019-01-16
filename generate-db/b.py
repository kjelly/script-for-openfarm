with open('a.tsv', 'r') as ftr:
    data = ftr.readlines()
with open('clean.csv', 'w') as ftr:
    for i in data[1:]:
        p = i.split('\t')
        ftr.write('%s\t%s' % (p[2], p[6]))

