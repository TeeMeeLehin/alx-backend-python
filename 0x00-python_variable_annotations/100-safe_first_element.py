#!/usr/bin/env python3
""" Basic Annotations """
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ funtion doc """
    if lst:
        return lst[0]
    else:
        return None
