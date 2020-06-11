"""
file: node.py
language: python3
author: Bruce Herring
author: RIT CS Dept.
description:
   lecture code for mutable linked Node data type
"""

from dataclasses import dataclass
from typing import Any, Union

@dataclass
class Node:
    value: Any
    rest: Union[None, 'Node']
