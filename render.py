import pathlib
from typing import Iterable

import yaml
from jinja2 import Environment, FileSystemLoader
from rich import print

import visitor
from specs import AwesomeListFile

__ROOT = pathlib.Path(__file__).parent
__TEMPLATES_DIR = __ROOT / "templates"
__SPECS_DIR = __ROOT / "specs"

__TEMPLATES = Environment(loader=FileSystemLoader(__TEMPLATES_DIR))

MANIFEST = yaml.safe_load(pathlib.Path("manifest.yaml").read_text("utf-8"))


def read_awesome_lists() -> Iterable[AwesomeListFile]:
    for spec_file in MANIFEST["specs"]:
        spec_file = pathlib.Path(spec_file)
        content = AwesomeListFile.parse_obj(
            yaml.safe_load(spec_file.read_text("utf-8"))
        )
        yield content


def main():
    buffers = []
    for awesome_list in read_awesome_lists():
        res = awesome_list.accept(visitor.MarkdownRenderer(__TEMPLATES))
        buffers.append(res)

    pathlib.Path("README.md").write_text("\n---\n".join(buffers), "utf-8")


if __name__ == "__main__":
    main()
