xa, ya, xb, yb, xc, yc = map(int, raw_input().split())

print abs(0.5 * ((xa * yb - xb * ya) + (xb * yc - xc * yb) + (xc * ya - xa * yc)))