# argv = argument variable

import sys

# print(sys.argv)
# print(type(sys.argv))

word_lengths = 0

for arg in sys.argv[1:]:
    word_lengths += len(arg)

print(f"the length is {word_lengths}")

# in order to run this code, it need to be done on a terminal.
# python3 .,.,.,.,.py
