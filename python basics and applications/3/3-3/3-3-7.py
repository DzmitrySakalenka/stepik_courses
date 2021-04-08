import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'\ba+\b', r'argh', line, count=1, flags=re.IGNORECASE))