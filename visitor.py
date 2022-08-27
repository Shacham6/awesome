import pathlib
from typing import TypeVar

from jinja2 import Environment, FileSystemLoader

from specs import (
    AwesomeListFile,
    AwesomeListNode,
    Group,
    Item,
    ListHeader,
    ListItems,
    NodeVisitor,
)

_T = TypeVar("_T")


class MarkdownRenderer(NodeVisitor[str]):
    def __init__(self, templates_loader: Environment, level: int = 1):
        self.__templates_loader = templates_loader
        self.__level = level

    def handle(self, node: AwesomeListNode) -> str:
        return node.accept(self)

    def handle_awesome_list_file(self, node: AwesomeListFile) -> str:
        template = self.__templates_loader.get_template("awesome_list_file.jinja2")
        return template.render(
            handle=self.handle,
            header=node.header,
            items=node.items,
        )

    def handle_list_header(self, node: ListHeader) -> str:
        template = self.__templates_loader.get_template("list_header.jinja2")
        return template.render(
            handle=self.handle,
            name=node.name,
            description=node.description,
        )

    def handle_list_items(self, node: ListItems) -> str:
        template = self.__templates_loader.get_template("list_items.jinja2")
        return template.render(
            handle=self.handle,
            items=node.__root__,
        )

    def handle_item(self, node: Item) -> str:
        template = self.__templates_loader.get_template("item.jinja2")
        return template.render(
            handle=self.handle,
            name=node.name,
            description=node.description,
            link=node.link,
        )

    def handle_group(self, node: Group) -> str:
        template = self.__templates_loader.get_template("group.jinja2")
        return template.render(
            handle=MarkdownRenderer(self.__templates_loader, self.__level + 1).handle,
            name=node.name,
            children=node.children,
            description=node.description,
            link=node.link,
            level=self.__level + 1,
        )
