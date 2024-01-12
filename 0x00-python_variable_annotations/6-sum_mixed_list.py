#!/usr/bin/env python3
from typing import List, Union
""" Basic Annotations """

Flist = List[Union[int, float]]


def sum_mixed_list(mxd_list: Flist) -> float:
    """ basic sum function """
    return sum(mxd_list)
