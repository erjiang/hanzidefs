import collections
import sys

import cedict

usage = "python3 segmenter.py cedict_ts.u8 < inputtext.txt"

commas = [",", "、", "，"]


def segment(txt, dic):
    """Returns a list of sentences, each sentence is a list of words. It tries
    to keep the ending period mark with the sentence. Kind of messed up when it
    encounters punctuation, but if you just need the words then it's all
    right."""

    sentences = []
    curr_sent = []
    curr_word = ""

    def end_of_word():
        nonlocal curr_word, curr_sent
        if curr_word:
            curr_sent.append(curr_word)
            curr_word = ""

    def end_of_sent(c):
        nonlocal curr_sent
        end_of_word()
        if curr_sent:
            curr_sent.append(c)
            sentences.append(curr_sent)
            curr_sent = []
    
    for c in txt:
        if c in commas:
            end_of_word()
            curr_sent.append(c)
            continue

        if not ('\u4e00' <= c <= '\u9fff'):
            end_of_sent(c)
            continue

        candidate = curr_word + c
        
        if candidate in dic:
            curr_word = candidate
        else:
            end_of_word()
            curr_word = c

    return sentences


def count_words(sentences):
    """Given a list of lists, counts the individual items. It filters out all
    items that do not start with a hanzi."""
    from itertools import chain
    count = collections.Counter([w for w in chain.from_iterable(sentences) if '\u4e00' <= w[0] <= '\u9fff'])
    return count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write(usage)
        sys.exit(1)

    sys.stderr.write("Parsing CEDICT...\n")
    sys.stderr.flush()
    with open(sys.argv[1], 'r') as f:
        cedict = cedict.parse_cedict(f)

    sys.stderr.write("Processing text...\n")
    sys.stderr.flush()
    sentences = segment(sys.stdin.read(), cedict)
    counts = count_words(sentences)
    for w, c in counts.most_common():
        print("%s\t%s" % (w, c))
