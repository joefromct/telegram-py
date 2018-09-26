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

class Recompose():
  """OOP example. We could also optionally retain buff_lines as a singleton in
  the class instance."""
  def __init__(self, current_line=""):
    self.current_line = current_line
  def maybe_add_word(self, word):
    if is_too_long(self.current_line, word):
      tmp = self.current_line
      self.current_line = word
      return tmp
    else:
      self.current_line += f" {word}"


buff_lines = []
r = Recompose()
for word in string_to_words_list(lorem_ipsum):
  tmp = r.maybe_add_word(word)
  if tmp:
    buff_lines.append(tmp)

# last line...
final = "\n".join(tz.concatv(buff_lines, [r.current_line,]))

# put it together
assert final.strip() == answer.strip()
