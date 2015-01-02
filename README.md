This is a pile of Python 3 code that extracts unique hanzi from a UTF-8 file
and combines them with their reading and definition from CEDICT.

hanzidefs.py
============

This program will generate a TSV file containing each hanzi along with up
to 3 readings/definitions for that hanzi. The hanzi are listed in order from
the most common to the least common in that file.

This is useful for generating cards for flashcard software such as Anki.

Instructions
------------

1. Download the CEDICT:
   `http://www.mdbg.net/chindict/export/cedict/cedict_1_0_ts_utf-8_mdbg.zip`
2. Extract the CEDICT to some file, probably `cedict_ts.u8`
3. Run `git submodule init`
4. Get a text file in UTF-8 format. You may need to use `file` to check your
   file's encoding and `iconv` to convert it.`
5. Run `python3 hanzidefs.py cedict_ts.u8 < yourtext.txt > yourdefs.tsv`
6. Open up your TSV file in a spreadsheet tool or import it into your favorite
   SRS study software.


hanzifreqs.py
=============

This program is a utility script that prints out all the hanzi from an input
file along with its number of occurrences, sorted from most frequent to least
frequent.

This is useful for analyzing a document, perhaps to estimate its difficulty.

Usage:

`python3 hanzifreqs.py < yourtext.txt > yourfreqs.tsv`
