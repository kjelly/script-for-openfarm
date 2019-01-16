#!/usr/bin/env python3
import json
import sys
import os


def extract(s, word):
    try:
        i = s.index(word)
        low = i - 10
        high = i + 10
        if low < 0:
            low = 0
        if high >= len(s):
            high = len(s) - 1
        return s[low:high]
    except ValueError:
        return None


def normalize_symptoms(lst):
    def f(x):
        if x is None:
            return 'N'
        else:
            return 'Y'
    return list(map(f, lst))


def normalize_answer(s):
    s = s.strip()
    r = ['N'] * 5
    for i in s:
        r[int(i, 10) - 1] = 'Y'
    return r


def main():
    with open(sys.argv[1], 'r') as ftr:
        data = ftr.readlines()

    data = [i.split('\t') for i in data]

    parts = ['根', '莖', '葉', '花', '果']

    if os.path.exists(sys.argv[2]):
        with open(sys.argv[2], 'r') as ftr:
            result = json.loads(ftr.read())
    else:
        result = {}

    for i in data:
        if i[0] in result:
            continue
        if len(i) <= 1:
            continue
        print(i[0])
        print(i[1])
        print('http://www.google.com/search?q=%s' % i[0])
        r = []
        for j in parts:
            r.append(extract(i[1], j))
        for index, value in enumerate(r):
            print('%d. %s -> %s' % (index + 1, parts[index], value))
        ans = input('Is it good?')
        if ans.strip() == '':
            result[i[0]] = normalize_symptoms(r)
        else:
            result[i[0]] = normalize_answer(ans)

        print('--------------')

        print(result)
        with open(sys.argv[2], 'w') as ftr:
            json.dump(result, ftr, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
