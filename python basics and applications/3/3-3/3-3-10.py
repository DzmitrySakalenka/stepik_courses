import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'^(1(01*0)*1|0)*$', line):
        print(line)

#alternative
pattern = "^(0|(1(01*0)*1))*$"
pattern = re.compile(pattern)
for line in sys.stdin:
    line = line.rstrip()
    if pattern.match(line):
        print(line)