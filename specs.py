# pylint: disable=missing-module-docstring, missing-class-docstring
# pylint: disable=missing-function-docstring
from __future__ import annotations

import abc
from typing import Generic, List, Optional, Protocol, TypeVar, Union

from pydantic import BaseModel

_T = TypeVar("_T")


class NodeVisitor(Generic[_T], metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle_awesome_list_file(self, node: AwesomeListFile) -> _T:
        raise NotImplementedError

    @abc.abstractmethod
    def handle_list_header(self, node: ListHeader) -> _T:
        raise NotImplementedError

    @abc.abstractmethod
    def handle_list_items(self, node: ListItems) -> _T:
        raise NotImplementedError

    @abc.abstractmethod
    def handle_item(self, node: Item) -> _T:
        raise NotImplementedError

    @abc.abstractmethod
    def handle_group(self, node: Group) -> _T:
        raise NotImplementedError


class AwesomeListNode(BaseModel, metaclass=abc.ABCMeta):
    def accept(self, visitor: NodeVisitor[_T]) -> _T:
        raise NotImplementedError


class AwesomeListFile(AwesomeListNode):
    header: ListHeader
    items: ListItems

    def accept(self, visitor: NodeVisitor[_T]) -> _T:
        return visitor.handle_awesome_list_file(self)


class ListHeader(AwesomeListNode):
    name: str
    description: str

    def accept(self, visitor: NodeVisitor[_T]) -> _T:
        return visitor.handle_list_header(self)


class ListItems(AwesomeListNode):
    __root__: List[
        Union[
            Group,
            Item,
        ]
    ]

    def accept(self, visitor: NodeVisitor[_T]) -> _T:
        return visitor.handle_list_items(self)


class Item(AwesomeListNode):
    name: str
    description: Optional[str] = None
    link: Optional[str] = None
    levels: Optional[List[str]] = None

    def accept(self, visitor: NodeVisitor[_T]) -> _T:
        return visitor.handle_item(self)


class Group(AwesomeListNode):
    name: str
    children: ListItems
    description: Optional[str] = None
    link: Optional[str] = None
    levels: Optional[List[str]] = None

    def accept(self, visitor: NodeVisitor[_T]) -> _T:
        return visitor.handle_group(self)


AwesomeListFile.update_forward_refs()
ListItems.update_forward_refs()
Item.update_forward_refs()
Group.update_forward_refs()
