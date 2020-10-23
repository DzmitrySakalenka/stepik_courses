import re
import sys


for line in sys.stdin:
    line = line.strip()
    print(re.sub(r'(\w)\1+', r'\1', line))