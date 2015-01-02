import sys

from collections import defaultdict

def parse_cedict(f):
    """Given a file handle of a CEDICT, parse it into a dictionary of
    lists."""

    terms = defaultdict(list)
    for line in f.readlines():

        # skip comments
        if line.startswith("#"):
            continue

        definitions = line.partition('/')[2].strip()
        definitions = definitions.replace('/', '; ')

        # get both trad and simplified chars
        trad, simp, _ = line.split(" ", 2)

        pinyin = line.partition(']')[0].partition('[')[2]

        entry = {
            "simp": simp,
            "trad": trad,
            "pinyin": pinyin,
            "def": definitions
        }
        
        # store simplified version
        terms[simp].append(entry)

        # store trad version only if different from simplified
        if simp != trad:
            terms[trad].append(entry)

    return terms 
