# pylint: disable=missing-module-docstring, missing-class-docstring
# pylint: disable=missing-function-docstring
from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel


class AwesomeListFile(BaseModel):
    header: ListHeader
    items: ListItems


class ListHeader(BaseModel):
    name: str
    description: str


class ListItems(BaseModel):
    __root__: List[
        Union[
            Group,
            Item,
        ]
    ]


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    link: Optional[str] = None
    levels: Optional[List[str]] = None


class Group(BaseModel):
    name: str
    children: ListItems
    description: Optional[str] = None
    link: Optional[str] = None
    levels: Optional[List[str]] = None


AwesomeListFile.update_forward_refs()
ListItems.update_forward_refs()
Item.update_forward_refs()
Group.update_forward_refs()
