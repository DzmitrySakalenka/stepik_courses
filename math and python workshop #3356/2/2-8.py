print(open(input(), 'r').read())


s = 0
for i in open(input(), 'r'):
    a += int(i)
#or print(sum(map(int,open(input()).readlines())))


print(open(input(), 'r').readlines()[-2])


import re

sheet, mean = input()
nums = list(map(int, re.findall(r'\s[1-5]\s', open(sheet, 'r').read())))
average = (sum(nums) / len(nums))

if average == int(open(mean, 'r').read()):
    print('OK')
else:
    print('ERROR')
#or
#with open(sheet) as fsheet, open(mean) as fmean:
#    rates = [int(x[-11]) for x in map(str.strip, fsheet) if x[-10:].strip() in '(автомат) (экзамен)']
#    print(['ERROR', 'OK'][int(fmean.read()) == round(sum(rates) / len(rates))])


from os.path import exists, isfile
fn = input()
if isfile(fn):
    with open(fn) as f:
        print(f'CONTENT:\n{f.read()}')
else:
    print('ERROR:','Это каталог, а не файл' if exists(fn) else 'Файл не существует', sep='\n')


with open('output.txt', 'w') as f:
    f.write(input()+'\n')
#or open('output.txt', 'w').write(input())


import os.path
file_name, event = input()
mode = "r+" if os.path.isfile(file_name) else "x+"
with open(file_name, mode) as h:
    lines = h.readlines()
    c = len(lines) - lines.count("\n") + 1
    h.seek(0)
    h.write(f"event {c} - '{event}'\n")
    h.writelines(lines)