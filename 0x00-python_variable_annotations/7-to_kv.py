#!/usr/bin/env python3
from typing import Tuple, Union
""" Basic Annotations """


FT = Tuple[str, float]


def to_kv(k: str, v: Union[int, float]) -> FT:
    """ basic function """
    return (k, v*v)
