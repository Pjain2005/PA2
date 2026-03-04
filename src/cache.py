from __future__ import annotations

from collections import deque
from typing import List, Tuple


def parse_input(path: str) -> Tuple[int, int, List[int]]:
    """
    Input format:
      line 1: k m
      line 2: r1 r2 ... rm
    """
    with open(path, "r", encoding="utf-8") as f:
        first = f.readline().strip().split()
        if len(first) != 2:
            raise ValueError("First line must be: k m")

        k = int(first[0])
        m = int(first[1])

        second = f.readline().strip().split()
        req = [int(x) for x in second]

        if len(req) != m:
            raise ValueError(f"Expected {m} requests, got {len(req)}")

    return k, m, req


def fifo_misses(k: int, req: List[int]) -> int:
    """
    FIFO eviction:
    -Cache holds up to k items.
    -On miss: if full, evict the item that has been in cache the longest.
    Returns the number of misses.
    """
    if k <= 0:
        return len(req)

    cache = set()
    order = deque()  #stores items in the order they were inserted (oldest on left)
    misses = 0

    for x in req:
        if x in cache:
            continue  #hit

        misses += 1  #miss
        if len(cache) < k:
            cache.add(x)
            order.append(x)
        else:
            evict = order.popleft()
            cache.remove(evict)
            cache.add(x)
            order.append(x)

    return misses


def lru_misses(k: int, req: List[int]) -> int:
    """
    LRU eviction:
    -keep track of items in cache.
    -keep a list that stores usage order.
      Front of list = least recently used
      End of list = most recently used
    """
    if k <= 0:
        return len(req)

    cache = set()
    usage_order = []   #left = least recent, right = most recent
    misses = 0

    for x in req:
        if x in cache:
            #move to the end (most recently used).
            usage_order.remove(x)
            usage_order.append(x)
        else:
            #a miss.
            misses += 1

            if len(cache) < k:
                #space available
                cache.add(x)
                usage_order.append(x)
            else:
                #cache full → remove least recently used
                lru_item = usage_order.pop(0)  #remove first element
                cache.remove(lru_item)

                cache.add(x)
                usage_order.append(x)

    return misses

def optff_misses(k: int, req: List[int]) -> int:
    if k <= 0:
        return len(req)
    
    m = len(req)
    INFINITY = float('inf')

    # Precompute the next use of each item after each position.
    # next_after[i] will be a dict mapping item to its next index >= i where it is requested again.
    next_after: List[dict] = [None] * (m + 1)
    next_after[m] = {}
    running: dict = {}
    for i in range(m - 1, -1, -1):
        running[req[i]] = i #update next use of req[i] to current index
        next_after[i] = dict(running) #make a copy of current next uses

    cache: set = set()
    misses = 0

    for i, x in enumerate(req):
        if x in cache:
            continue  #hit

        misses += 1  #miss
        if len(cache) < k:
            cache.add(x)
        else:
            # find the item in cache with the farthest next use
            future = next_after[i + 1] # next uses of items after current index
            evict = max(cache, key=lambda item: future.get(item, INFINITY))
            cache.remove(evict)
            cache.add(x)

    return misses
