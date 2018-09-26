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


def recursive(word_list, current_line="", buff_lines=[]):
  if word_list:
    word, *rest_list = word_list
    if is_too_long(current_line, word):
      buff_lines.append(current_line)
      current_line = word
      recursive(rest_list, current_line, buff_lines)
    else:
      current_line += f" {word}"
      recursive(rest_list, current_line, buff_lines)
  else:
    buff_lines.append(current_line)
  return buff_lines


buff_lines = thread_last(lorem_ipsum,
                         string_to_words_list,
                         recursive)

final = "\n".join(buff_lines)

assert final.strip() == answer.strip()
#buff = ''
#r = Recompose()
#for word in word_list:
#  tmp = r.maybe_add_word(word)
#  if tmp:
#    buff += f"{tmp}\n"
#buff += f"{r.current_line}\n"
#
#print(buff)
