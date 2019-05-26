import os

import Ofile


def main():
    f = os.walk(os.path.curdir)
    for s, d, a in f:
        o = Ofile
        r = a
        q: str
        for q in r:
            print(q)
            _a = o.OFile.is_file(s + "/" + q)
            print(str(_a))

        print(a)
        print(d)
        print(s)


pass

if __name__ == '__main__':
    main()
    pass
