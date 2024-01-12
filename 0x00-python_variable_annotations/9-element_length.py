#!/usr/bin/env python3
from typing import Callable
""" Basic Annotations """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function to return element length """
    return [(i, len(i)) for i in lst]
