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

def closure_recompose():
  line = ""
  def recompose(word):
    nonlocal line
    if is_too_long(line, word):
      tmp = line
      line = word
      return tmp
    else:
      line += f" {word}"
  return recompose


r = closure_recompose()

buff_lines = thread_last(lorem_ipsum                       , # my input
                         string_to_words_list              , # split to words
                         (map, r)                          , # map words to recompose (with state)
                         (filter, lambda x: x is not None) , # because each call returns something
                         list)

# enclosure has one remaining varibale
last_line = r.__closure__[0].cell_contents

# put it together
final = "\n".join(tz.concatv(buff_lines, [last_line,]))

# should match our answer?
assert final.strip() == answer.strip()
