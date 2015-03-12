#!/usr/bin/env python


import sys


# common characters in GB
gb_cc = frozenset([
b"\xce\xd2", # 我
b"\xb5\xc4", # 的
b"\xc4\xe3", # 你
b"\xca\xc7", # 是
b"\xb2\xbb", # 不
b"\xc1\xcb", # 了
b"\xd2\xbb", # 一
b"\xc3\xc7", # 们
b"\xd5\xe2", # 这
b"\xd3\xd0" # 有
])

big5_cc = frozenset([
b"\xa7\xda", # 我
b"\xaa\xba", # 的
b"\xa7\x41", # 你
b"\xac\x4f", # 是
b"\xa4\xa3", # 不
b"\xa4\x46", # 了
b"\xa4\x40", # 一
b"\xad\xcc", # 們
b"\xb3\x6f", # 這
b"\xa6\xb3" # 有
])

utf8_cc = frozenset([
"我".encode(),
"的".encode(),
"你".encode(),
"是".encode(),
"不".encode(),
"了".encode(),
"一".encode(),
"们".encode(),
"这".encode(),
"有".encode(),
"們".encode(),
"這".encode()
])


def process_file(f):
    txt = open(f, 'rb').read()

    big5score = 0
    gbscore = 0
    utf8score = 0

    for i, b in enumerate(txt[:-3]):
        # look for high bytes
        if b > 0xa0:
            if b < 0xb4:  # could be common big5 char
                if bytes([b, txt[i+1]]) in big5_cc:
                    big5score += 1
            if 0xb2 <= b <= 0xd5:  # could be common gb char
                if bytes([b, txt[i+1]]) in gb_cc:
                    gbscore += 1

            if 0xe4 <= b <= 0xe8:
                if bytes([b, txt[i+1], txt[i+2]]) in utf8_cc:
                    utf8score += 1

    if utf8score >= gbscore:
        if utf8score >= big5score:
            return 'utf8'
        else:
            return 'big5'
    else:
        if gbscore > big5score:
            return 'gb18030'
        else:
            return 'big5'


if __name__ == "__main__":
    print(process_file(sys.argv[1]))
