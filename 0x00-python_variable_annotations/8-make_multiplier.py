#!/usr/bin/env python3
from typing import Callable
""" Basic Annotations """


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ basic function """

    def multi(n: float) -> float:
        return n*multiplier

    return multi
