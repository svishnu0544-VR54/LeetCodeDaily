"""
PYTHON DSA HANDY TOOLKIT
Save this file as: python_dsa_cheatsheet.py

Quick Python utilities useful for DSA / LeetCode / interviews
Includes typical time complexities.

---

1. SORTING

---

arr.sort()                 # In-place sort
sorted(arr)                # Returns new sorted list

Time Complexity:
Timsort
Best: O(n)
Average: O(n log n)
Worst: O(n log n)

Reverse sort
arr.sort(reverse=True)

Sort with key
arr.sort(key=lambda x: x[1])

---

2. SET (HashSet)

---

s = set()

s.add(x)
s.remove(x)
x in s

Remove duplicates
unique = list(set(arr))

Union
a | b

Intersection
a & b

Difference
a - b

Time Complexity:
Insert: O(1)
Delete: O(1)
Lookup: O(1)
Worst: O(n)

---

3. DICTIONARY (HashMap)

---

m = {}

m[key] = value
val = m[key]

Check existence
if key in m:

Iterate
for k, v in m.items():

Time Complexity:
Insert: O(1)
Delete: O(1)
Lookup: O(1)
Worst: O(n)

---

4. DEFAULTDICT

---

from collections import defaultdict

freq = defaultdict(int)
freq[x] += 1

group = defaultdict(list)
group[key].append(val)

Time Complexity:
Insert: O(1)
Lookup: O(1)

---

5. COUNTER (Frequency Map)

---

from collections import Counter

count = Counter(arr)

Most common
count.most_common(1)

Time Complexity:
Build Counter: O(n)
Lookup: O(1)

---

6. HEAP (Priority Queue)

---

import heapq

heap = []

heapq.heappush(heap, x)
heapq.heappop(heap)

Peek
heap[0]

Max heap trick
heapq.heappush(heap, -x)

Time Complexity:
Push: O(log n)
Pop: O(log n)
Peek: O(1)

---

7. BINARY SEARCH

---

import bisect

bisect.bisect_left(arr, x)
bisect.bisect_right(arr, x)

Insert in sorted order
bisect.insort(arr, x)

Time Complexity:
Search: O(log n)
Insert: O(n)

---

8. DEQUE (Double Ended Queue)

---

from collections import deque

q = deque()

q.append(x)
q.appendleft(x)

q.pop()
q.popleft()

Time Complexity:
Append: O(1)
Pop: O(1)

---

9. ENUMERATE

---

for i, val in enumerate(arr):
pass

Time Complexity:
O(n)

---

10. ZIP

---

for a, b in zip(arr1, arr2):
pass

Time Complexity:
O(n)

---

11. LIST COMPREHENSION

---

squares = [x*x for x in range(n)]

Filter
evens = [x for x in arr if x % 2 == 0]

Time Complexity:
O(n)

---

12. STRING TRICKS

---

Reverse string
s[::-1]

Sort string
''.join(sorted(s))

Check anagram
sorted(a) == sorted(b)

Time Complexity:
Sort: O(n log n)

---

13. MATRIX INITIALIZATION

---

Correct way

grid = [[0]*n for _ in range(m)]

Avoid

grid = [[0]*n]*m

---

14. INFINITY

---

import math

math.inf
-math.inf

---

15. SWAP

---

a, b = b, a

Time Complexity:
O(1)

---

16. REVERSE LIST

---

arr.reverse()

or

arr[::-1]

Time Complexity:
O(n)

---

17. RANGE

---

range(n)
range(1, n+1)
range(n, -1, -1)

Time Complexity:
O(1)

---

18. GRAPH (Adjacency List)

---

from collections import defaultdict

graph = defaultdict(list)

graph[u].append(v)

Time Complexity:
Add edge: O(1)

---

19. STACK

---

stack = []

stack.append(x)
stack.pop()

Time Complexity:
Push: O(1)
Pop: O(1)

---

20. COMMON BUILTINS

---

min(arr)          # O(n)
max(arr)          # O(n)
sum(arr)          # O(n)
len(arr)          # O(1)

any(arr)          # O(n)
all(arr)          # O(n)

---

21. FLATTEN LIST

---

flat = [x for row in matrix for x in row]

Time Complexity:
O(n)

---

22. FAST INPUT (Competitive Programming)

---

import sys

input = sys.stdin.readline

---

23. MOST IMPORTANT MODULES FOR DSA

---

collections
heapq
bisect
itertools
math
functools
operator
sys

"""
