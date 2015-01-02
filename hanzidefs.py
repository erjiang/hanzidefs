import collections
import sys

import cedict
import pinyin


"""
This program takes a word list and prints out each word along with three
definitions from the given dictionary.

The wordlist should have each term on a separate line. If a TSV file is given,
then the first field is assumed to be the term to look up.
"""


usage = "Usage: python hanzidefs.py cedict_ts.u8 < wordlist.tsv > outputdefs.tsv\n"
usage += "Usage: python hanzifreqs.py < inputtext.txt | python hanzidefs.py cedict_ts.u8\n"


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

    sys.stderr.write("Generating defs...\n")
    sys.stderr.flush()
    for l in sys.stdin.readlines():
        ch = l.partition("\t")[0]
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
