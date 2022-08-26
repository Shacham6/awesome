# Shacham's Awesome List
This is my awesome list, for various things.
This is more for me, but if you find this list useful, cheers.

---
# Python
> Python related resources
- **[Python Enchancement Proposals - Index](https://peps.python.org/)**
## Guides
- **[fstring.help](https://fstring.help)** - A cheat-sheet website which provides insight towards the stuff possible with f-strings 
- **[Python File Modes Explanations](https://stackoverflow.com/a/23566951)** - All those `r w a r+ w+`, blah blah blah? An explanation for _those_. 
- **[Type Theory: Type Variance in Python](https://rednafi.github.io/reflections/variance-of-generic-types-in-python.html)**
- **[What's dictproxy?](https://stackoverflow.com/questions/25440694/whats-the-purpose-of-dictproxy)**
- **[Instagram - Copy-on-write friendly Python garbage collection](https://instagram-engineering.com/copy-on-write-friendly-python-garbage-collection-ad6ed5233ddf)**
- **[Python Decorators - Cool Example Tweet](https://twitter.com/nedbat/status/1543933895514591237?t=4jd5Q3dKPkOC6lsREeklQA&s=09)**
- **[Did you know that the Python 🐍 `functools.reduce` and `itertools.accumulate` are related?](https://twitter.com/mathsppblog/status/1556555347413852163?t=1jRlyQuEV3FQXITcQUdszg&s=09)**
- **[How I added C-style for-loops to Python](https://sadh.life/post/cursed-for/?s=09)**
### Setup-Tools
> Python's most popular build system.
- **[How to build a package with `pyproject.toml` (setuptools)](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)**
- **[How to build a package with `setup.cfg` (setuptools)](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html)**
## Awesome-Lists
> An aggregation of cool resources relating to a subject.
- **[Awesome Python AST](https://github.com/gyermolenko/awesome-python-ast)**
- **[Awesome pyproject](https://github.com/carlosperate/awesome-pyproject)**
## Misc.
> Stuff that didn't really fit in anywhere else.
- **[Classifiers List](https://pypi.org/pypi?%3Aaction=list_classifiers)** - An actual list of all legitimate classifiers to be used in Python packages. 
- **[undataclass](https://www.pythonmorsels.com/undataclass/?s=09)** - Given a definitions of `dataclasses.dataclass`, expose the generated source-code. 
- **[C vs Golang Python extension performance](https://ipdata.co/blog/c-vs-golang-python-extensions/)**
- **[The Bas Steins newsletter](https://bas.codes/)** - A newsletter that mentions multiple Python GitHub repositories. Like weekly "trending" for Python. 
- **[Pandas Alternatives](https://towardsdatascience.com/8-alternatives-to-pandas-for-processing-large-datasets-928fc927b08c)**
## Meta-Programming
- **[ast_selector](https://github.com/guilatrova/ast_selector)** - A package which allows __CSS selector style__ querying on Python AST's 
- **[datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator)** - Generates python code from schemas. 
- **[prestring](https://pypi.org/project/prestring/)** - A utility package to generate valid Pythonic Source-Code. 
## Functional Programming
- **[Pipe](https://github.com/JulienPalard/Pipe)** - A Python library to use infix notations in Python 
## Command-Line Interface
- **[Rich](https://github.com/Textualize/rich)** - Make beautiful CLI applications, very easily. 
## TUI (Terminal UI)
> Resources for Terminal UI.
- **[Textual](https://github.com/Textualize/textual)** - A TUI abstraction over Rich. Looks awesome! 
- **[pyTermTk](https://github.com/ceccopierangiolieugenio/pyTermTk)** - A Python TUI library. Not Textual. Still seemingly cool looking. Has graphs and stuff. 
## HTTP
### Clients
- **[httpx](https://www.python-httpx.org/)** - My favorite http client. 
- **[requests](https://pypi.org/project/requests/)** - The most known HTTP client for Python. 
- **[aiohttp](https://docs.aiohttp.org/en/stable/)** - Another popular http package w/ async support. 
### Server
- **[FastAPI](https://fastapi.tiangolo.com/)** - The most popular modern HTTP framework for Python as far as I know.
  - Supports OpenAPI generation and stuff.
  - Fast w/ async support.
  - Integrates well with Pydantic.
 
## Data Science
- **[streamlit](https://github.com/streamlit/streamlit)** - Let's you turn data scripts into sharable web apps. Not a self-hosted service. 
## Data Serialization
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - The most popular data-serialization framework for Python, as far as I know. 
- **[dill](https://pypi.org/project/dill/)** - An extension of python's `pickle` module. Pretty popular. 
### `YAML`
- **[oyaml](https://github.com/wimglenn/oyaml)** - YAML package that maintains the order of keys 
## Testing
> Resources to help with the process of testing your code.
- **[ward](https://github.com/darrenburns/ward)** - An interesting, alternative testing-framework for Python. All things considered I'd have preferred this one if pytest wasn't already the clear winner.. 
### Pytest
- **[pytest](https://docs.pytest.org/en/7.1.x/)** - The de-facto testing framework for Python 
- **[pytest-monitor](https://pypi.org/project/pytest-monitor/)**
- **[pytest-profiling](https://github.com/man-group/pytest-plugins/tree/master/pytest-profiling)**
- **[Awesome Pytest](https://github.com/augustogoulart/awesome-pytest)** - A list of `pytest` resources. 
- **[pytest-subsets](https://github.com/pytest-dev/pytest-subtests)** - Looks like a way to "split" a test into "segments"; With each being reported separately. 
- **[pytest-benchmark](https://github.com/ionelmc/pytest-benchmark)**
## Profilers
- **[memray](https://github.com/bloomberg/memray)** - A suddenly incredibly popular memory profiler. It was initially private as far as I know, and soon after it was released to the public it became immensely popular, very quickly. 
- **[line-profiler](https://pypi.org/project/line-profiler/)**
- **[memory-profiler](https://pypi.org/project/memory-profiler)**
- **[black](https://github.com/psf/black)** - The currently most popular automatic formatter for Python. Really rigid, but that's a "feature". 
- **PyPerf** - Toolkit to write, run and analyze benchmarks. Same idea as `Py-Spy`, but from kernel-space. 
- **py-spy** - sampling profiler for Python programs. 
- **[Pyroscope](https://pyroscope.io/)**
## Linter
- **[Flake8](https://flake8.pycqa.org/en/latest/)** - A popular Python linter that's more focused on coding conventions. 
- **[Bandit](https://github.com/PyCQA/bandit)** - A security linter from PyCQA 
### Pylint
- **[pylint](https://pylint.pycqa.org/en/latest/index.html)** - The pretty-much most popular linter for Python. Is __very__ involved in the code. Will be effective **only if used pragmatically**. 
- **[Pylint Message Control](https://pylint.pycqa.org/en/latest/user_guide/messages/message_control.html)**
## Security
- **[PyUP](https://pyup.io/)** - Python Dependency Security real-time service. Kinda like `snyk` from my understanding. 
## Files and Filesystem
- **[watchfiles](https://pypi.org/project/watchfiles/)** - A package to watch changes in local directory. 
- **[magicalimport](https://pypi.org/project/magicalimport/)** - Importing a module from physical file path. 
- **[pox](https://pypi.org/project/pox/)** - A collection of utilities for navigating and manipulating filesystems. 
- **[pathspec](https://pypi.org/project/pathspec/)** - A utility library for pattern matching of file paths. So far this only includes Git’s wildmatch pattern matching which itself is derived from Rsync’s wildmatch. 
## Documentation
- **[interrogate](https://github.com/econchick/interrogate)** - Validates that all of the things are documented? 
### mkdocs
- **[mkdocs](https://github.com/mkdocs/mkdocs)** - The best documentation generator for Programming Projects. Written in Python. Has a sweet GitHub-Pages integration. 
- **[mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)** - Automatic documentation from sources, for MkDocs. 
- **[mkdocs-click](https://pypi.org/project/mkdocs-click/)** - Generate mkdocs pages from `click` apps. 
## Tasks and Task Management
- **[huey](https://github.com/coleifer/huey)** - A small Task-Queue for Python 
- **[rocketry](https://github.com/Miksus/rocketry)** - A scheduling framework for Python. Strives for simplicity. 
## Concurrency
- **[pathos](https://pathos.readthedocs.io/en/latest/index.html)** - _"parallel graph management and execution in heterogeneous computing"_ 
- **[mpire](https://github.com/Slimmer-AI/mpire)** - `M`ulti`P`rocessing `I`s `R`eally `E`asy - Another concurrency package for Python 
## Refactoring
- **[pasta](https://github.com/google/pasta)** - A Python refactoring tool based on the `ast` module. Comes in the form of an SDK. 
## Meta / Tracing
- **[objgraph](https://mg.pov.lt/objgraph/)** - A module that lets you visually explore Python object graphs. 
## Applications
- **[dunk](https://github.com/darrenburns/dunk)** - Prettier git diffs. 
- **[mypyc](https://mypyc.readthedocs.io/en/latest/getting_started.html#installation)** - Compiled Python code to a Python extension. Based on type hinting. Seems to actually work! 
- **[Pokete](https://github.com/lxgr-linux/pokete)** - It's a Pokemon, but in a terminal. 
- **[Dinghy](https://pypi.org/project/dinghy/)** - A GitHub activity digest tool. 
## Clients
- **[Jira](https://pypi.org/project/jira/)** - A client for Jira. 
## Package Management
- **[pip-review](https://pypi.org/project/pip-review/)**
- **[pip-run](https://github.com/jaraco/pip-run)** - Run one-off Python scripts that have requirements (defined inlined) 
- **[distlib](https://github.com/pypa/distlib)**
# Rust
> Rust related resources
- **[lib.rs](https://lib.rs)**
## exercises
- **[Rustlings](https://github.com/rust-lang/rustlings)**
## Guides
- **[Rust Design Patterns - Idioms](https://rust-unofficial.github.io/patterns/idioms/index.html)** - An unofficial document describing Rust best practices and idioms. 
## Articles
- **[Rust Is Hard, Or: The Misery of Mainstream Programming](https://hirrolot.github.io/posts/rust-is-hard-or-the-misery-of-mainstream-programming.html)**
## Python
> Python related resources
- **[inline_python](https://docs.rs/inline-python/latest/inline_python/)**
- **[maturin](https://github.com/PyO3/maturin)**
- **[pyo3](https://github.com/PyO3/pyo3)** - Rust <-> Python bindings 
## Command-Line Interface
- **[scrawl](https://github.com/xvrqt/scrawl)** - A library that opens a user's text editor and returns the results as a string 
# Makefile
## Guides
- **[Makefile Tutorial](https://makefiletutorial.com/)**
# GitHub
- **[GraphQL Explorer](https://docs.github.com/en/graphql/overview/explorer)** - To explore the Github things with GraphQL. Looks cool actually. 
## Guides
- **[Creating A Reusable Workflow](https://docs.github.com/en/actions/using-workflows/reusing-workflows#creating-a-reusable-workflow)** - Package existing plans so that replication will be (allegedly) easy. 
- **[Webhooks & Payloads](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads)** - Documentation for the GitHub payloads 
## Actions
- **[Labeler](https://github.com/actions/labeler)** - Labels pull-requests, based on whether or not some files change. 
- **[Slash Command Dispatch](https://github.com/marketplace/actions/slash-command-dispatch)** - Helps to facilitate slash-commands 
- **[GitHub Actions For Jira](https://github.com/atlassian/gajira)**
### Awesome-Lists
> An aggregation of cool resources relating to a subject.
- **[Awesome Actions](https://github.com/sdras/awesome-actions)**
# Open-Source
## Applications
- **[myfreelogomaker](https://myfreelogomaker.com/)** - A website to generate logos that look good. Adi used it for my personal projects. 
- **[Choose a License](https://choosealicense.com/)** - Describes in relative ease the different licenses found in Open-Source projects. 
- **[Regexr](https://regexr.com/)** - A great site to build, test and learn Regex. 
## Guides
- **[Keep A Changelog](https://keepachangelog.com/en/1.0.0/)** - A reference for a Changelog file. 
- **[Semver](https://semver.org/)** - The __manifesto__ of semantic-versioning. 
# Guides
- **[System Design Primer](ttps://github.com/donnemartin/system-design-primer)** - A GitHub repository that provides lessons on systems design. 
- **[LeetDesign](https://leetdesign.com/)** - System Design Practice Problems 
# Data Science
- **[ml-ops.org](https://ml-ops.org/)** - A website detailing stuff about mlops. Just guessing it's popular to do it's leading position on Google's search results. 
## Guides
- **[MLOPs Primer](https://github.com/dair-ai/MLOPs-Primer)** - A Github repository in the same vein as System Design Primer. 
# Bash
## Cheat-Sheet
- **[Bash Cheatsheet](https://devhints.io/bash)** - A good cheatsheet for doing stuff in Bash (and Zsh). 
# Applications
- **[0.1 + 0.2 == 0.3000000004](https://0.30000000000000004.com/)** - Great example about how floating points work. 
# Cheat-Sheet
- **[Learn X in Y minutes](https://learnxinyminutes.com/)** - A great website to quickly learn programming languages and stuff, relatively quickly. Works as a cheatsheet. 
# jq
## Cheat-Sheet
- **[`jq` Cheatsheet](https://lzone.de/cheat-sheet/jq)** - A cheatsheet for all `jq` features 
## Applications
- **[`jq` Playground](https://jqplay.org/)** - A place to test `jq` queries. 
# `JSON`
- **[JSON Lines](https://jsonlines.org/)** - A format which is basically "streamable" json. 
- **[ndjson](http://ndjson.org/)** - Another format which is basically "streamable" json. Looks identical to JSON Lines. 
# `YAML`
- **[Advanced YAML syntax cheatsheet](https://www.educative.io/blog/advanced-yaml-syntax-cheatsheet)**
# GraphQL
## Guides
- **[Tutorial](https://graphql.org/learn/)** - Official GraphQL tutorial. 