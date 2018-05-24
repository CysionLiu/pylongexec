import heapq
from collections import Counter, deque


def de():
    d=deque()
    d.append(12)
    d.append(15)
    print(d)
    d.appendleft(25)
    d.append(300)
    print(d)
    d.appendleft(121)
    d.appendleft(211)
    print(d)
    d.pop()
    d.popleft()
    print(d)
if __name__ == '__main__':
    print(Counter('gsjkldfseifjsghljlefjslef'))
    print(Counter([3,12,34,12,3,21,23,12,34,56,76,76,3,2,12,34,76,25]))
    de()
    ll=[3,2,56,33,7,78,5,23,123,36,23,78,36,25]
    heapq.heapify(ll)
    print(ll)
