#!/usr/bin/env python

doors = [False] * 100

for i in range(100):
        for j in range(i, 100, i+1):
            doors[j] = not doors[j]

for k, door in enumerate(doors):
    print ("Door %d is" % (k+1), "open." if door else "closed.")

doors