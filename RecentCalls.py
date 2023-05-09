#!/usr/bin/python3

class RecentCounter:

    def __init__(self):
        self._requests = []
    def ping(self, t):
        count = 0
        self._requests.append(t)
        for req in self._requests:
            if req in range(t-3000, t+1):
                count += 1
        return count    


# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(1,T+1):
    counter = RecentCounter()
    calls = list(map(int,input().split()))
    for ind,time in enumerate(calls):
        print(f'Case #{t}_{ind}: {counter.ping(time)}')