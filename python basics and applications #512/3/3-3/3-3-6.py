import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'human', r'computer', line))