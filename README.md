This is a pile of Python 3 code that extracts unique hanzi from a UTF-8 file
and combines them with their reading and definition from CEDICT.


hanzifreqs.py
=============

This program is a utility script that prints out all the hanzi from an input
file along with its number of occurrences, sorted from most frequent to least
frequent.

This is useful for analyzing a document, perhaps to estimate its difficulty.

Usage:

`python3 hanzifreqs.py < yourtext.txt > yourfreqs.tsv`


segmenter.py
============

This program takes a Chinese text and attempts to segment the text into
sentences, and the sentences into words. It doesn't deal too well with
punctuation and mixed Latin characters and hanzi, but if you just need to
extract Chinese terms from a text it works fine.

It will print each term along with its number of occurrences, sorted from most
frequent to least frequent.

Usage:

`python3 segmenter.py < yourtext.txt > wordfreqs.tsv`


hanzidefs.py
============

Given a list of terms, this program will generate a TSV file containing each
term along with up to 3 readings/definitions for that term.

This is useful for generating cards for flashcard software such as Anki.

Instructions
------------

1. Download the CEDICT:
   `http://www.mdbg.net/chindict/export/cedict/cedict_1_0_ts_utf-8_mdbg.zip`
2. Extract the CEDICT to some file, probably `cedict_ts.u8`
3. Run `git submodule init`
4. Get a text file in UTF-8 format. You may need to use `file` to check your
   file's encoding and `iconv` to convert it.`
5. Run `python3 segmenter.py cedict_ts.u8 < yourtext.txt > wordlist.tsv` or
   `python3 hanzifreqs.py < yourtext.txt > wordlist.tsv` to generate a word
   list.
6. Run `python3 hanzidefs.py cedict_ts.u8 < wordlist.tsv > yourdefs.tsv`
7. Open up your TSV file in a spreadsheet tool or import it into your favorite
   SRS study software.


License
=======

This software is distributed under the terms of the Affero GPL v3 license,
whose text can be found in the file `COPYING`.
