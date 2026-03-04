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


#stubs (i will implement later)
def lru_misses(k: int, req: List[int]) -> int:
    raise NotImplementedError


def optff_misses(k: int, req: List[int]) -> int:
    raise NotImplementedError