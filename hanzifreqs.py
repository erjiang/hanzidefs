import sys

from hanzidefs import get_all_hanzi

if __name__ == "__main__":

    chars = get_all_hanzi(sys.stdin.read())

    for ch, ct in chars:
        print("%s\t%s" % (ch, ct))
