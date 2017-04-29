import itertools
 
N = 99
count,lines = map(int, raw_input().split())
relations = {}
for i in xrange(lines):
    f,t = map(int, raw_input().split())
    f -= 1; t -= 1
    relations[f * N + t] = 1
_max = 1

fn = lambda v: relations.has_key(v[0] * N + v[1])

for i in xrange(2, count + 1):
    combi = itertools.combinations(xrange(count), i)

    for c in combi:
        c = itertools.combinations(c, 2)

        if all(map(fn, c)):
            _max = i
 
print _max