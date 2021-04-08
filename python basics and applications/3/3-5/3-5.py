import json

cls = {c['name']: c['parents'] for c in json.loads(input())}

isbase = lambda b, d: b == d or any(isbase(b, c) for c in cls[d])

for p in sorted(cls):
    print(p, ':', len({c for c in cls if isbase(p, c)}))