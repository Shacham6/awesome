import pathlib
from typing import List, Mapping, Tuple, TypedDict, cast

import jinja2
import yaml

templates = jinja2.Environment(
    loader=jinja2.FileSystemLoader(pathlib.Path(__file__).parent.joinpath("templates"))
)

# block_template: jinja2.Template = jinja2.Template(
#     pathlib.Path(__file__).parent.joinpath("block_template.jinja2").read_text("utf-8")
# )
block_template = templates.get_template("block.jinja2")


class ContentItem(TypedDict):
    name: str
    description: str
    tags: List[str]


header_details, content_spec = cast(
    Tuple[
        Mapping[str, str],
        List[ContentItem],
    ],
    yaml.safe_load_all(
        pathlib.Path(__file__).parent.joinpath("content.yaml").read_text("utf-8")
    ),
)

groups = {}

for item in content_spec:
    g = groups
    if not item["tags"]:
        g = g.setdefault("Rest", {})
    for p in item["tags"]:
        g = g.setdefault(p, {})
    group_items = g.setdefault("_items", [])
    group_items.append(item)


md_content = [
    "# Shacham's Awesome List",
    "This is my awesome list, for various things.",
    "This is more for me, but if you find this list useful, cheers.",
    "",
    "---",
]


def walk(group_name, group: dict, level=1):
    # md_content.append(f"{'#' * level} {group_name}")
    # md_content.append(header_details.get(group_name, ""))

    md_content.append(templates.get_template("header.jinja2").render({
        "name": group_name,
        "level": level,
        "description": header_details.get(group_name, ""),
    }))

    for item in group.pop("_items", []):
        # md_content.append(f"- {item['name']} - {item['description']}")
        md_content.append(block_template.render(item))

    for inner_group_name, inner_group in group.items():
        walk(inner_group_name, inner_group, level + 1)


for group_name, group in groups.items():
    walk(group_name, group)

pathlib.Path("README.md").write_text("\n".join(md_content), encoding="utf-8")
