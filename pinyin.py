# some code to turn ascii pinyin into fancy unicode pinyin

accented = {
    "a1":"ā", "a2":"á", "a3":"ǎ", "a4":"à", "a5":"a", 
    "e1":"ē", "e2":"é", "e3":"ě", "e4":"è", "e5":"e", 
    "i1":"ī", "i2":"í", "i3":"ǐ", "i4":"ì", "i5":"i",
    "o1":"ō", "o2":"ó", "o3":"ǒ", "o4":"ò", "o5":"o",
    "u1":"ū", "u2":"ú", "u3":"ǔ", "u4":"ù", "u5":"u",
    "v1":"ǖ", "v2":"ǘ", "v3":"ǚ", "v4":"ǜ", "v5":"ü"
}


def prettify(pinyin):
    """Prettifies multiple pronunciations separated by spaces."""
    return " ".join([prettify_one(w) for w in pinyin.split(" ")])


def prettify_one(pinyin):
    """Prettifies a single pronunciation.

    >>> prettify_one("zhong1")
    "zhōng"
    """

    tone = pinyin[-1]

    # first, fix any u with diaresis
    pinyin = pinyin.replace('u:', 'ü')
    pinyin = pinyin.replace('v', 'ü')

    # if no tone mark, just return as-is
    if not tone.isdigit():
        return pinyin

    # strip tone mark from pronunciation
    pinyin = pinyin[:-1]

    # replace the first vowel in alphabetical order
    if pinyin.find('a') != -1:
        return pinyin.replace('a', accented['a'+tone])
    if pinyin.find('e') != -1:
        return pinyin.replace('e', accented['e'+tone])
    if pinyin.find('i') != -1:
        return pinyin.replace('i', accented['i'+tone])
    if pinyin.find('o') != -1:
        return pinyin.replace('o', accented['o'+tone])
    if pinyin.find('u') != -1:
        return pinyin.replace('u', accented['u'+tone])
    if pinyin.find('ü') != -1:
        return pinyin.replace('ü', accented['v'+tone])

    # else...
    return pinyin
