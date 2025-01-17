#! /usr/bin/env python3
#-*- coding:utf-8 -*-

from paths import raw_dir, sxhy_path, check_uptodate
from singleton import Singleton
import jieba
import os


_rawsxhy_path = os.path.join(raw_dir, 'shixuehanying.txt')


def _gen_sxhy_dict():
    print("Parsing shixuehanying dictionary ...")
    words = set()
    with open(_rawsxhy_path, 'r') as fin:
        for line in fin.readlines():
            if line[0] == '<':
                continue
            for phrase in line.strip().split()[1:]:
                if not is_cn_sentence(phrase):
                    continue
                idx = 0
                while idx + 4 <= len(phrase):
                    # Cut 2 chars each time.
                    words.add(phrase[idx : idx + 2])
                    idx += 2
                # Use jieba to cut the last 3 chars.
                if idx < len(phrase):
                    for word in jieba.lcut(phrase[idx:]):
                        words.add(word)
    with open(sxhy_path, 'w') as fout:
        fout.write(' '.join(words))


class Segmenter(Singleton):

    def __init__(self):
        if not check_uptodate(sxhy_path):
            _gen_sxhy_dict()
        with open(sxhy_path, 'r') as fin:
            self.sxhy_dict = set(fin.read().split())

    def segment(self, sentence):
        toks = []
        idx = 0
        while idx + 4 <= len(sentence):
            # Cut 2 chars each time.
            if sentence[idx : idx + 2] in self.sxhy_dict:
                toks.append(sentence[idx : idx + 2])
            else:
                for tok in jieba.lcut(sentence[idx : idx + 2]):
                    toks.append(tok)
            idx += 2
        # Cut last 3 chars.
        if idx < len(sentence):
            if sentence[idx : ] in self.sxhy_dict:
                toks.append(sentence[idx : ])
            else:
                for tok in jieba.lcut(sentence[idx : ]):
                    toks.append(tok)
        return toks


def is_cn_char(ch):
    """ Test if a char is a Chinese character. """
    return ch >= u'\u4e00' and ch <= u'\u9fa5'

def is_cn_sentence(sentence):
    """ Test if a sentence is made of Chinese characters. """
    for ch in sentence:
        if not is_cn_char(ch):
            return False
    return True

def split_sentences(text):
    """ Split a piece of text into a list of sentences. """
    sentences = []
    i = 0
    for j in range(len(text) + 1):
        if j == len(text) or \
                text[j] in [u'，', u'。', u'！', u'？', u'、', u'\n']:
            if i < j:
                sentence = u''.join(filter(is_cn_char, text[i:j]))
                sentences.append(sentence)
            i = j + 1
    return sentences

NUM_OF_SENTENCES = 4
CHAR_VEC_DIM = 512
