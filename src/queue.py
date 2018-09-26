import toolz as tz
from toolz import first, second, drop, thread_first, thread_last, flip, concat, reduce
from pprint import pprint as pp, pformat
from utils import string_to_words_list, is_too_long, lorem_ipsum, answer

"""
Telegram Problem:
(from wikipedia)

Write a program which accepts lines of text and generates output
lines containing as many words as possible, where the number of characters in
each line does not exceed a certain length. The words may not be split and we
assume no word is longer than the size of the output lines. This is analogous
to the word-wrapping problem in text editors.

In conventional logic, the programmer rapidly discovers that neither the input
nor the output structures can be used to drive the call hierarchy of control
flow. In FBP, on the other hand, the problem description itself suggests a
solution:

"""


words_list = string_to_words_list(lorem_ipsum)
words_list.reverse() # for pop to work in order

line = ""
buff_lines = []

while words_list:
    word = words_list.pop()
    if not is_too_long(line, word):
        line += f" {word}"
    else:
        buff_lines.append(line)
        line = word
buff_lines.append(line)

final = "\n".join(buff_lines)

assert final.strip() == answer.strip()
