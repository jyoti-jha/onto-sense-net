import nltk
import os

filename = '../data/novel/raw/combined/total.txt'

with open(filename) as f:
    data = f.read().replace('\n', '')

from __future__ import unicode_literals
from iscnlp import Tokenizer
tk = Tokenizer(lang='hin', split_sen=True)

