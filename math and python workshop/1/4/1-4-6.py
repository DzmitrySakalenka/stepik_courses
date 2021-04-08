def read_first_n_lines(filename, n=1, **kwargs):
    with open(filename, **kwargs) as f:
        return [next(f).strip() for x in range(n)]


def read_nth_line(filename, n=0, **kwargs):
    with open(filename, **kwargs) as f:
        for i,line in enumerate(f):
            if i == n:
                return line
    return None


f1, f2, n = read_first_n_lines(r'file.txt', 3)
n = int(n)

with open(f2, 'a') as fout:
    fout.write(read_nth_line(f1, n).lower())