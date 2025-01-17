#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from char_dict import CharDict
from paths import raw_dir
from singleton import Singleton
import os

_pinyin_path = os.path.join(raw_dir, 'pinyin.txt')


def _get_vowel(pinyin):
    i = 0
    while i < len(pinyin) and \
            pinyin[i] not in ['A', 'O', 'E', 'I', 'U', 'V']:
        i += 1
    return pinyin[i : ]

def _get_rhyme(pinyin):
    vowel = _get_vowel(pinyin)
    if vowel in ['A', 'IA', 'UA']:
        return 1
    elif vowel in ['O', 'UO']:
        return 2
    elif vowel == 'E':
        return 3
    elif vowel in ['IE', 'UE']:
        return 4
    elif vowel == 'I' and pinyin[0] in ['Z', 'C', 'S']:
        return 5
    elif vowel == 'ER':
        return 6
    elif vowel == 'I' and pinyin[0] in ['B', 'P', 'M', 'F', 'D', 'T', 'N', 'L', 'J', 'Q', 'X', 'Y']:
        return 7
    elif vowel in ['EI', 'UI']:
        return 8   
    elif vowel in ['AI', 'UAI']:
        return 9
    elif vowel == 'U':
        return 10
    elif vowel == 'V':
        return 11
    elif vowel in ['OU', 'IU']:
        return 12
    elif vowel in ['AO', 'IAO']:
        return 13
    elif vowel in ['AN', 'IAN', 'UAN']:
        return 14
    elif vowel in ['EN', 'IN', 'UN', 'VN']:
        return 15
    elif vowel in ['ANG', 'IANG', 'UANG']:
        return 16
    elif vowel in ['ENG', 'ING']:
        return 17
    elif vowel in ['ONG', 'IONG']:
        return 18
    return 0


class PronDict(Singleton):

    def __init__(self):
        self.char_dict = CharDict()
        self._pron_dict = dict()
        with open(_pinyin_path, 'r') as fin:
            for line in fin.readlines():
                toks = line.strip().split()
                ch = chr(int(toks[0], 16))
                if ch not in self.char_dict:
                    continue
                self._pron_dict[ch] = []
                for tok in toks[1 : ]:
                    self._pron_dict[ch].append((tok[:-1], int(tok[-1])))

    def co_rhyme(self, a, b):
        """ Return True if two pinyins may have the same rhyme. """
        if a in self._pron_dict and b in self._pron_dict:
            a_rhymes = map(lambda x : _get_rhyme(x[0]), self._pron_dict[a])
            b_rhymes = map(lambda x : _get_rhyme(x[0]), self._pron_dict[b])
            for a_rhyme in a_rhymes:
                if a_rhyme in b_rhymes:
                    return True
        return False

    def counter_tone(self, a, b):
        """ Return True if two pinyins may have opposite tones. """
        if a in self._pron_dict and b in self._pron_dict:
            level_tone = lambda x : x == 1 or x == 2
            a_tones = map(lambda x : level_tone(x[1]), self._pron_dict[a])
            b_tones = map(lambda x : level_tone(x[1]), self._pron_dict[b])
            for a_tone in a_tones:
                if (not a_tone) in b_tones:
                    return True
        return False

    def __iter__(self):
        return iter(self._pron_dict)

    def __getitem__(self, ch):
        return self._pron_dict[ch]


