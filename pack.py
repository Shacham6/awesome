import pathlib
from typing import Iterable

import yaml
from jinja2 import Environment, FileSystemLoader
from rich import print

import visitor
from specs import AwesomeListFile

__ROOT = pathlib.Path(__file__).parent
__TEMPLATES_DIR = __ROOT / "templates2"
__SPECS_DIR = __ROOT / "specs"

__TEMPLATES = Environment(loader=FileSystemLoader(__TEMPLATES_DIR))


def read_awesome_lists() -> Iterable[AwesomeListFile]:
    for spec_file in __SPECS_DIR.glob("*.yaml"):
        content = AwesomeListFile.parse_obj(
            yaml.safe_load(spec_file.read_text("utf-8"))
        )
        yield content


def main():
    for awesome_list in read_awesome_lists():
        res = awesome_list.accept(visitor.MarkdownRenderer(__TEMPLATES))
        print(res)


if __name__ == "__main__":
    main()