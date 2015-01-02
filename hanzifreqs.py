import sys
import collections


def get_all_hanzi(txt):

    # count all the characters in CJK range
    counts = collections.Counter([c for c in txt if '\u4e00' <= c <= '\u9fff'])

    sys.stderr.write("%d uniq chars found\n" % len(counts))

    # return characters from most to least common
    return counts.most_common()


if __name__ == "__main__":

    chars = get_all_hanzi(sys.stdin.read())

    for ch, ct in chars:
        print("%s\t%s" % (ch, ct))
