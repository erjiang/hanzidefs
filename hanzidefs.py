import collections
import sys

import cedict
import pinyin


usage = "Usage: python hanzidefs.py cedict_ts.u8 < inputtext.txt > outputdefs.tsv\n"


def get_all_hanzi(txt):
    
    # count all the characters in CJK range
    counts = collections.Counter([c for c in txt if '\u4e00' <= c <= '\u9fff'])

    sys.stderr.write("%d uniq chars found\n" % len(counts))

    # return characters from most to least common
    return counts.most_common()


def def2field(definition):
    """Given a parsed definition object {hanzi: _, pinyin: _, def: _}, generate
    the formatted text field to show up in the output."""
    return """{pronounce}: {meaning}""".format(
        pronounce=pinyin.prettify(definition['pinyin']),
        meaning=definition['def'])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write(usage)
        sys.exit(1)

    sys.stderr.write("Parsing CEDICT...\n")
    sys.stderr.flush()
    with open(sys.argv[1], 'r') as f:
        cedict = cedict.parse_cedict(f)

    sys.stderr.write("Reading source text...\n")
    sys.stderr.flush()
    hanzi = get_all_hanzi(sys.stdin.read())

    sys.stderr.write("Generating defs...\n")
    sys.stderr.flush()
    for ch in [c for c, _ in hanzi]:
        defs = cedict[ch]
        def1 = def2 = def3 = ""
        if not defs:
            def1 = "Unknown"
        else:
            def1 = def2field(defs[0])
            if len(defs) >= 2:
                def2 = def2field(defs[1])
                if len(defs) >= 3:
                    def3 = def2field(defs[2])

        print("""%s\t%s\t%s\t%s""" % (ch, def1, def2, def3))
