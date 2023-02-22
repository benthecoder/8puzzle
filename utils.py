# source: https://github.com/aimacode/aima-python/blob/master/utils.py

import functools
import heapq
import itertools


class PriorityQueue:
    """A Queue in which the minimum (or maximum) element (as determined by f and
    order) is returned first.
    If order is 'min', the item with minimum f(x) is
    returned first; if order is 'max', then it is the item with maximum f(x).
    Also supports dict-like lookup."""

    def __init__(self, order="min", f=lambda x: x):
        self.heap = []
        if order == "min":
            self.f = f
        elif order == "max":  # now item with max f(x)
            self.f = lambda x: -f(x)  # will be popped first
        else:
            raise ValueError("Order must be either 'min' or 'max'.")

    def append(self, item):
        """Insert item at its correct position."""
        heapq.heappush(self.heap, (self.f(item), item))

    def extend(self, items):
        """Insert each item in items at its correct position."""
        for item in items:
            self.append(item)

    def pop(self):
        """Pop and return the item (with min or max f(x) value)
        depending on the order."""
        if self.heap:
            return heapq.heappop(self.heap)[1]
        else:
            raise Exception("Trying to pop from empty PriorityQueue.")

    def __len__(self):
        """Return current capacity of PriorityQueue."""
        return len(self.heap)

    def __contains__(self, key):
        """Return True if the key is in PriorityQueue."""
        return any([item == key for _, item in self.heap])

    def __getitem__(self, key):
        """Returns the first value associated with key in PriorityQueue.
        Raises KeyError if key is not present."""
        for value, item in self.heap:
            if item == key:
                return value
        raise KeyError(str(key) + " is not in the priority queue")

    def __delitem__(self, key):
        """Delete the first occurrence of key."""
        try:
            del self.heap[[item == key for _, item in self.heap].index(True)]
        except ValueError:
            raise KeyError(str(key) + " is not in the priority queue")
        heapq.heapify(self.heap)


def is_in(elt, seq):
    """Similar to (elt in seq), but compares with 'is', not '=='."""
    return any(x is elt for x in seq)


def memoize(fn, slot=None, maxsize=32):
    """Memoize fn: make it remember the computed value for any argument list.
    If slot is specified, store result in that slot of first argument.
    If slot is false, use lru_cache for caching the values."""
    if slot:

        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val

    else:

        @functools.lru_cache(maxsize=maxsize)
        def memoized_fn(*args):
            return fn(*args)

    return memoized_fn


def itertools_flatten(nested):
    return tuple(itertools.chain.from_iterable(nested))


def rev_map(path):
    actions = {"U": "D", "D": "U", "L": "R", "R": "L"}
    return [actions[action] for action in path]


def print_puzzle(state):
    for i in range(0, 9, 3):
        print(" ".join([str(x) if x != 0 else "_" for x in state[i : i + 3]]))


def manhattan(node):
    state = list(node.state)
    index_goal = {
        0: [2, 2],
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
    }
    index_state = {}
    index = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    x, y = 0, 0

    for i in range(len(state)):
        index_state[state[i]] = index[i]

    mhd = 0

    for i in range(8):
        for j in range(2):
            mhd = abs(index_goal[i][j] - index_state[i][j]) + mhd

    return mhd


def linear(node):
    # goal state
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    return sum([1 if node.state[i] != goal[i] else 0 for i in range(8)])


def max_heuristic(node):
    """
    h3 is  the max heuristics of linear and manhattan distance
    """

    return max(linear(node), manhattan(node))


def parse_text_file(fpath):

    with open(fpath, "r") as f:
        lines = f.readlines()

    state = []

    for line in lines:
        row = line.strip().split()
        state.append([int(x) if x != "_" else 0 for x in row])

    state = itertools_flatten(state)

    return state
