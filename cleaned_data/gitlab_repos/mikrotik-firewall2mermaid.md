# Repository Information
Name: mikrotik-firewall2mermaid

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/valsr/mikrotik-firewall2mermaid.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: .gitlab-ci.yml
================================================
image: python:3.10
stages:
  - lint
  - build
  - release
variables:
  PACKAGE_REGISTRY_URL_ROOT: "${CI_API_V4_URL}/projects/${CI_PROJECT_ID}/packages/generic/releases/"
  PACKAGE_NAME: "firweall2mermaid"
Python Code Lint:
  stage: lint
  before_script:
    - pip install poetry
    - poetry config virtualenvs.create false
    - poetry install
  script: poetry run black .
Static Type check:
  stage: lint
  before_script:
    - pip install poetry
    - poetry config virtualenvs.create false
    - poetry install
  script: poetry run mypy src
Unit Tests:
  stage: lint
  before_script:
    - pip install poetry
    - poetry config virtualenvs.create false
    - poetry install
  script: poetry run pytest --cov tests
Build Code:
  stage: build
  before_script:
    - pip install poetry
    - poetry config virtualenvs.create false
    - poetry install
  script:
    - poetry build
    - echo "TAG=$(cat pyproject.toml | grep version | cut -d\" -f 2)" >> variables.env
  artifacts:
    paths:
      - dist/*.whl
      - dist/*.tar.gz
    reports:
      dotenv: variables.env
    when: on_success
    expire_in: 30 days
  rules:
    - if: $CI_COMMIT_TAG
      when: never
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
Upload Artifacts:
  stage: release
  image: curlimages/curl:latest
  needs:
    - job: "Build Code"
      artifacts: true
  rules:
    - if: $CI_COMMIT_TAG
      when: never
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  script:
    - echo "Packaging assets for release ${TAG}"
    - 'curl --header "JOB-TOKEN: $CI_JOB_TOKEN" --upload-file dist/firewall2mermaid-${TAG}-py3-none-any.whl "${PACKAGE_REGISTRY_URL_ROOT}/${TAG}/${PACKAGE_NAME}-${TAG}-py3-none-any.whl"'
    - 'curl --header "JOB-TOKEN: $CI_JOB_TOKEN" --upload-file dist/firewall2mermaid-${TAG}.tar.gz "${PACKAGE_REGISTRY_URL_ROOT}/${TAG}/${PACKAGE_NAME}-${TAG}.tar.gz"'
Create Release:
  stage: release
  image: registry.gitlab.com/gitlab-org/release-cli:latest
  needs:
    - job: "Upload Artifacts"
    - job: "Build Code"
      artifacts: true
  rules:
    - if: $CI_COMMIT_TAG
      when: never
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  script:
    - echo "Releasing $TAG"
  release:
    name: '$TAG'
    tag_name: '$TAG'
    description: 'Created using release pipeline'
    ref: '$CI_COMMIT_SHA'
    assets:
      links:
        - name: "${PACKAGE_NAME}-${TAG}-py3-none-any.whl"
          url: "${PACKAGE_REGISTRY_URL_ROOT}/${TAG}/${PACKAGE_NAME}-${TAG}-py3-none-any.whl"
        - name: "${PACKAGE_NAME}-${TAG}.tar.gz"
          url: "${PACKAGE_REGISTRY_URL_ROOT}/${TAG}/${PACKAGE_NAME}-${TAG}.tar.gz"
================================================

File: Contributing.md
================================================
# How to contribute
[< back to readme](README.md)
You want to contribute? Awesome. Lets get through the gritty details so that we can get your code
home! This guide should help you at least a little bit in getting there, you might need to add some
elbow-grease and some patience as well.
## TOC
1. [Getting Started](#getting-started)
1. [Set Up Local Environment](#set-up-local-environment)
1. [Making Changes](#making-changes)
1. [Testing Changes](#testing-changes)
1. [Submitting Changes](#submitting-changes)
1. [Get Help](#get-help)
## Getting Started
Submitting changes follows a simple process can be summarized in the following diagram:
```mermaid
%%{init: {'flowchart': {'htmlLabels': false}, 'theme': 'dark'}}%%
flowchart LR
fork ---> code ---> test ---> lint ---> pr[pull request]
```
Your first step will be to fork the repository, which means you will need a
[gitlab account](https://gitlab.com/). Once you fork the repository you will need to can begin
making your changes.
## Set Up Local Environment
To setup a local environment for development you will need to have the following installed:
- [Git](https://git-scm.com)
- [Python (3.10+)](https://www.python.org/)
- [Poetry](https://python-poetry.org)
Once the prerequisites are installed, you can setup the environment by following the steps bellow:
1. Clone git repository
   ```bash
   git clone https://gitlab.com/valsr/mikrotik-firewall2mermaid /some/path
   ```
1. Open terminal/shell inside the cloned repository and then run the following to setup the project:
   ```bash
   poetry install
   ```
## Generating Graphs/Running
Once you have setup the system you can execute the application by running `poetry run app ...`.
```bash
poetry run app --input mikrotik_export.rsc
# will only output graph details for the filter firwall section and only input chain (and sub-chains)
poetry run app --input mikrotik_export.rsc --graph filter:input,-:
```
This will parse the export file `mikrotik_export.rsc` and generate a mermaid file
`mikrotik_export.mmd` based on the firewall rules.
For other options see [Command Line Options](README.md#command-line-options).
## Making Changes
How you do your work is up to you, we don't have many rules to follow but if you would want to make
the entire PR process smoothers follow the general steps below:
1. Create a topic branch from where you want to base your work
   - This is usually the **main** branch
   - Only target **release branches** if you are certain your fix must be on that branch
1. Make commits of *logical* and *atomic* units
1. Make sure your commit messages are in the proper format
1. Make sure you have added the necessary tests for your changes
### Making Trivial Changes
For trivial changes (documentation updates, typo corrections, any small non-code changes) you can
omit most of the requirements - just fork/branch-commit-pull request will suffice. If the change is
not a minor one, then your pull request will be rejected and you will need to resubmit using the
standard process.
## Testing Changes
Before submitting your changes, make sure that all tests pass. To run the tests:
```bash
poetry run pytest src
```
In addition add tests for your modifications and ensure that a good enough coverate is followed
(70%+ for non-critical code, 90%+ for critical code).
## Submitting Changes
Once your changes are ready to go you will need to do the following:
1. Rebase your changes on top of the most recent version of the branch you want to merge to
1. Verify your changes are okay:
   - Make sure they are well documented
   - Make sure you have tested them locally
   - Make sure the project builds and installs/updates properly
1. Create a pull request and follow the request template
1. Once your changes have been reviewed you might need to perform corrections based on the feedback
  from the PR
If any of these stages fail, you will need to amend your PR to address the issues found.
## Get Help
If you need more help with any aspect of the project or how to submit your work you can create an
issue and tag it as a `question`!
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2023 valsr
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
================================================

File: README.md
================================================
# firewall2mermaid
[![pipeline status](https://gitlab.com/valsr/mikrotik-firewall2mermaid/badges/main/pipeline.svg)](https://gitlab.com/valsr/mikrotik-firewall2mermaid/-/commits/main)
[![coverage report](https://gitlab.com/valsr/mikrotik-firewall2mermaid/badges/main/coverage.svg)](https://gitlab.com/valsr/mikrotik-firewall2mermaid/-/commits/main)
[![Latest Release](https://gitlab.com/valsr/mikrotik-firewall2mermaid/-/badges/release.svg)](https://gitlab.com/valsr/mikrotik-firewall2mermaid/-/releases)
Generate mermaid graphs for MikroTik firewall rules.
## Installing Application
Download the latest release from https://gitlab.com/valsr-personal/mikrotik-firewall2mermaid/-/releases.
Once downloaded you can install it by
```bash
pip install firweall2mermaid-x.x.x-py3-none-any.whl
```
## Generating Graphs/Running
Once you have setup the system you can simply execute the poetry scripts as follow:
```bash
firewall2mermaid --input mikrotik_export.rsc
```
This will parse the export file `mikrotik_export.rsc` and generate a mermaid file
`mikrotik_export.mmd` based on the firewall rules. For advance usage see
[Advance Usage](#advance-usage).
### Command Line Options
> You can always use `-h` to see command help
You can customize the output generation by setting the following option/flags:
| argument                            | description                                                        |
| ----------------------------------- | ------------------------------------------------------------------ |
| -h, --help                          | The build in help screen                                           |
| --version                           | Application version                                                |
| --input                             | Miktoritk input file                                               |
| --output                            | Path to the output file (defaults to `<input>.mmd`)                |
| --graph                             | Graph selector/specified (See [Graph Selectors](#graph-selectors)) |
| --comments                          | Determine how to handle comments on graph nodes                    |
| --show-logs, --no-show-logs         | Whether to show nodes of action="log"                              |
| --show-disabled, --no-show-disabled | whether to show disabled nodes                                     |
| --show-legend, --no-show-legend     | Whether to shoe the node type legend                               |
| --direction                         | Graph direction                                                    |
| --log-rules                         | Whether to log the rules as comments at the start of the graph     |
| --flow, --add-flow-elements         | Add upstream/downstream flow elements                              |
| --colapse-as-rule                   | Each collapse element will be modeled as rule                      |
| --rootless                          | Do not render the root outline/box                                 |
| --log-command                       | Log the executing command as comment in the graph                  |
| -v, --verbose                       | Increase verbosity                                                 |
## Notes
### Output file
When not specified the output file will be generated based on the input file by replacing the
file extension, typically `.rsc`, with `.mmd`
```bash
firewall2mermaid --input /path/to/my/file.rsc # Output will be `/path/to/my/file.mmd`
```
## Advance Usage
### Graph Selectors
You can use graph selectors to alter how the firewall rules are render. With selectors you can set
which sections/chains are rendered, which are hidden, which are collapsed and which are splatted.
Selectores are specified in the `--graph` flag in a comma separated value list. Selectors are
applied in the order they are read, with first selector having the highest precedence, while the
last selector having the lower precedence. If, by chance, no selector matches the section/chain, it
will default to render/show it. For that reason, when using `--graph` flag alway include the default
`:` selector as the very last one.
Each selector is broken down into three parts - `[mod][section]:[chain]`. The modifier `[mod]` is
operation to apply to the given section/chain and is one of the following:
- +: Render the section/chain normally (can also be omitted)
- *: Splat the given section/chain - [Splatting Sections/Chains](#splatting-sectionschains)
- %: Collapsed the given section/chain - [Collapsing Sections/Chains](#collapsing-sectionschains)
- -: Hide the given section/chain - [Hidding Sections/Chains](#hidding-sectionschains)
The `[section]`/`[chain]` specifier will match the given section and/or chains. If omitted, the
selector will assume to match all section/chains. Note that in order to omit the section specifier
you will either need to specify a chain `:input` or the global selectors `:`, `-` (any modification
character on their own).
```bash
... --graph filter # Renders the filter section
... --graph filter:input,-:input # Render the filter input chain, hides all other input chains
... --graph filter:input,-:input,%: # Render the filter input chain, hides all other input chains, collapsed all other chains
```
```bash
firewall2mermaid --input file.rsc --graph +filter,-:input,*mangle:,%:
# The selectors above will do the following:
# 1. Render `filter` section
# 2. Hide/remove all chains named `input`
# 3. Splat all chains in `mangle` (except input due to precedence)
# 4. Collapse remaining chains
```
### Hidding Sections/Chains
Hidding sections and chains removes them from the rendered graph completely. This include removing
links, rules that point to sections/chains. In many cases the global selector `-:` is used to remove
all other chains not already part of the preceding selectors.
```bash
firewall2mermaid --input file.rsc --graph -filter,-:input,+:
# In here `-filter`: Removes filter section and its decendants (chains/rules) as well as their
# links. `-:input` removes all chains named `input` as well as its decendants (chains/rules).
```
### Collapsing Sections/Chains
Collapsing a section/chain replace the entire section/chain with a single node with the chain name.
This is useful to simplify the output diagram by removing nodes while still maintaining
relationships between all nodes. When collapsing nodes, all links will be repointed to the collapsed
node - e.g. jump rule link will now be pointing form the collapsed parent.
Note `collapsed-as-rule` modifies how collapsed nodes are rendered. This option will model collapsed
nodes as a rule place in the chains where the node is linked from thus forming a continuation of the
chain.
### Splatting Sections/Chains
Splatting allows to take a chain and render it as its own parent node - i.e. treat it as a section
node. This is useful when wanting to simplify the diagram by decreesing the nesting of chains inside
sections.
### Flow
This option will add default the missing setions and chains from the packet flow perspective. That
is it will add a node for the following missed chains:
- Prerouting chians for Mangle, and NAT (called dstnat) sections
- Input chains for Mangle and Filter sections
- Forward chains for Mangle and Filter sections
- Output chains for Mangle and Filter sections
- Postrouting chains for Mangle and NAT (called srcnat)
The addition will respect all graph selectors except the global graph selectors.
### Contributing
See [Contributing](Contributing.md) if you are planning to contribute (i.e. submit PR/MR/Patches).
================================================

File: app.py
================================================
"""Application startup logic."""
import logging
import os
import argparse
import re
import sys
import importlib.metadata
from firewall2mermaid.common import GRAPH_SELECTOR_PATTERN, parse_list
from firewall2mermaid.errors import InvalidGraphSelector
from firewall2mermaid.model import GraphSelector, ParserRule
from firewall2mermaid.parser import parse_rules
from firewall2mermaid.render import Renderer
from firewall2mermaid.tree import TreeMaker
class NegateAction(argparse.Action):
    """Utility to construct toggle command line options (i.e. --show --no-show)."""
    def __call__(self, parser, namespace, values, option_string=None):
        if option_string:
            setattr(namespace, self.dest, option_string[2:4] != "no")
def main():
    """CLI main entry point."""
    args = create_parser().parse_args()
    setup_logging(args.verbose)
    logging.debug("Args: %s", args)
    parsed_elements = parse_graph_selector(parse_list(args.graph))
    logging.debug("Parsed graph elements: %s", parsed_elements)
    output_file: str = determine_output_filename(args.input, args.output)
    extra_args = []
    if args.log_command:
        command_arg = "Command: " + " ".join(sys.argv[1:])
        extra_args.append(command_arg)
    execute(
        args.input,
        parsed_elements,
        output_file,
        show_logs=args.show_logs,
        show_disabled=args.show_disabled,
        comments=args.comments[0],
        show_legend=args.show_legend,
        direction=args.direction[0] if args.direction else "TB",
        log_rules=args.log_rules,
        add_flow_elements=args.flow,
        collapse_as_rule=args.collapsed_as_rule,
        show_root=not args.rootless,
        extra_logs=extra_args,
    )
def setup_logging(verbose: bool):
    """Setup logging.
    Args:
        verbose (bool): Whether to use verbose loggin
    """
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s - %(levelname)s - %(message)s")
def is_file_valid(parser, arg):
    """
    Check if the given file is valid and readable.
    Args:
        parser (argparse.ArgumentParser): The argument parser object.
        arg (str): The file path to check.
    Returns:
        str: The valid file path. False if not valid
    """
    if not os.path.isfile(arg) or not os.access(arg, os.R_OK):
        parser.error("The file %s does not exist or we can't read it!", arg)
        return False
    return arg
def create_parser() -> argparse.ArgumentParser:
    """Construct argument parser.
    Returns:
        argparse.ArgumentParser: Application parser
    """
    parser = argparse.ArgumentParser(
        description="Graph MikroTik firewall rules to mermaid js",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    version = importlib.metadata.metadata("firewall2mermaid")["Version"]
    parser.add_argument("--version", action="version", version=version)
    parser.add_argument(
        "--input",
        required=True,
        metavar="FILE",
        type=lambda x: is_file_valid(parser, x),
        help="Path to the input file containing firewall rules",
    )
    parser.add_argument(
        "--output",
        help="Path to the output file to store the processed results (default: input.mmd)",
    )
    parser.add_argument(
        "--graph",
        nargs="+",
        help="""Graph selected elements. Specify items using graph selector format -
`[mod]section:chain`. 'mod' are optional characters that modifies how the elements are graphed,
when present they have the meaning:
- +: Render the given section/chain normally
- *: Will splat the given section/chain (i.e. render ungrouped)
- -: Will not render the given section/chain (note takes precedence over other modifiers)
- %%: Will collapse the given section/chain
Either section or chain may be omitted to specify 'all' elements of that type.
For example ':ddos' will graph all chains named 'ddos' of all sections. Similarly 'raw:' or 'raw'
will graph the entire 'raw' section.
You can use ':' as a global selector to catch all-else scenarios. For example '-:' will hide all
element that are not explicitly selected. Similarly '+:' will render all elements that are not""",
    )
    parser.add_argument(
        "--comments",
        "--comment-handling",
        "--node-comments",
        choices=["show", "hide", "auto", "prefer"],
        default="auto",
        nargs=1,
        help="Show/hide comments on graph nodes",
    )
    parser.add_argument(
        "--show-logs",
        "--no-show-logs",
        action=NegateAction,
        dest="show_logs",
        default=False,
        help="Shows log nodes",
        nargs=0,
    )
    parser.add_argument(
        "--show-disabled",
        "--no-show-disabled",
        action=NegateAction,
        dest="show_disabled",
        default=False,
        help="Shows disabled nodes",
        nargs=0,
    )
    parser.add_argument(
        "--show-legend",
        "--no-show-legend",
        action=NegateAction,
        dest="show_legend",
        default=True,
        help="Shows node legend",
        nargs=0,
    )
    parser.add_argument(
        "--direction",
        choices=["TB", "BT", "LR", "RL"],
        help="Graph direction",
        default=["TB"],
        nargs=1,
    )
    parser.add_argument(
        "--log-rules",
        action="store_true",
        default=False,
        help="Add a comment/log for each rule in the graph",
    )
    parser.add_argument(
        "--flow",
        "--add-flow-elements",
        action="store_true",
        default=False,
        help="Add upstream/downstream flow elements (as in packet flow)",
    )
    parser.add_argument(
        "--collapsed-as-rule",
        "--collapse-as-rule",
        action="store_true",
        default=False,
        help="Render collapsed elements as rules in current chain/section",
    )
    parser.add_argument(
        "--rootless",
        "--no-root",
        action="store_true",
        default=False,
        help="Render graph without root node",
    )
    parser.add_argument(
        "--log-command",
        action="store_true",
        default=False,
        help="Log execution command line",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Increase verbosity")
    return parser
def determine_output_filename(
    input_file_arg: str,
    output_arg: str | None,
) -> str:
    """Determine output file path for given input parameters.
    Args:
        input_file_arg (str): Input file argument
        output_arg (str | None): Output file argument (if specified)
    Returns:
        str: Output file path.
    """
    if not output_arg:
        output_arg = os.path.splitext(input_file_arg)[0]
        output_arg += ".mmd"
    return output_arg
def execute(
    file_path: str,
    graph: list[GraphSelector],
    output_file: str,
    show_disabled=False,
    show_logs=False,
    comments="auto",
    show_legend=True,
    direction="TB",
    log_rules=False,
    add_flow_elements=False,
    collapse_as_rule=False,
    show_root=True,
    extra_logs: list[str] | None = None,
):
    """Main application execution.
    Args:
        file_path (str): Input file (Mikrotik file)
        graph (list[GraphSelector]): List of elements to graph.
        output_file (str): Output file (where to store graph file)
        show_disabled (bool, optional): Show disabled nodes on graph. Defaults to False.
        show_logs (bool, optional): Show log nodes. Defaults to False.
        comments (str, optional): Node comment handling. Defaults to 'auto'.
        show_legend (bool, optional): Show legend nodes. Defaults to True.
        direction (str, optional): Overall graph direction. Defaults to "TB".
        log_rules (bool, optional): Log all rules as comments at the beginning of the graph.
            Defaults to False.
        add_flow_elements (bool, optional): Add upstream elements (chains, sections, etc).
            Defaults to False.
        collapse_as_rules (bool, optional): Render collapsed chains as rules instead. Defaults to
            False.
        show_root (bool, optional): Render graph with root node. Defaults to True.
    """
    extra_logs = extra_logs or []
    rules: list[ParserRule] = parse_rules(file_path)
    tree_maker = TreeMaker(
        parsed_rules=rules,
        elements=graph,
        prune_disabled_rules=not show_disabled,
        prune_log_rules=not show_logs,
        add_flow_elements=add_flow_elements,
    )
    root = tree_maker.make_tree()
    renderer = Renderer(
        root,
        graph_selector=graph,
        node_render_mode=comments,
        show_legend=show_legend,
        graph_direction=direction,
        log_rules=log_rules,
        collapse_as_rule=collapse_as_rule,
        show_root=show_root,
        extra_logs=extra_logs,
    )
    graph_text = renderer.render_graph()
    with open(output_file, "w", encoding="utf-8") as out_file:
        out_file.write(graph_text)
        logging.info("Graph data save to %s", output_file)
def parse_graph_selector(elements: list[str]) -> list[GraphSelector]:
    """
    Parses a list of graph selector elements and returns a list of GraphSelector objects.
    Args:
        elements (list[str]): The list of graph selector elements to parse.
    Returns:
        list[GraphSelector]: A list of GraphSelector objects.
    Raises:
        InvalidGraphSelector: If an element in the list does not match the expected pattern.
    """
    p = re.compile(GRAPH_SELECTOR_PATTERN)
    t: list[GraphSelector] = []
    for element in elements:
        m = p.match(element)
        if not m:
            raise InvalidGraphSelector(element)
        d = m.groupdict()
        t.append(GraphSelector(d["id"] or "", mod=d["mod"] or ""))
    return t
================================================

File: common.py
================================================
"""Common/utility functions and definitions used by the entire application."""
from __future__ import annotations
import sys
from typing import Callable
from firewall2mermaid.model import GraphSelector, PacketFlowElement, Rule, TreeNode
# Detached element name
DETACHED = "detached"
GRAPH_SELECTOR_PATTERN = r"^(?P<mod>[+*\-%]+)?(?P<id>[^:\s]*(:[^:\s]*){0,2})$"
# Natural sort order of section
SECTION_SORT_ORDER = ["legend", "raw", "mangle", "nat", "filter"]
def section_sort_key(name: str) -> int:
    """Create section sort key.
    Args:
        name (str): Section name
    Returns:
        int: Sort key
    """
    return SECTION_SORT_ORDER.index(name) if name in SECTION_SORT_ORDER else sys.maxsize
# class/styles definitions
CLASS_DEF = {
    "accept": "fill:#2c8c57",
    "tarpit": "fill:#2c8c57",
    "drop": "fill:#8c2c61",
    "src-nat": "fill:#8c572c",
    "dst-nat": "fill:#8c572c",
    "masquerade": "fill:#8c572c",
    "log": "fill:#686d6d",
    "jump": "fill:#44797f",
    "return": "fill:#44797f",
    "passthrough": "fill:#686d6d",
    "fasttrack-connection": "fill:#686d6d",
    "disabled": "fill:#444444",
    "collapsed": "fill:#47605e",
}
def __generate_flow(order: list[tuple[str, str]]) -> PacketFlowElement:
    """Generate flow for given list of ordered tuples (section, chain)
    Args:
        order (list[tuple[str, str]]): List of ordered flow elements (section, chain)
    Returns:
        PacketFlowElement: Root flow element
    """
    root = PacketFlowElement(order[0][0], chain=order[0][1])
    element = root
    for item in order[1:]:
        flow = PacketFlowElement(item[0], item[1])
        element.next = flow
        element = flow
    return root
TAB_CHARACTER = "\t"
"""Tabular character to use for indentation"""
FIREWALL_LINE_START = "/ip firewall"
"""firewall line start"""
LINK_STYLE_BETWEEN_SECTIONS = "-.->"
"""link style between sections"""
LINK_STYLE_NORMAL = "-->"
"""Default link style"""
LINK_STYLE_NORMAL_LONGER = "--->"
"""Elongated link style"""
LINK_STYLE_INVISIBLE = "~~~"
"""Invisible link style"""
DEFAULT_LINK_LABEL = "otherwise"
"""Default link label"""
PREROUTING_FLOW = __generate_flow(
    [("raw", "prerouting"), ("mangle", "prerouting"), ("nat", "dstnat")]
)
"""Packet flow for prerouting phase"""
INPUT_FLOW = __generate_flow([("mangle", "input"), ("filter", "input")])
"""Packet flow for input phase"""
FORWARD_FLOW = __generate_flow([("mangle", "forward"), ("filter", "forward")])
"""Packet flow for forward phase"""
OUTPUT_FLOW = __generate_flow([("raw", "output"), ("mangle", "output"), ("filter", "output")])
"""Packet flow for output phase"""
POSTROUTING_FLOW = __generate_flow([("mangle", "postrouting"), ("nat", "srcnat")])
"""Packet flow for postrouting phase"""
ALL_FLOWS = [PREROUTING_FLOW, INPUT_FLOW, FORWARD_FLOW, OUTPUT_FLOW, POSTROUTING_FLOW]
"""All known flows"""
def find_jump_target_rule(rule: Rule) -> Rule | None:
    """Get the first rule of the chain corresponding to the rule's jump target parameter.
    Args:
        rule (Rule): Jump rule
    Returns:
        Rule|None: Rule or None
    """
    if not rule.jump_target:
        return None
    jump_chain = rule.jump_target_chain()
    if not jump_chain:
        return None
    return jump_chain.first_rule()
def parse_list(list_arg: list[str], sort_key: Callable | None = None) -> list[str]:
    """Parsing list from so that we can also use ',' as separator.
    Args:
        list_arg (list[str]): Input parameters
        sort_key (Callable, optional): If set sort the list using this as sort key parameter
    Returns:
        list[str]: Parsed and sorted list
    """
    l = []
    if list_arg:
        l = [item for x in list_arg for item in x.split(",")]
    if sort_key:
        l.sort(key=sort_key)
    return l
def dedup(items: list) -> list:
    """Deduplicate items in list using equality.
    Args:
        list (list): List to deduplicate
    Returns:
        list: New list with deduplicated items removed
    """
    deduped = []
    for item in items:
        if item not in deduped:
            deduped.append(item)
    return deduped
def create_adhoc_rule(section: str, chain: str, index: int, **kwargs: str) -> Rule:
    """Create adhock rule from given parameters.
    Args:
        section (str): Firewall section
        chain (str): Parent chain name
        index (int): Rule index
        kwargs (dict): Additional rule attributes
    Returns:
        Rule: Created rule
    """
    attributes: dict[str, str] = {"action": "accept", "chain": chain}
    for k, v in kwargs.items():
        attributes[k.replace("-", "_")] = v
    line_args = " ".join([f"{k}={v}" for k, v in attributes.items()])
    line = f"{FIREWALL_LINE_START} {section} add {line_args}"
    return Rule(line, index, attributes)
def get_effective_selector(
    selectors: list[GraphSelector], element_or_id: str | TreeNode
) -> GraphSelector:
    """
    Finds and returns the most applicable GraphSelector for given element or identifier. Selection
    logic is as fallow:
    1. Fully qualified match
    2. Same level selector (precedence by lowest number of wildcards and right most components as
        wildcards) i.e. section:chain:* > section:*:rule > section:*:* > *:*:rule > *:*:*
    3. Default
    Args:
        selectors (list[GraphSelector]): List of selectors
        element_or_id (str|Chain|Section|Rule): Element or id to match
    Returns:
        GraphSelector: Most applicable selector or default selector if no match found
    """
    element_id = element_or_id.id if isinstance(element_or_id, TreeNode) else element_or_id
    id_components = element_id.split(":")
    depth = len(id_components)
    level_selectors = [x for x in selectors if x.depth == depth]
    closest_match: tuple[int, GraphSelector] | None = None
    for selector in level_selectors:
        match_score = _compute_selector_score(id_components, selector)
        if match_score == 0:
            continue
        if match_score == 1:
            return selector
        if not closest_match or closest_match[0] > match_score:
            closest_match = (match_score, selector)
    if closest_match:
        return closest_match[1]
    return GraphSelector("")  # always true graph selector (no selectors specified)
def _compute_selector_score(id_components: list[str], selector: GraphSelector):
    """
    Computes the score of a given selector based on the provided id components.
    Args:
        id_components (list[str]): The list of ID components.
        selector (GraphSelector): The selector object to compute the score for.
    Returns:
        int: The computed score for the selector. Lower scores means closer match with 1 meaning
        perfect match and 0 means no match. Scoring values higher than 1 are related to the number
        and position of wildcards in the selector. The higher the score the less specific the
        selector. Sample example (* indicates selector wildcard match):
            - <match>:<match>:<match> => score 1
            - <match>:<match>:* => score 2
            - <match>:*:<match> => score 4
            - <match>:*:* => score 6
            - *:<match>:<match> => score 8
            - *:<match>:* => 10
            - *:*:<match> => score 12
    """
    l = len(id_components)
    components = selector.selectors
    if len(components) < l:
        return 0
    score = 1
    for i, component in enumerate(id_components):
        if not components[i]:
            score = score + (l - i) ** 2
        elif component != components[i]:
            return 0
    return score
================================================

File: errors.py
================================================
"""Error definitions for application."""
class ApplicationError(Exception):
    """Custom exception class for application errors.
    This class represents an exception that is raised when an error occurs within the application.
    It inherits from the base Exception class.
    Attributes:
        message (str): The error message associated with the exception.
    """
    def __init__(self, message):
        self.message = message
    def __str__(self) -> str:
        return self.message
class InvalidGraphSelector(ApplicationError):
    """Invalid graph selector."""
    def __init__(self, selector):
        super().__init__(f"Invalid graph selector '{selector}'")
        self.selector = selector
class ElementNotFound(ApplicationError):
    """Element not found exception."""
    def __init__(self, name):
        super().__init__(f"Invalid element '{name}'")
        self.element = name
class SectionAlreadyExistsError(ApplicationError):
    """Raised when attempted to add a section that already exists in the current root node."""
    def __init__(self, name):
        super().__init__(f"Section '{name}' already exists in the root node")
        self.name = name
class ChainAlreadyExistsError(ApplicationError):
    """Raised when attempted to add a chain that already exists in the current section."""
    def __init__(self, name, section):
        super().__init__(f"Chain '{name}' already exists in {section}")
        self.name = name
================================================

File: model.py
================================================
"""Graph AST model"""
from __future__ import annotations
from functools import total_ordering
import logging
from typing import Any, Mapping
from firewall2mermaid.errors import (
    ChainAlreadyExistsError,
    ElementNotFound,
    SectionAlreadyExistsError,
)
DETACHED = "detached"
class GraphSelector:
    """Used to modify graph representation for specific nodes. The selector is divided into two
    parts - the node selection (id_selector) and graph modifier (mod). The id_selector is used to
    denote which nodes should be modified by this selector and follows the format of
    section:chain:rule (assuming wildcard when any of them are missing). The modifiers are any
    combination of modifying characters (%, ^, *, etc). Note that this class doesn't directly modify
    the graph but is used by the TreeMaker and Renderer to determine how to create/render the
    graph."""
    def __init__(self, id_selector: str, mod: str = ""):
        """
        Initializes a GraphSelector object.
        Args:
            id_selector (str): Selectors.
            mod (str, optional): Modifier characters. Defaults to "".
        """
        self._mod = mod or ""
        """Modifier characters"""
        self._id_components = (id_selector or "").strip().split(":")
        """Identifier name"""
        self._empty = not any(x for x in self._id_components if x)
        self._depth = len(self._id_components)
    def __repr__(self):
        selector = ":".join(x or "*" for x in self._id_components)
        return f"GraphSelector({selector}=>{self._mod})"
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GraphSelector):
            return NotImplemented
        return self._mod == other._mod and self._id_components == other._id_components
    @property
    def selectors(self):
        """Returns a list of the id components used as selectors."""
        return list(self._id_components)
    @property
    def depth(self):
        """Returns the selector depth (number of id components)."""
        return self._depth
    @property
    def empty(self):
        """Returns True if all id components are empty."""
        return self._empty
    @property
    def default(self):
        """Returns True if this is the default selector (::)."""
        return self.empty
    @property
    def splat(self):
        """Returns True if the selected nodes should be splatted."""
        return "*" in self._mod
    @property
    def show(self):
        """Returns True if the selected nodes should be shown."""
        return not self._mod or "+" in self._mod
    @property
    def remove(self):
        """Returns True if the selected nodes should be removed."""
        return "-" in self._mod
    @property
    def collapse(self):
        """Returns True if the selected nodes should be collapsed."""
        return "%" in self._mod
    @property
    def render(self):
        """Check if the element should be rendered based on the modifier character."""
        if self.remove:
            return False
        return self.show or self.splat or self.collapse
class Link:
    """Link between two graph nodes."""
    def __init__(
        self,
        start: LinkableTreeNode,
        end: LinkableTreeNode,
        style: str | None = None,
        label: str | None = None,
    ):
        """Constructor
        Args:
            start (Element): Starting node (tail end)
            end (Element): Ending node (arrow end)
            style (str, optional): Link style to use (if None it will be determined based on default
                rules). Defaults to None.
            label (str, optional): Link label (to use during rendering). Defaults to "".
        """
        self.start = start
        """Starting node (tail end)."""
        self.end = end
        """Ending node (arrow end)."""
        self.style = style
        """Link style to use (if None it will be determined based on default rules)."""
        self.label = label
        """Link label."""
        self.render = True
        """Whether the link should be rendered."""
        self.id = str(id(self))
        """Link identifier."""
    def __str__(self):
        return f"Link from {self.start} to {self.end}"
    def __repr__(self):
        s = f"Link from {self.start} to {self.end}"
        if not self.render:
            s += "[!render]"
        return s
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Link):
            return False
        return (
            self.start == other.start
            and self.end == other.end
            and self.style == other.style
            and self.label == other.label
        )
    def __hash__(self):
        return hash((self.start.id, self.end.id))
    def clone(self):
        """Clones link."""
        return Link(self.start, self.end, self.style, self.label)
class ParserRule:
    """Structure to hold rule information after being parsed by the parser"""
    def __init__(self, line: str, attributes: dict[str, str]):
        """Constructor
        Args:
            line (str): Parser line (rule line)
            attributes (dict[str, str]): Parsed attributes
        """
        self.line = line
        """Raw line"""
        self.attributes = attributes
        """Rule attributes"""
    @property
    def section(self) -> str:
        """Section name (determined from raw line)
        Returns:
            str:
        """
        return self.line.split()[2]
    @property
    def chain(self) -> str:
        """Chain name as determine from parsed attributes
        Returns:
            str:
        """
        return self.attributes["chain"]
    def __repr__(self) -> str:
        attrs = [f"{k}={v}" for k, v in self.attributes.items() if k != "chain"]
        return f"Rule section={self.section} chain={self.chain} {' '.join(attrs)}"
class TreeNode:
    """Base tree node. All tree elements (Section, Chain, Rule) inherit from this class."""
    def __init__(self, parent: TreeNode | None = None):
        self.parent: TreeNode | None = parent
        """Parent node"""
    @property
    def id(self) -> str:
        """Node identifier"""
        return "unidentified tree node"
    @property
    def tree_root(self) -> RootNode:
        """Root tree node
        Returns:
            Root:
        """
        if isinstance(self, RootNode):
            return self
        if self.parent is None:
            raise ValueError("Parent is null")
        return self.parent.tree_root
    def get_parents(self) -> list[TreeNode]:
        """Get all parent nodes
        Returns:
            list[TreeNode]: List of parent nodes
        """
        parents = []
        node = self
        while node.parent:
            parents.append(node.parent)
            node = node.parent
        return parents
    @property
    def parents(self) -> list[TreeNode]:
        """
        Returns a list of parent nodes for the current node.
        Returns:
            A list of TreeNode objects representing the parent nodes.
        """
        return self.get_parents()
class LinkableTreeNode(TreeNode):
    """Base class for tree nodes that can have links (i.e. Section, Chain, Rule)."""
    def __init__(self, parent: TreeNode):
        super().__init__(parent)
        self.links: list[Link] = []
        """Node links"""
    def add_link(self, to: LinkableTreeNode, style: str | None = None, label: str | None = None):
        """Add link to tree.
        Args:
            link (Link): Link to add
        """
        if not self.tree_root.has_tree_element(to):
            raise ElementNotFound(f"Tree does not contain end node {to} of link")
        self.links.append(Link(self, to, style, label))
    def add_existing_link(self, link: Link):
        """Add (an existing) link to tree replacing the start with this rule.
        Args:
            link (Link): Link to add
        """
        if not self.tree_root.has_tree_element(link.end):
            raise ElementNotFound(f"Tree does not contain end node {link.end} of link")
        if link in link.start.links:
            link.start.remove_link(link)
        link.start = self
        self.links.append(link)
    def remove_link(self, link: Link):
        """Remove existing link
        Args:
            link (Link): Link to add
        """
        self.links.remove(link)
    def remove_links_to(self, to: LinkableTreeNode):
        """Remove all existing links to given end node
        Args:
            to (LinkableNode): End node
        """
        links = [l for l in self.links if l.end == to]
        for link in links:
            self.links.remove(link)
    def clone_links(self, new_start: LinkableTreeNode | None = None):
        """Clone links and replace start with given node.
        Args:
            new_start (LinkableTreeNode | None, optional): New start node or None to use
                current/self. Defaults to None.
        Returns:
            list[Link]: Cloned links
        """
        links = [l.clone() for l in self.links]
        for l in links:
            l.start = new_start or self
        return links
@total_ordering
class Rule(LinkableTreeNode):
    """Element representing a firewall rule. When a rule is parsed each of its attributes (i.e.
    action, jump-target) will be added as property (replacing - with _) and can be accessed plainly
    as `rule.action` or `rule.jump_target`.
    """
    def __init__(self, line: str, index: int, attributes: Mapping[str, Any | None]):
        """Constructor
        Args:
            line (str): full firewall rule e.g. `/ip firewall filter ....`
            index (int): rule index (usually line number)
            attributes (dist[str, Any|None]) : Parsed attributes
        """
        super().__init__(Chain(DETACHED))
        self.parent: Chain
        """Parent chain"""
        self.parent.add_rule(self)
        self.known_attributes: list[str] = list(attributes.keys())
        """List of know/parsed attributes"""
        self.loggable = True
        """Whether rule is loggable to the rule log"""
        self.index = index
        """Rule index (based on parsed file)"""
        self.raw_line = line.strip()
        """The rule line as written in the input file"""
        for key in attributes:
            self.__dict__[key] = attributes[key]
    @property
    def id(self) -> str:
        """Rule identifier
        Returns:
            str:
        """
        return f"{self.parent.id}:rule{self.index}"
    @property
    def chain(self) -> str:
        """Rule chain name. This is a short hand for writing self.parent.name.
        Returns:
            str: Rule chain name
        """
        return self.parent.name
    @property
    def is_terminal_rule(self) -> bool:
        """Whether the rule is flow ending (that is no more processing after it). Note this applies
        to the rule only and not the whole flow and it mostly relies on the rule action and whether
        rule has matchers.
        Returns:
            bool: True if packet flow stops/terminates at the rule.
        """
        return self.action in ["drop", "accept", "reject", "tarpit"] and not self.has_rule_matchers
    @property
    def has_rule_matchers(self) -> bool:
        """Whether rule has matchers properties (any property other than action, comment, chain,
        log_prefix, log, jump_target)
        Returns:
            bool:
        """
        return (
            set(self.known_attributes).difference(
                {"action", "comment", "chain", "log_prefix", "log", "jump_target"}
            )
            != set()
        )
    @property
    def line(self) -> str:
        """Raw line text"""
        return self.raw_line
    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            return None
    def next_rule(self) -> Rule | None:
        """Return the next rule (by index) in the chain. This is a shortcut for
        parent.next_rule(self).
        Returns:
            Rule|None: Next rule in the chain or None.
        """
        return self.parent.next_rule(self)
    def detach(self) -> Rule:
        """Remove rule from parent chain. Note does not remove links to rule."""
        self.parent.remove_rule(self)
        return self
    def __gt__(self, other):
        if not isinstance(other, Rule):
            raise TypeError(f"Unsupported operation for type {type(other)}")
        return self.index > other.index
    def __str__(self):
        return f"Rule {self.index}"
    def __eq__(self, other):
        if not isinstance(other, Rule):
            return False
        if id(self) == id(other):
            return True
        if (
            self.index != other.index
            or self.loggable != other.loggable
            or self.known_attributes != other.known_attributes
        ):
            return False
        for attribute in self.known_attributes:
            if self.__getattribute__(attribute) != other.__getattribute__(attribute):
                return False
        return True
    def __repr__(self):
        return f"Rule {self.index} in {self.chain}"
    def jump_target_chain(self) -> Chain | None:
        """Return the chain node this rule jumps to. If rule isn't a jump rule, then None will be
        returned.
        Returns:
            Chain | None: Jump chain
        """
        return self.parent.parent.chain(self.jump_target) if self.jump_target else None
    def clone(self) -> Rule:
        """Copy/clone rule. Note that the copied rule's index and raw line will be the same as this
        rule.
        Returns:
            Rule: Rule clone
        """
        attr = {x: getattr(self, x) for x in self.known_attributes}
        r = Rule(self.raw_line, self.index, attr)
        r.loggable = r.loggable
        r.links = self.clone_links(r)
        return r
class Chain(LinkableTreeNode):
    """Element representing a firewall chain. Rule can be accessed by subscript with the rule id -
    e.g. chain["rule1"]."""
    def __init__(self, name: str):
        """Constructor
        Args:
            name (str): Chain name
        """
        self.name = name
        """Chain name."""
        super().__init__(Section(DETACHED))
        self.parent: Section
        """Section chain belong to."""
        self.parent.add_chain(self)
        self.rules: list[Rule] = []
        """Dictionary of rules found in this chain (key = rule id)"""
        self.render = True
        """Whether the chain should be rendered"""
    @property
    def id(self) -> str:
        """Chain identifier
        Returns:
            str:
        """
        return f"{self.parent.id}:{self.name}"
    def _sort_rules(self):
        if self.rules:
            self.rules.sort(key=lambda x: x.index)
    def first_rule(self) -> Rule | None:
        """Return the first rule in the chain.
        Returns:
            Rule: Rule or None
        """
        self._sort_rules()
        return self.rules[0] if self.rules else None
    def last_rule(self) -> Rule | None:
        """Return the last rule in the chain.
        Returns:
            Rule: Rule or None
        """
        self._sort_rules()
        return self.rules[-1] if self.rules else None
    def next_rule(self, rule: Rule) -> Rule | None:
        """Return the next rule in the chain for given rule (if part of the chain). Otherwise
        returns None.
        Args:
            rule (Rule): Chain rule
        Returns:
            Rule | None: Next rule in the chain or None
        """
        self._sort_rules()
        try:
            index = [x.index for x in self.rules].index(rule.index)
            index += 1
            return self.rules[index] if index < len(self.rules) else None
        except ValueError:
            return None
    def add_rule(self, rule: Rule):
        """Add rule to chains. Note it will not add rule links to the parent.
        Args:
            rule (Rule): Rule to be added.
        """
        # find existing rule by index
        existing_rule = next(iter(x for x in self.rules if x.index == rule.index), None)
        if existing_rule:
            logging.warning("Attempted to add rule with rule index already chain %s", rule)
            return None
        self.rules.append(rule)
        rule.parent = self
        return rule
    def remove_rule(self, rule: Rule) -> Rule | None:
        """Remove given rule from chain. Removed rule will be re-attached to a new empty
        root/section/chain.
        Args:
            rule (Rule): Rule to remove.
        Returns:
            Rule | None: Removed rule or None if rule isn't part of the chain's rules.
        """
        if rule in self.rules:
            self.rules.remove(rule)
            Chain(DETACHED).add_rule(rule)
            return rule
        logging.warning("Asked to remove non-existing rule %s", rule)
        return None
    def detach(self):
        """Remove self from parent section."""
        self.parent.remove_chain(self)
    def __str__(self):
        return f"Chain {self.name}"
    def __repr__(self):
        s = f"Chain {self.name} in {self.parent.name}"
        if not self.render:
            s += "[!render]"
        return s
    def __eq__(self, other):
        if not isinstance(other, Chain):
            return False
        if id(self) == id(other):
            return True
        if self.name != other.name:
            return False
        if self.render != other.render:
            return False
        if self.rules != other.rules:
            return False
        return True
    def clone(self) -> Chain:
        """Clone self.
        Returns:
            Chain: Clone of self.
        """
        c = Chain(self.name)
        c.render = self.render
        for r in self.rules:
            c.add_rule(r.clone())
        c.links = self.clone_links(c)
        return c
class Section(LinkableTreeNode):
    """Element representing a firewall section. Chains can be accessed by subscript with the chain
    name - e.g. section["input"].
    """
    def __init__(self, name: str):
        """Constructor
        Args:
            name: Section name
        """
        self.name: str = name
        """Section name - just the id"""
        super().__init__(RootNode())
        self.parent: RootNode
        """Section identifier"""
        self.parent.add_section(self)
        self.chains: list[Chain] = []
        """Child chain elements."""
        self.render = True
        """Whether the section should be rendered"""
    @property
    def id(self) -> str:
        """Section identifier.
        Returns:
            str:
        """
        return self.name
    def get_or_add_chain(self, name: str) -> Chain:
        """Get or add chain by name.
        Args:
            name (str): Chain name.
        Returns:
            Chain
        """
        chain = self.chain(name)
        if not chain:
            logging.debug("Adding chain %s to %s", name, self.parent)
            return self.add_chain(name)
        return chain
    def chain(self, name: str) -> Chain | None:
        """Get chain by name.
        Args:
            name (str): Chain name
        Returns:
            Chain|None: Found chain or None if chain isn't found.
        """
        chain = [c for c in self.chains if c.name == name]
        return chain[0] if chain else None
    def has_chain(self, name: str) -> bool:
        """Checks if given chain exists in tree.
        Args:
            name (str): Chain name.
        Returns:
            bool
        """
        if [c for c in self.chains if c.name == name]:
            return True
        return False
    def add_chain(self, chain: Chain | str) -> Chain:
        """Add chain to section. If chain is given as string, then a new chain will be created.
        Args:
            chain (Chain | str): Chain to add or chain name to create.
        Returns:
            Chain: Added chain. Raises ChainAlreadyExistsError if chain with given name already
                exists.
        """
        name = chain if isinstance(chain, str) else chain.name
        if self.has_chain(name):
            raise ChainAlreadyExistsError(name, self.parent)
        c = Chain(chain) if isinstance(chain, str) else chain
        c.parent = self
        self.chains.append(c)
        return c
    def remove_chain(self, chain: Chain) -> Chain | None:
        """Remove given chain from section. Removed chain will be attached to a new default parent.
        Args:
            chain (Chain): Chain
        Returns:
            Chain | None: Removed chain, or None if chain not found in section.
        """
        if chain not in self.chains:
            logging.warning("Asked to remove non-existing chain %s", chain)
            return None
        self.chains.remove(chain)
        Section(DETACHED).add_chain(chain)
        return chain
    def next_section(self) -> Section | None:
        """Return next section in tree.
        Returns:
            Section: Next section or None if none found
        """
        return self.parent.next_section(self)
    def detach(self):
        """Detach self from tree parent."""
        self.parent.remove_section(self)
    def __str__(self):
        return f"Section {self.name}"
    def __repr__(self):
        s = f"Section {self.name}"
        if not self.render:
            s += "[!render]"
        return s
    def clone(self) -> Section:
        """Clone self.
        Returns:
            Section: Clone section.
        """
        s = Section(self.name)
        s.render = self.render
        for c in self.chains:
            s.add_chain(c.clone())
        s.links = self.clone_links(s)
        return s
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Section):
            return False
        if id(self) == id(other):
            return True
        if self.name != other.name:
            return False
        if self.render != other.render:
            return False
        if self.chains != other.chains:
            return False
        return True
class RootNode(TreeNode):
    """Represents the top of the tree structure"""
    def __init__(self):
        super().__init__()
        self.sections: list[Section] = []
        """List of child section elements"""
    def has_section(self, name: str) -> bool:
        """Checks if given section exists in tree.
        Args:
            name (str): Section name.
        Returns:
            bool
        """
        return bool([x for x in self.sections if x.name == name])
    def section(self, name: str) -> Section | None:
        """Get section by name.
        Args:
            name (str): Section name.
        Returns:
            Section|None: Found section or None if no section is found.
        """
        section = [x for x in self.sections if x.name == name]
        if not section:
            return None
        return section[0]
    def get_or_add_section(self, name: str) -> Section:
        """Get or create section
        Args:
            name (str): Section name
        """
        section = self.section(name)
        if not section:
            logging.debug("Adding section %s to tree", name)
            return self.add_section(name)
        return section
    def has_tree_element(self, element: TreeNode) -> bool:
        """
        Checks if the given element exists in the tree.
        Args:
            element (TreeNode): The element to check.
        Returns:
            bool: True if the element exists in the tree, False otherwise.
        """
        if isinstance(element, Section):
            return element in self.sections
        if isinstance(element, Chain):
            return element in self.chains
        return element in self.rules
    @property
    def chains(self) -> list[Chain]:
        """List all chains in tree"""
        return [c for s in self.sections for c in s.chains]
    @property
    def rules(self) -> list[Rule]:
        """List all rules in subelements.
        Returns:
            list[Rule]:
        """ """"""
        return [r for c in self.chains for r in c.rules]
    def next_section(self, section: Section) -> Section | None:
        """Return the next section based on packet flow order in the tree.
        Args:
            section (Section): Current section.
        Returns:
            Section | None: Next section or None if section is not part of this tree or there is the
            last section.
        """
        from firewall2mermaid.common import section_sort_key
        if section not in self.sections:
            return None
        self.sections.sort(key=lambda x: section_sort_key(x.name.lower()))
        index = self.sections.index(section)
        index += 1
        return self.sections[index] if index < len(self.sections) else None
    def first_section(self) -> Section | None:
        """Return the first section based on packet flow order in this tree.
        Returns:
            Section | None: First section or None
        """
        from firewall2mermaid.common import section_sort_key
        if not self.sections:
            return None
        return min(self.sections, key=lambda x: section_sort_key(x.name.lower()))
    def add_section(self, section: Section | str) -> Section:
        """Add section to tree. If section is given as string, then a new section will be created.
        Args:
            section (Section | str): section to add or section name to create.
        Returns:
            Section: Added section. Raises SectionAlreadyExistsError if the section by same name
                already exists.
        """
        name = section if isinstance(section, str) else section.name
        if self.has_section(name):
            raise SectionAlreadyExistsError(name)
        s = Section(section) if isinstance(section, str) else section
        s.parent = self
        self.sections.append(s)
        return s
    def remove_section(self, section: Section) -> Section | None:
        """Remove section from tree.
        Args:
            section (Section): Section to remove.
        Returns:
            Section | None: Removed section or None if no section has been removed.
        """
        if section not in self.sections:
            logging.warning("Asked to remove non-existing section %s", section)
            return None
        self.sections.remove(section)
        RootNode().add_section(section)
        return section
    def next_rule_index(self) -> int:
        """Get the next available rule index.
        Returns:
            int: Next available rule index.
        """
        return max((x.index for x in self.rules), default=-1) + 1
    def clone(self) -> RootNode:
        """Clone tree.
        Returns:
            RootNode: Cloned root.
        """
        r = RootNode()
        for s in self.sections:
            r.add_section(s.clone())
        return r
    def __eq__(self, other):
        if not isinstance(other, RootNode):
            return False
        if id(self) == id(other):
            return True
        if self.sections != other.sections:
            return False
        return True
class PacketFlowIterator:
    """Iterator for PacketFlowElement."""
    def __init__(self, flow: PacketFlowElement):
        """Constructor.
        Args:
            flow (PacketFlowElement): Flow element to iterate over.
        """
        self.head: PacketFlowElement | None = flow
        self.reversed = reversed
    def __iter__(self):
        return self
    def __next__(self) -> PacketFlowElement:
        if not self.head:
            raise StopIteration
        element = self.head
        self.head = self.head.next
        return element
class PacketFlowElement:
    """Packet flow element/leaf"""
    def __init__(self, section: str, chain: str):
        """Constructor.
        Args:
            section (str): Section name.
            chain (str): Chain name
        """
        self.section = section
        """Section name"""
        self.chain = chain
        """Chain Name"""
        self.next: PacketFlowElement | None = None
        """Next flow element (downstream)"""
    def __iter__(self):
        return PacketFlowIterator(self)
    def __reversed__(self):
        nodes: list[PacketFlowElement] = [self]
        node = self
        while node.next:
            node = node.next
            nodes.append(node)
        nodes = [PacketFlowElement(x.section, x.chain) for x in nodes]
        nodes.reverse()
        for i in range(0, len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return PacketFlowIterator(nodes[0])
    def last_node(self) -> PacketFlowElement:
        """Get the last node in the flow.
        Returns:
            PacketFlowElement: _description_
        """
        return self.next.last_node() if self.next else self
================================================

File: parser.py
================================================
"""Microtik File parser."""
import logging
import re
from firewall2mermaid.common import FIREWALL_LINE_START
from firewall2mermaid.model import ParserRule
def __is_firewall_rule_line(line: str) -> bool:
    """Determine if line is a firewall rule
    Args:
        line (str): Raw line string
    Returns:
        bool: True if line is a firewall rule that we can parse
    """
    return line.startswith(
        (
            f"{FIREWALL_LINE_START} filter",
            f"{FIREWALL_LINE_START} nat",
            f"{FIREWALL_LINE_START} raw",
        )
    )
def parse_rules(file_path: str) -> list[ParserRule]:
    """Parse input file and generate list of applicable rules
    Args:
        file_path (str): Input file path
    Returns:
        list[ParserRule]: List of parsed rules. Note that in all rules the parent (chain) is set to
            None.
    """
    logging.info("Parsing rules from %s", file_path)
    rules: list[ParserRule] = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if __is_firewall_rule_line(line):
                logging.debug("Found firewall rule line: %s", line)
                rules.append(parse_rule(line))
    logging.debug("Parsed total %d rules", len(rules))
    return rules
def parse_rule(line: str) -> ParserRule:
    """Parse rule from given rule line
    Args:
        line (str): Firewall rule line as appearing in dump
    Returns:
        ParserRule: Parsed rule
    """
    return ParserRule(line.strip(), attributes=parse_rule_attributes(line))
def parse_rule_attributes(line: str) -> dict[str, str]:
    """Parse rule attributes for given full line.
    Args:
        line (str): Raw file line.
    Returns:
        dict[str, str]: Parsed attributes
    """
    attributes: dict[str, str] = {}
    tokens = re.split(r'\s+(?=(?:(?:[^"]*"){2})*[^"]*$)', line)
    for token in tokens:
        if "=" in token:
            attr, value = token.split("=")
            attr = attr.replace("-", "_")
            value = value.replace('"', "")
            attributes[attr] = value
    attrs = [f"{k}={v}" for k, v in attributes.items()]
    logging.debug("Parsed rule attributes: %s", " ".join(attrs))
    # case rule is added with no action (defaults to accept)
    if "action" not in attributes:
        logging.debug("No action parsed - assigning 'accept' as default")
        attributes["action"] = "accept"
    return attributes
================================================

File: common.py
================================================
"""Common rendering functions."""
import logging
from firewall2mermaid.common import (
    CLASS_DEF,
    LINK_STYLE_BETWEEN_SECTIONS,
    LINK_STYLE_NORMAL,
    LINK_STYLE_NORMAL_LONGER,
    find_jump_target_rule,
)
from firewall2mermaid.model import Chain, Link, Rule, Section
def hash_node(node) -> str:
    """Hash a node to a string.
    Args:
        node (Node): Node
    Returns:
        str: Hashed node
    """
    if isinstance(node, (Section, Chain, Rule)):
        return str(id(node)) if hasattr(node, "name") and node.name == "detached" else node.id
    return "unknown node type"
def is_link_between_sections(link: Link) -> bool:
    """Check if the link is between sections (chains, sections).
    Args:
        link (Link): Link
    Returns:
        bool: True if the link is between sections, False otherwise.
    """
    end_hierarchy = [
        hash_node(node)
        for node in [link.end, *link.end.get_parents()]
        if isinstance(node, (Section, Chain, Rule))
    ]
    return {hash_node(x) for x in [link.start, *link.start.get_parents()]}.intersection(
        end_hierarchy
    ) == set()
def get_link_style(link: Link) -> str:
    """Generate link mermaid code.
    Args:
        link (Link): Link
    Returns:
        str: Mermaid text for given link
    """
    if link.style:
        return link.style
    if is_link_between_sections(link):
        return LINK_STYLE_BETWEEN_SECTIONS
    link_style = LINK_STYLE_NORMAL
    if isinstance(link.start, Rule):
        is_jump_with_matchers = link.start.action == "jump" and link.start.has_rule_matchers
        is_multiple_links = len(link.start.links) > 1
        if is_jump_with_matchers:
            # elongate the otherwise in jump
            is_same_jump_target = find_jump_target_rule(link.start) == link.end
            link_style = LINK_STYLE_NORMAL_LONGER if not is_same_jump_target else LINK_STYLE_NORMAL
        elif is_multiple_links:
            is_same_parent = link.start.parent == link.end.parent
            link_style = LINK_STYLE_NORMAL_LONGER if not is_same_parent else LINK_STYLE_NORMAL
    return link_style
def determine_rule_style(rule: Rule) -> str | None:
    """Determine the graph style to use for given rule.
    Args:
        rule (Rule): Rule
    Returns:
        str | None: Node style or None if no style can be determined
    """
    if rule.disabled == "yes":
        logging.debug("Rule '%s' is disabled", rule)
        return "disabled"
    return rule.action if rule.action in CLASS_DEF else None
def determine_rule_action_sublabel(rule: Rule) -> str:
    """Create label part from rule action parameters.
    Args:
        rule (Rule): Rule
    Returns:
        str: label part
    """
    if rule.action in ["log", "drop", "accept", "return"]:
        return f"{rule.action}"
    if rule.action == "jump":
        return f"jump to {rule.jump_target}"
    if rule.action in ["add-src-to-address-list", "add-dst-to-address-list"]:
        label = f"add ip to '{rule.address_list}'"
        if rule.address_list_timeout:
            label += f" for {rule.address_list_timeout}"
        return label
    return ""
def determine_rule_connection_sublabel(rule: Rule) -> str:
    """Create label part from rule connection parameters.
    Args:
        rule (Rule): Rule
    Returns:
        str: Label part
    """
    return f"connection is {rule.connection_state}" if rule.connection_state else ""
def determine_rule_packet_sublabel(rule: Rule) -> str:
    """Create label part from rule packet parameters
    Args:
        rule (Rule): Rule
    Returns:
        str: Label part
    """
    label = ""
    attrs = []
    if rule.protocol:
        attrs.append(rule.protocol)
    if rule.tcp_flags:
        attrs.append(rule.tcp_flags)
    if rule.dst_limit:
        attrs.append(f"below {rule.dst_limit}")
    if attrs:
        label = f"is {','.join(attrs)}"
    return label
def determine_rule_src_sublabel(rule: Rule) -> str:
    """Create label part from rule source parameters.
    Args:
        rule (Rule): Rule
    Returns:
        str: label part
    """
    label = ""
    if (
        rule.src_address_list
        or rule.src_address
        or rule.src_address_type
        or rule.port
        or rule.src_port
        or rule.in_interface
        or rule.in_bridge_port
    ):
        if rule.src_address_list:
            label = rule.src_address_list
        elif rule.src_address:
            label = rule.src_address
        elif rule.src_address_type:
            label = rule.src_address_type
        else:
            label = "any"
        if rule.src_port or rule.port:
            label += f":{rule.src_port}" if rule.src_port else f":*{rule.port}"
    # on
    if rule.in_interface or rule.in_bridge_port:
        label += " on "
        if rule.in_interface:
            label += rule.in_interface
        if rule.in_bridge_port:
            label += f":{rule.in_bridge_port}"
    return "src is " + label if label else ""
def determine_rule_dst_sublabel(rule: Rule) -> str:
    """Create label part from rule destination parameters.
    Args:
        rule (Rule): Rule
    Returns:
        str: label part
    """
    label = ""
    # to
    if (
        rule.dst_address_list
        or rule.dst_address
        or rule.dst_address_type
        or rule.port
        or rule.dst_port
        or rule.out_interface
        or rule.out_bridge_port
    ):
        if rule.dst_address_list:
            label = rule.dst_address_list
        elif rule.dst_address:
            label = rule.dst_address
        elif rule.dst_address_type:
            label = rule.dst_address_type
        else:
            label = "any"
        if rule.dst_port or rule.port:
            label += f":{rule.dst_port}" if rule.dst_port else f":*{rule.port}"
    # on
    if rule.out_interface or rule.out_bridge_port:
        label += " on "
        if rule.out_interface:
            label += rule.out_interface
        if rule.out_bridge_port:
            label += f":{rule.out_bridge_port}"
    return f"dst is {label}" if label else ""
def determine_rule_label(rule: Rule, comment_handling="auto") -> str:
    """Create rule node label.
    Args:
        rule (Rule): Rule
        comment_handling (str, optional): Whether to use shortened labels. Defaults to auto.
            Can be one of:
                - show: Always shows comments in node labels
                - hide: Never shows comments in node labels
                - auto: Shows comments only when no other label can be generated
                - prefer: Shows comments in node label instead of generated label, if aviable
    Returns:
        str: Label
    """
    logging.debug("Creating label for rule '%s' with mode '%s'", rule, comment_handling)
    if comment_handling == "prefer" and rule.comment:
        # quote the label
        if any(char in rule.comment for char in ["(", ")", "{", "}", "[", "]"]):
            return f'"{rule.comment}"'
        logging.debug("Preferring comment as label '%s'", rule.comment)
        return rule.comment
    label: str = ""
    # label parts
    action_label = determine_rule_action_sublabel(rule)
    packet_label = determine_rule_packet_sublabel(rule)
    src_label = determine_rule_src_sublabel(rule)
    dst_label = determine_rule_dst_sublabel(rule)
    connection_label = determine_rule_connection_sublabel(rule)
    if packet_label or src_label or dst_label or connection_label:
        label_parts = []
        if packet_label:
            label_parts.append(packet_label)
        if connection_label:
            label_parts.append(connection_label)
        if src_label:
            label_parts.append(src_label)
        if dst_label:
            label_parts.append(dst_label)
        label = ", ".join(label_parts)
        logging.debug("Found the following label parts: %s", ", ".join(label_parts))
    # add comment part - if show or auto + nothing generated
    add_comment = comment_handling == "show" or (comment_handling == "auto" and not label)
    if add_comment and rule.comment:
        logging.debug("Adding rule comment: %s", rule.comment)
        label = f"{label} *{rule.comment}" if label else rule.comment
    # fall back when no label can be generated and no comment exists
    if not label:
        label = action_label if action_label else rule.id
        logging.debug("No label generated, falling back to label/rule id")
    # add question mark when links are more than one (a jump most likely)
    if len(rule.links) > 1 and rule.has_rule_matchers:
        logging.debug("Rule splits path")
        label += "?"
    # add notes if logging to someplace
    if rule.log == "yes":
        logging.debug("Rule is logged, adding log part %s", rule.log_prefix)
        label += f" !>{{{rule.log_prefix}}}"
    # quote the label
    if any(char in label for char in ["(", ")", "{", "}", "[", "]"]):
        return f'"{label}"'
    return label
def determine_link_label(link: Link) -> str:
    """Generate label for given link. If link has label (not None) it will return that label.
    Otherwise it will generate a label based on the linking nodes.
    Args:
        link (Link): Link
    Returns:
        str: Formatted link label - e.g. |some text here| or empty string when link is chained or
            link has empty "" as label.
    """
    if link.label is not None:
        logging.debug("Using link label '%s' from '%s'", link.label, link)
        return link.label
    if is_link_between_sections(link):
        # find the right name for the section
        if isinstance(link.end, Rule):
            return f"to {link.end.parent.parent.name}:{link.end.parent.name}"
        if isinstance(link.end, Chain):
            return f"to {link.end.parent.name}:{link.end.name}"
        if isinstance(link.end, Section):
            return f"to {link.end.name}"
        return "to unknown parent"
    return ""
================================================

File: model.py
================================================
"""Render model classes used by Renderer to construct and render the graph from the AST."""
from __future__ import annotations
import logging
from typing import Callable, Generator, Type, TypeVar
import uuid
from firewall2mermaid.common import LINK_STYLE_INVISIBLE, TAB_CHARACTER
from firewall2mermaid.model import Link
from firewall2mermaid.render.common import get_link_style, determine_link_label
NodeT = TypeVar("NodeT")
class Node:
    """Node in the graph."""
    def __init__(self, node_id: str | int | None = None, direction="TB", parent=None):
        if not node_id:
            self.id = uuid.uuid4().hex
        elif isinstance(node_id, int):
            self.id = str(node_id)
        else:
            self.id = node_id
        self.direction = direction
        self.parent: Node | None = parent
        self.children: list[Node] = []
    def format_graph_line(self, line: str, level=0, line_ending: bool | str = False):
        """Line render helper (for tabulation and formatting).
        Args:
            line (str): Graph line to render
            level (int, optional): Indentation level. Defaults to 0.
            line_ending (int|str, optional): Whether to add line ending to the line. If True or any
                string value then it will append the given line ending (\n for True)
        Returns:
            str: Formatted line
        """
        ending = ""
        if line_ending:
            if isinstance(line_ending, bool):
                ending = "\n"
            else:
                ending = line_ending
        return f"{TAB_CHARACTER*level}{line}{ending}"
    def normalize_render_text(self, text: str, level: int):
        """
        Normalize the render text by formatting it and adding the appropriate level of indentation.
        Args:
            text (str): The render text to be normalized.
            level (int): The indentation level.
        Returns:
            str: The normalized render text.
        """
        if not text:
            return text
        return "\n".join(
            [
                self.format_graph_line(x.strip(), level, True)
                for x in self.render_start(level).split("\n")
            ]
        )
    def join_render_lines(self, first: str, second: str):
        """
        Joins two lines together, ensuring that there is a newline character between them if
            necessary.
        Args:
            first (str): The first line.
            second (str): The second line.
        Returns:
            str: The joined lines.
        """
        if not first:
            return second
        if not second:
            return first
        return f"{first}{second}" if first.endswith("\n") else f"{first}\n{second}"
    def render(self, level: int = 0) -> str:
        """Renders the node as graph text.
        Returns:
            str: Graph text
        """
        logging.debug("Rendering node %s: %s", self.id, self)
        text = self.render_start(level)
        for child in self.children:
            child_text = child.render(level + 1)
            text = self.join_render_lines(text, child_text)
        text = self.join_render_lines(text, self.render_end(level))
        return text
    def render_start(self, _):
        """
        Called during the start of the node rendering method, before calling render on node's
        children. Subclasses should override this to supply the actual rendered text of the node.
        Parameters:
        - level (int): Indentation
        Returns:
            - Node rendered text
        """
        return ""
    def render_end(self, _):
        """
        Called after rendering the child nodes, for any additional node text that needs to be
        render. Subclasses should override this to supply the actual rendered text of the node.
        Parameters:
        - level (int): Indentation
        Returns:
            - Node render text
        """
        return ""
    def add_child(self, node):
        """Adds child node.
        Args:
            node: Node to add as a child
        Return:
            self
        """
        self.children.append(node)
        node.parent = self
        return self
    def insert_child(self, index: int, node):
        """Adds child node to given index (same use as list.insert)
        Args:
            index: Index to insert the node at
            node: Node to add as a child
        Return:
            self
        """
        self.children.insert(index, node)
        node.parent = self
        return self
    def child_index(self, node_id: str | int):
        """Returns the index of the child with the given id."""
        for index, child in enumerate(self.children):
            if child.id == node_id:
                return index
        return None
    def find_node_by_id(self, node_id: str | int, recurse=False):
        """Find node by given id by searching the current node and its direct children.
        Args:
            id (str | int): Node identifier
            recurse (bool, optional): If recurse then it will also search through all children.
                Defaults to False.
        Returns:
            Node|None: None if not found otherwise the found node.
        """
        node_id = str(node_id)
        return self.find_node(lambda node: node.id == node_id, recurse=recurse)
    def find_node(self, callback: Callable[[Node], bool], recurse=False):
        """Find node by given id by searching the current node and its direct children.
        Args:
            id (str | int): Node identifier
            recurse (bool, optional): If recurse then it will also search through all children.
                Defaults to False.
        Returns:
            Node|None: None if not found otherwise the found node.
        """
        if callback(self):
            return self
        for child in self.children:
            if callback(child):
                return child
            if recurse:
                node = child.find_node(callback, recurse)
                if node:
                    return node
        return None
    def next_sibling(self, node_id: str | int):
        """Find next sibling in the direct children of this node by given id.
        Args:
            id (str|int): Node identifier
            recurse (bool, optional): If recurse then it will also search through all children.
                Defaults to False.
        Returns:
            Node|None: None if not found otherwise the found node.
        """
        node_id = str(node_id)
        found = False
        for node in self.children:
            if found:
                return node
            if node.id == node_id:
                found = True
        return None
    def previous_sibling(self, node_id: str | int):
        """Find previous sibling in the direct children of this node by given id.
        Args:
            id (str|int): Node identifier
            recurse (bool, optional): If recurse then it will also search through all children.
                Defaults to False.
        Returns:
            Node|None: None if not found otherwise the found node.
        """
        node_id = str(node_id)
        previous_node = None
        for node in self.children:
            if node.id == node_id:
                return previous_node
            previous_node = node
        return None
    def walk_tree(self):
        """Walk the tree and yield nodes."""
        yield self
        for child in self.children:
            yield from child.walk_tree()
    def walk_nodes(self, node_type: Type[NodeT]) -> Generator[NodeT, None, None]:
        """Walk the tree and yield nodes of specific type."""
        if isinstance(self, node_type):
            yield self
        for child in self.children:
            yield from child.walk_nodes(node_type)
    def remove_child(self, node_id: str | int):
        """Removes a child from the node.Args:
            id (str|int): Node identifier
        Returns:
            Node|None: None if not found otherwise the remoevd node."""
        node_id = str(node_id)
        for child in self.children:
            if child.id == node_id:
                self.children.remove(child)
                return child
        return None
class GraphRootNode(Node):
    """Root node of the graph."""
    def __init__(self, graph_direction: str = "TB"):
        super().__init__("graphroot")
        self.direction = graph_direction
    def render(self, level: int = 0) -> str:
        """Renders the node as graph text."""
        return super().render(-1)
    def __repr__(self) -> str:
        return "GraphRoot"
class LiteralNode(Node):
    """A literal text node. Node doesn't have children."""
    def __init__(self, text=""):
        super().__init__()
        self.text = text
    def render(self, level=0) -> str:
        return self.format_graph_line(self.text, level, True)
    def __repr__(self) -> str:
        return f"Literal: {self.text}"
class CommentNode(Node):
    """A comment node"""
    def __init__(self, comment: str):
        super().__init__("")
        self.text = comment
    def render(self, level=0) -> str:
        return self.format_graph_line(f"%% {self.text}", 0, True)
    def __repr__(self) -> str:
        return f"Comment: {self.text}"
class RuleNode(Node):
    """A mock rule node withought needint a rule"""
    def __init__(self, rule_id: str, label: str, style: str | None = None):
        super().__init__(rule_id)
        self.label = label
        self.style = style
    def render_start(self, level: int):
        text = self.id
        if self.label:
            text += f"[{self.label}]"
        if self.style:
            text += f":::{self.style}"
        return self.format_graph_line(text, level)
    def __repr__(self) -> str:
        return f"Rule: {self.id}"
class SubgraphNode(Node):
    """Subgraph node - chain or section."""
    def __init__(
        self,
        direction: str,
        node_id: str,
        name: str | None = None,
        render_direction: bool = True,
    ):
        super().__init__(node_id)
        self.name = name
        self.direction = direction
        self.render_direction = render_direction
    def render_start(self, level):
        tagline = f"subgraph {self.id}"
        if self.name:
            tagline += f" [{self.name}]"
        text = self.format_graph_line(tagline, level, True)
        if self.render_direction:
            text += self.format_graph_line(f"direction {self.direction}", level + 1, True)
        return text
    def render_end(self, level):
        return self.format_graph_line("end", level, True)
    def __repr__(self) -> str:
        return f"Subgraph: {self.id}"
class LinkNode(Node):
    """
    Represents a link in the graph.
    Attributes:
        id (str): The unique identifier of the node.
        link (Link): Original link.
        label (str): The label of the link.
        start_id (str): Effective start node id.
        end_id (str): Effective end node id.
    """
    def __init__(
        self,
        link: Link,
        label: str | None = None,
        start_id: str | None = None,
        end_id: str | None = None,
    ):
        super().__init__(link.id)
        self.link = link
        self.label = label
        self._start_id = start_id
        self._end_id = end_id
    @property
    def start_id(self):
        """
        Returns the effective start node id of the link (either the Link.start_id or if setter is
        called then returns that value).
        Returns:
            str: Effective start node id.
        """
        return self._start_id if self._start_id else self.link.start.id
    @start_id.setter
    def start_id(self, value: str | None):
        self._start_id = value
    @property
    def end_id(self):
        """
        Returns the effective end node id of the link (either the Link.end_id or if setter is called
            then returns that value).
        Returns:
            str: Effective end node id.
        """
        return self._end_id if self._end_id else self.link.end.id
    @end_id.setter
    def end_id(self, value: str | None):
        self._end_id = value
    def render_start(self, level):
        if not self.link.render:
            logging.info("Won't render link '%s' -> render property set to False", self.link)
            return ""
        label = self.label or ""
        if not self.label and self.link.style != LINK_STYLE_INVISIBLE:
            label = determine_link_label(self.link)
        if label:
            label = f"|{label}|"
        return self.format_graph_line(
            f"{self.start_id} {get_link_style(self.link)}{label} {self.end_id}", level
        )
    def __repr__(self) -> str:
        return f"Link: from {self.start_id} to {self.end_id}"
class StyleNode(Node):
    """
    Represents a style definition node.
    Attributes:
        id (str): The unique identifier of the node.
        style (str): The style of the node.
    """
    def __init__(self, node_id: str, style: str):
        super().__init__(node_id)
        self.style = style
    def render(self, level=0):
        """
        Renders the node with the specified style at the given indentation level.
        Args:
            level (int): The indentation level for rendering the node.
        Returns:
            str: The rendered graph line for the node.
        """
        return self.format_graph_line(f"classDef {self.id} {self.style}", 0, True)
    def __repr__(self) -> str:
        return f"Style: {self.id}"
class NodeRenderState:
    """Represents the render state of a node."""
    def __init__(self, remove: bool = False, collapse: bool = False, splat: bool = False):
        self.set_state(remove, collapse, splat)
    def set_state(self, remove: bool = False, collapse: bool = False, splat: bool = False):
        """
        Sets the state of the node.
        Args:
            remove (bool): Whether to remove the node.
            collapse (bool): Whether to collapse the node.
            splat (bool): Whether to splat the node.
        Returns:
            None
        """
        self._remove = remove
        if remove:
            self._collapse = False
            self._splat = False
        else:
            self._collapse = collapse
            self._splat = splat
    @property
    def remove(self):
        """
        Returns whether the node should be removed or not.
        Returns:
            bool: True if the node should be removed, False otherwise.
        """
        return self._remove
    @property
    def render(self):
        """
        Returns the node's render state.
        Returns:
            bool: True if the node should be rendered, False otherwise.
        """
        return not self._remove
    @property
    def splat(self):
        """
        Returns the node's splat state.
        Returns:
            bool: True if the node should be splatted, False otherwise.
        """
        return self._splat
    @property
    def collapse(self):
        """
        Returns the node's collapse state.
        Returns:
            bool: True if the node should be collapsed, False otherwise.
        """
        return self._collapse
================================================

File: __init__.py
================================================
"""Containt rendering logic to render tree model into mermaid graph."""
from __future__ import annotations
import logging
from firewall2mermaid.common import (
    CLASS_DEF,
    LINK_STYLE_INVISIBLE,
    get_effective_selector,
)
from firewall2mermaid.model import (
    Chain,
    GraphSelector,
    Link,
    LinkableTreeNode,
    RootNode,
    Section,
    TreeNode,
)
from firewall2mermaid.render.common import determine_rule_label, determine_rule_style
from firewall2mermaid.render.model import (
    CommentNode,
    GraphRootNode,
    LinkNode,
    LiteralNode,
    Node,
    NodeRenderState,
    RuleNode,
    StyleNode,
    SubgraphNode,
)
class Renderer:
    """Graph renderer"""
    def __init__(
        self,
        model: RootNode,
        graph_selector: list[GraphSelector],
        node_render_mode="auto",
        show_legend=True,
        graph_direction="TB",
        log_rules=False,
        collapse_as_rule=False,
        show_root=True,
        extra_logs: list[str] | None = None,
    ):
        """
        Initialize the Render object.
        Args:
            model (RootNode): The tree model.
            graph_selector (list[GraphSelector]): The list of graph selectors.
            node_render_mode (str, optional): The node comments rendering mode. Defaults to "auto".
            show_legend (bool, optional): Whether to generate/show legend nodes. Defaults to True.
            graph_direction (str, optional): The graph direction. Defaults to "TB".
            log_rules (bool, optional): Whether to add rule log at the top of graph. Defaults to
                False.
            collapse_as_rule (bool, optional): Whether to render collapsed chains as rules instead.
                Defaults to False.
            show_root (bool, optional): Whether to show the root node. Defaults to True.
            extra_logs (list[str], optional): The extra logs to add to the graph. Defaults to [].
        """
        self.model = model
        """Tree model"""
        self.node_render_mode = node_render_mode
        """Node comments rendering mode"""
        self.show_legend = show_legend
        """Generate/show legend nodes"""
        self.graph_direction = graph_direction
        """Graph direction"""
        self.log_rules = log_rules
        """Add rule log at the top of graph"""
        self.collapse_as_rule = collapse_as_rule
        """Render collapsed chains as rules instead"""
        self._last_rule_index = 0
        self._link_remap: dict[Link, tuple[str | None, str | None]] = {}
        """List of link remaps (start/end id)"""
        self.extra_logs = list(extra_logs or [])
        """Extra logs to add to the graph"""
        self.model_links = [l for section in self.model.sections for l in section.links]
        self.model_links.extend(l for chain in self.model.chains for l in chain.links)
        self.model_links.extend(l for rule in self.model.rules for l in rule.links)
        self.show_root = show_root
        self.graph_selector = graph_selector
        self.has_collapse_selectors = any(x.collapse for x in graph_selector)
    def _next_rule_index(self):
        """Helper method to keep track of ephemeral rules"""
        if self._last_rule_index == 0:
            self._last_rule_index = self.model.next_rule_index()
        self._last_rule_index += 1
        return self._last_rule_index
    def render_graph(self) -> str:
        """Generate Mermaid graph text for the passed model and configuration.
        Returns:
            str: The Mermaid graph text.
        """
        graph: GraphRootNode = self._generate_render_tree()
        if self.show_legend:
            self._add_legend_node(graph)
        logging.info("Rendering graph")
        return graph.render()
    def _generate_render_tree(self):
        graph = GraphRootNode()
        top_direction = "TB" if self.show_legend else self.graph_direction
        if self.extra_logs:
            for log in self.extra_logs:
                graph.add_child(CommentNode(log))
        graph.add_child(
            LiteralNode(r"%%{init: {'flowchart': {'htmlLabels': false}, 'theme': 'dark'}}%%")
        )
        graph.add_child(LiteralNode(rf"flowchart {top_direction}"))
        graph.add_child(LiteralNode())
        if self.log_rules:
            self._add_rule_log_nodes(graph)
            graph.add_child(LiteralNode())
        self._add_style_nodes(graph)
        graph.add_child(LiteralNode())
        self._add_model_nodes(graph)
        if self.collapse_as_rule:
            self._add_collapsed_as_rule_nodes(graph)
        self._add_link_nodes(graph)
        return graph
    def _add_link_nodes(self, graph: GraphRootNode):
        logging.info("Adding link nodes")
        graph.add_child(LiteralNode())
        graph.add_child(CommentNode("Relationships"))
        if self.model_links:
            for link in self.model_links:
                graph_link = self._create_link_node(link)
                # Drop self links
                if graph_link.start_id == graph_link.end_id:
                    logging.debug("Self link from/to '%s', skipping link", graph_link.start_id)
                    continue
                if not graph.find_node_by_id(graph_link.start_id, True):
                    # if start is collapsed
                    logging.debug(
                        "Start node (%s) is not rendered, skipping link(%s)",
                        graph_link.start_id,
                        link,
                    )
                    continue
                if not graph.find_node_by_id(graph_link.end_id, True):
                    logging.debug(
                        "End node (%s) is not rendered, skipping link(%s)", graph_link.end_id, link
                    )
                    continue
                logging.debug("Adding link node: %s", graph_link)
                graph.add_child(graph_link)
    def _create_link_node(self, link: Link):
        if link in self._link_remap:
            remapped = self._link_remap[link]
            logging.debug("Link (%s) remapped from to %s", link, remapped)
            start_id = remapped[0]
            end_id = remapped[1]
        else:
            start_id = link.start.id
            end_id = link.end.id
        return LinkNode(link, start_id=start_id, end_id=end_id)
    def _add_collapsed_as_rule_nodes(self, graph: GraphRootNode):
        logging.info("Adding collapsed sections/chains as rule nodes")
        collapsed_map = self._generate_collapsed_node_map()
        for link in self.model_links:
            if link.style == LINK_STYLE_INVISIBLE:
                continue
            if link.start.id in collapsed_map and link.end.id in collapsed_map:
                logging.debug(
                    "Both link start (%s) and end node (%s) are collapsed, skipping adding node",
                    link.start.id,
                    link.end.id,
                )
                continue
            if link.start.id in collapsed_map:
                element = collapsed_map[link.start.id]
                target = graph.find_node_by_id(link.end.id, recurse=True)
                assert target
                parent = target.parent
                assert parent
                rule = self._create_collapsed_node(element.id, element.id)
                index = parent.child_index(target.id) or 0
                parent.insert_child(index, rule)
                logging.debug("Added node (%s) as collapsed rule (%s)", element.id, rule.id)
                self._update_link_remap(link, rule.id, link.end.id)
            elif link.end.id in collapsed_map:
                element = collapsed_map[link.end.id]
                target = graph.find_node_by_id(link.start.id, recurse=True)
                assert target
                parent = target.parent
                assert parent
                rule = self._create_collapsed_node(element.id, element.id)
                index = parent.child_index(target.id) or -1
                parent.insert_child(index + 1, rule)
                logging.debug("Added node (%s) as collapsed rule (%s)", element.id, rule.id)
                self._update_link_remap(link, link.start.id, rule.id)
    def _generate_collapsed_node_map(self):
        collapsed_map: dict[str, LinkableTreeNode] = {}
        for section in self.model.sections:
            render = self._determine_rendering_status(section)
            if not render.collapse:
                continue
            collapsed_map[section.id] = section
            for chain in section.chains:
                render = self._determine_rendering_status(chain)
                if render.remove or render.splat:
                    continue
                collapsed_map[chain.id] = section
                for rule in chain.rules:
                    collapsed_map[rule.id] = section
        for chain in self.model.chains:
            if chain.id in collapsed_map:
                continue
            render = self._determine_rendering_status(chain)
            if render.remove or render.splat:
                continue
            if render.collapse:
                collapsed_map[chain.id] = chain
                for rule in chain.rules:
                    collapsed_map[rule.id] = chain
        return collapsed_map
    def _add_model_nodes(self, graph: GraphRootNode):
        logging.info("Rendering subgraphs")
        root: Node = graph
        if self.show_root:
            root = SubgraphNode(self.graph_direction, node_id="root")
            graph.add_child(root)
        for section in self.model.sections:
            self._add_section_node(section, root)
    def _add_section_node(self, section: Section, root: Node):
        section_node = None
        section_node = SubgraphNode(
            direction=self.graph_direction, node_id=section.id, name=section.name
        )
        for chain in section.chains:
            self._add_chain_node(chain, section_node, root)
        render = self._determine_rendering_status(section)
        if render.collapse:
            if self.collapse_as_rule:
                logging.debug(
                    "Section '%s' is collapsed as rule, deferring adding node", section.name
                )
                return
            logging.debug("Section '%s' is collapsed, adding as collapsed node", section.name)
            collapsed_node = self._create_collapsed_node(section.id, section.name)
            root.add_child(collapsed_node)
            self._update_remap_for_collapsed_node(section.id, collapsed_node.id)
            # update chain and rule links to point to collapsed node
            for chain in section.chains:
                self._update_remap_for_collapsed_node(chain.id, collapsed_node.id)
                for rule in chain.rules:
                    self._update_remap_for_collapsed_node(rule.id, collapsed_node.id)
        elif not render.render:
            logging.debug("Section '%s' is removed/hidden, skipping adding node", section.name)
        elif section_node.children:
            root.add_child(section_node)
            logging.debug("Added section '%s'", section)
        else:
            logging.debug("Section '%s' has no children, skipping adding to graph", section.name)
    def _add_chain_node(self, chain: Chain, parent: Node, root: Node):
        render = self._determine_rendering_status(chain)
        if not render.render:
            logging.debug("Chain '%s' is removed or hidden, skipping adding node", chain.name)
            return
        parent = root if render.splat else parent
        name = chain.id if render.splat else chain.name
        if render.collapse:
            self._add_chain_node_collapsed(chain, parent, name)
        else:
            self._add_chain_node_normal_render(chain, parent, name)
    def _add_chain_node_normal_render(self, chain, parent: Node, name):
        logging.debug("Rendering chain '%s' normally", chain.name)
        chain_node = SubgraphNode(direction=self.graph_direction, node_id=chain.id, name=name)
        parent.add_child(chain_node)
        logging.debug("Added chain '%s'", chain.name)
        for rule in chain.rules:
            rule_node = RuleNode(
                rule.id,
                determine_rule_label(rule, self.node_render_mode),
                determine_rule_style(rule),
            )
            chain_node.add_child(rule_node)
            logging.debug("Added rule node '%s' to chain", rule)
    def _add_chain_node_collapsed(self, chain: Chain, parent: Node, name: str):
        if self.collapse_as_rule:
            logging.debug("Chain '%s' is collapsed as rule, deferring adding node", chain.name)
            return
        logging.debug("Chain '%s' is collapsed, adding as collapsed node", chain.name)
        chain_node = self._create_collapsed_node(chain.id, name)
        self._update_remap_for_collapsed_node(chain.id, chain_node.id)
        for rule in chain.rules:
            self._update_remap_for_collapsed_node(rule.id, chain_node.id)
        parent.add_child(chain_node)
        logging.debug("Added chain '%s' as collapsed node", chain.name)
    def _create_collapsed_node(self, node_id: str, name: str):
        rule_id = f"{node_id}:collapsedrule{self._next_rule_index()}"
        return RuleNode(rule_id, f"{name} *collapsed", "collapsed")
    def _update_remap_for_collapsed_node(self, old_id: str, new_id: str):
        for link in self.model_links:
            if link.start.id == old_id:
                self._update_link_remap(link, new_id, None)
            if link.end.id == old_id:
                self._update_link_remap(link, None, new_id)
    def _update_link_remap(self, link: Link, start_id: str | None, end_id: str | None):
        if link in self._link_remap:
            self._link_remap[link] = (
                start_id or self._link_remap[link][0],
                end_id or self._link_remap[link][1],
            )
        else:
            self._link_remap[link] = (start_id, end_id)
        logging.debug("Link remap updated: %s -> %s", link, self._link_remap[link])
    def _get_styles_used(self) -> list[str]:
        """Return list of nodes styles used by renderable rules.
        Returns:
            list[str]: List of node styles.
        """
        styles: list[str] = []
        for section in self.model.sections:
            section_renderer = self._determine_rendering_status(section)
            for chain in section.chains:
                chain_renderer = self._determine_rendering_status(chain)
                render_rule = chain_renderer.splat or (
                    chain_renderer.render and section_renderer.render
                )
                if render_rule:
                    for rule in chain.rules:
                        style = determine_rule_style(rule)
                        if style and style not in styles:
                            styles.append(style)
        if self.has_collapse_selectors:
            styles.append("collapsed")
        return styles
    def _add_style_nodes(self, graph: GraphRootNode):
        logging.info("Adding styles")
        for style in self._get_styles_used():
            logging.debug("Adding style node: %s", style)
            graph.add_child(StyleNode(style, CLASS_DEF[style]))
    def _add_rule_log_nodes(self, graph: GraphRootNode):
        logging.info("Adding rule logs")
        for rule in self.model.rules:
            logging.debug("Adding rule: %s", rule)
            graph.add_child(CommentNode(rule.raw_line))
    def _add_legend_node(self, graph: GraphRootNode):
        logging.info("Adding legend node")
        legend_node = SubgraphNode("TB", node_id="legend", name="Legend")
        for style in self._get_styles_used():
            node = RuleNode(f"legend:rule{self._next_rule_index()}", f"*{style}", style)
            legend_node.add_child(node)
        index = 0
        root = graph
        if self.show_root:
            root = graph.find_node_by_id("root")
            if not root:
                raise ValueError("Can't find root node to add legend to")
        else:
            attachment_node: Node | None = next(graph.walk_nodes(SubgraphNode), None)
            if not attachment_node:
                attachment_node = next(graph.walk_nodes(RuleNode), None)
            index = graph.child_index(attachment_node.id) if attachment_node else 0
        root.insert_child(index or 0, legend_node)
        # legend was manually added during rendering so we will need to add links to it
        self._add_legend_link_nodes(graph, root)
    def _add_legend_link_nodes(self, graph: Node, root: Node):
        dummy = Section("dummy")
        for child in [x for x in root.children if isinstance(x, (RuleNode, SubgraphNode))]:
            if child.id == "legend":
                continue
            # start node doesn't matter as we will be overwritting its id
            link = Link(dummy, dummy, style=LINK_STYLE_INVISIBLE, label="")
            graph.add_child(LinkNode(link, start_id="legend", end_id=child.id))
    def _determine_rendering_status(self, element: TreeNode):
        if isinstance(element, Chain):
            return self._determine_chain_rendering_status(element)
        section_selector = get_effective_selector(self.graph_selector, element)
        if section_selector.remove:
            return NodeRenderState(remove=True)
        return NodeRenderState(collapse=section_selector.collapse)
    def _determine_chain_rendering_status(self, chain: Chain):
        chain_selector = get_effective_selector(self.graph_selector, chain)
        if chain_selector.remove:
            return NodeRenderState(remove=True)
        section_selector = get_effective_selector(self.graph_selector, chain.parent)
        if chain_selector.splat:
            return NodeRenderState(collapse=chain_selector.collapse, splat=True)
        if chain_selector.show and not chain_selector.default:
            return NodeRenderState(splat=not section_selector.show)
        if chain_selector.default:
            return NodeRenderState(
                splat=section_selector.splat,
                remove=section_selector.remove,
            )
        # section is collapsed but normal rendering for chain
        return NodeRenderState(
            collapse=True,
            splat=(section_selector.splat or section_selector.remove),
        )
================================================

File: tree.py
================================================
"""Creates AST tree that is used for rendering."""
import logging
from typing import Iterator
from firewall2mermaid.common import (
    ALL_FLOWS,
    FORWARD_FLOW,
    INPUT_FLOW,
    LINK_STYLE_INVISIBLE,
    OUTPUT_FLOW,
    POSTROUTING_FLOW,
    PREROUTING_FLOW,
    create_adhoc_rule,
    find_jump_target_rule,
    get_effective_selector,
)
from firewall2mermaid.model import (
    Chain,
    GraphSelector,
    PacketFlowElement,
    ParserRule,
    RootNode,
    Rule,
    Section,
)
class TreeMaker:
    """Constructs a tree graph from parsed rules. The tree is used for rendering the graph."""
    def __init__(
        self,
        parsed_rules: list[ParserRule],
        elements: list[GraphSelector],
        prune_disabled_rules=False,
        prune_log_rules=False,
        add_flow_elements=False,
    ):
        """Constructor
        Args:
            parsed_rules (list[ParserRule]): List of parsed rules to tree-fy
            elements (list[tuple[str,str]]): List of elements to populate tree with. Given in
                section, chain tuple.
            prune_disabled_rules (bool, optional): Whether to ignore/remove disabled nodes. Defaults
                to False.
            prune_log_rules (bool, optional): Whether to ignore/remove log rule nodes. Defaults to
                False.
            add_flow_elements (bool, optional): Add missing flow elements in the packet flow.
                Defaults to False.
        """
        self.parsed_nodes = list(parsed_rules)
        """List of parsed rules to tree-fy"""
        self.root: RootNode
        """Tree root"""
        self.graph_elements = list(elements)
        """List of elements to graph."""
        self.prune_disabled_rules = prune_disabled_rules
        """Whether to ignore/remove disabled nodes."""
        self.prune_log_rules = prune_log_rules
        """Whether to ignore/remove log rule nodes."""
        self.add_flow_elements = add_flow_elements
        """Add missing flow elements in the packet flow."""
    def make_tree(self) -> RootNode:
        """Construct a tree graph for given list of rules.
        Returns:
            Root: Constructed tree
        """
        logging.info("Constructing graph tree")
        self.root = RootNode()
        self._populate_tree()
        if self.add_flow_elements:
            self._add_missing_flow_elements()
        self._prune_tree()
        self._wire_relationships()
        return self.root
    def _prune_tree(self):
        """Prune generated tree"""
        logging.info("Pruning tree")
        prune_sections = []
        for section in self.root.sections:
            prune_chains = [
                chain for chain in section.chains if not self._should_graph_chain(chain)
            ]
            if len(prune_chains) == len(section.chains):
                prune_sections.append(section)
            else:
                for chain in prune_chains:
                    logging.debug("Pruning chain '%s'", chain)
                    chain.detach()
        for section in prune_sections:
            logging.debug("Pruning section '%s'", section)
            section.detach()
        for chain in self.root.chains:
            self._prune_rules(chain)
    def _prune_rules(self, chain: Chain):
        """Prune rules from chain based on pruning rules
        Args:
            chain (Chain): Chain to prune rules from
        """
        logging.debug("Pruning rules from chain '%s'", chain)
        prune_rules = []
        if self.prune_disabled_rules:
            prune_rules = [rule for rule in chain.rules if rule.disabled]
        if self.prune_log_rules:
            prune_rules.extend(rule for rule in chain.rules if rule.action == "log")
        for rule in prune_rules:
            logging.debug("Pruning rule '%s'", rule)
            rule.detach()
    def _populate_tree(self):
        """Populate tree from parsed rules without filtering any content."""
        for parsed_rule in self.parsed_nodes:
            section = self.root.get_or_add_section(parsed_rule.section)
            chain = section.get_or_add_chain(parsed_rule.chain)
            rule = Rule(
                line=parsed_rule.line,
                index=self.root.next_rule_index(),
                attributes=parsed_rule.attributes,
            )
            attrs = [f"{x}={rule.x}" for x in rule.known_attributes]
            logging.debug(
                "Adding rule '%s' at index %s with attributes: %s",
                rule.id,
                rule.index,
                " ".join(attrs),
            )
            chain.add_rule(rule)
    def _should_graph_chain(self, chain: Chain, chains_in_flow: list[Chain] | None = None) -> bool:
        """Check if chain should be graphed. Chain should be graphed if:
        1. The chain is not empty
        2. The chain is included in the graphing filters
        3. Chain is jumped to from another chain that will be graphed"""
        render = False
        chains_in_flow = chains_in_flow or []
        # use section selector to determine if chain should be graphed at first
        selector = get_effective_selector(self.graph_elements, chain.parent)
        render = selector.render
        # overwrite when chain selector is more specific
        selector = get_effective_selector(self.graph_elements, chain)
        if selector.remove or selector.splat:
            render = selector.render
        # check if chain is jumped by another chain that is to be graphed (this is a slow process
        # and could result in circular flow)
        if chain in chains_in_flow:
            logging.warning("Circular chain flow detected ignoring current check")
            return render
        for jump_chain in [
            x.parent
            for x in self.root.rules
            if x.action == "jump"
            and x.parent.parent == chain.parent
            and x.jump_target == chain.name
            and x.parent not in chains_in_flow
        ]:
            if self._should_graph_chain(jump_chain, chains_in_flow + [chain]):
                render = True
        logging.debug("Should render chain '%s': %s", chain.id, render)
        return render
    def _determine_graph_chains(self, tree: RootNode) -> list[Chain]:
        """Determine the chains that should be graphed in the given tree based on:
        1. Graphing filters
        2. Inclusions due to rule jumps
        Note this is a slow function so call it seldomly
        """
        chains: list[Chain] = []
        for section in tree.sections:
            for chain in section.chains:
                if self._should_graph_chain(chain):
                    logging.debug("Chain '%s' should be graphed", chain)
                    chains.append(chain)
        return chains
    def _list_has_chain(self, chains: list[Chain], section_name: str, chain_name: str) -> bool:
        """Check if section has chain with given name
        Args:
            chains (list[Chain]): List of chains to check if it contains given chain
            section (str): Section name to check
            chain_name (str): Chain name to check
        Returns:
            bool: True if section has chain with given name
        """
        return any(x for x in chains if x.name == chain_name and x.parent.name == section_name)
    def _add_missing_flow_elements(self):
        """Adds the missing packet flow elements (sections and chains) based on the current tree
        sections and chains"""
        graph_chains = self._determine_graph_chains(self.root)
        flows: list[PacketFlowElement] = []
        if (
            self._list_has_chain(graph_chains, "filter", "forward")
            or self._list_has_chain(graph_chains, "filter", "input")
            or self._list_has_chain(graph_chains, "nat", "srcnat")
            or self._list_has_chain(graph_chains, "mangle", "prerouting")
        ):
            flows.append(PREROUTING_FLOW)
        if self._list_has_chain(graph_chains, "filter", "input"):
            flows.append(INPUT_FLOW)
        if self._list_has_chain(graph_chains, "filter", "forward"):
            flows.append(FORWARD_FLOW)
        if self._list_has_chain(graph_chains, "filter", "output"):
            flows.append(OUTPUT_FLOW)
        if (
            self._list_has_chain(graph_chains, "filter", "forward")
            or self._list_has_chain(graph_chains, "filter", "output")
            or self._list_has_chain(graph_chains, "nat", "srcnat")
            or self._list_has_chain(graph_chains, "mangle", "postrouting")
        ):
            flows.append(POSTROUTING_FLOW)
        # add upstream chains based on flow
        for flow in flows:
            for item in iter(flow):
                section = self.root.get_or_add_section(item.section)
                if not section.has_chain(item.chain):
                    chain = section.add_chain(item.chain)
                    # add rule
                    chain.add_rule(
                        create_adhoc_rule(
                            section.name,
                            chain.name,
                            self.root.next_rule_index(),
                            action="accept",
                            comment="rule added for packet flow",
                        )
                    )
                # add if not already in graph_elements
                selector = get_effective_selector(
                    self.graph_elements, f"{item.section}:{item.chain}"
                )
                if not selector.render:
                    logging.debug(
                        "Adding missing flow element (%s, %s) to graph selector",
                        item.section,
                        item.chain,
                    )
                    self.graph_elements.append(GraphSelector(f"{item.section}:{item.chain}"))
    def _wire_relationships(self):
        for sections in self.root.sections:
            self._wire_section_relationships(sections)
        # packets flow from chains between section, there is an order between chains and within
        # chains
        self._add_flow_links_in_flows()
        self._add_links_between_flows()
    def _add_flow_links_in_flows(self):
        """Add packet flow links between items in same flow chain. For example for prerouting
        chain, the packet flow is raw prerouting -> mangle prerouting -> dstnat.
        """
        logging.debug("Adding packet flow links (chain level)")
        for flow in ALL_FLOWS:
            start_rule = None
            for item in flow:
                section = self.root.section(item.section)
                if not section:
                    flow = item.next
                    continue
                chain = section.chain(item.chain)
                if not chain:
                    flow = item.next
                    continue
                chain_first_rule = chain.first_rule()
                if (
                    start_rule
                    and (not start_rule.is_terminal_rule or start_rule.action == "accept")
                    and chain_first_rule
                ):
                    logging.debug(
                        "Adding link from '%s' to chain '%s'", start_rule.id, chain_first_rule.id
                    )
                    start_rule.add_link(chain_first_rule)
                    start_rule.parent.add_link(chain, LINK_STYLE_INVISIBLE)
                start_rule = chain.last_rule()
    def _add_links_between_flows(self):
        """Add links between flows"""
        logging.debug("Adding links between flows")
        # prerouting -> input
        prerouting = self._find_first_chain_in_flow(reversed(PREROUTING_FLOW))
        input_chain = self._find_first_chain_in_flow(INPUT_FLOW)
        if prerouting and input_chain:
            logging.debug("Adding link from '%s' to '%s'", prerouting.id, input_chain.id)
            prerouting.add_link(input_chain, LINK_STYLE_INVISIBLE)
            # add visible link
            last_rule = prerouting.last_rule()
            first_rule = input_chain.first_rule()
            if first_rule and last_rule:
                last_rule.add_link(first_rule)
        # prerouting -> forward
        forward = self._find_first_chain_in_flow(FORWARD_FLOW)
        if prerouting and forward:
            logging.debug("Adding link from '%s' to '%s'", prerouting.id, forward.id)
            prerouting.add_link(forward, LINK_STYLE_INVISIBLE)
            # add visible link
            last_rule = prerouting.last_rule()
            first_rule = forward.first_rule()
            if first_rule and last_rule:
                last_rule.add_link(first_rule)
        # forward -> postrouting
        forward_end = self._find_first_chain_in_flow(reversed(FORWARD_FLOW))
        postrouting = self._find_first_chain_in_flow(POSTROUTING_FLOW)
        if forward_end and postrouting:
            logging.debug("Adding link from '%s' to '%s'", forward_end.id, postrouting.id)
            forward_end.add_link(postrouting, LINK_STYLE_INVISIBLE)
            # add visible link
            last_rule = forward_end.last_rule()
            first_rule = postrouting.first_rule()
            if first_rule and last_rule:
                last_rule.add_link(first_rule)
        # output -> postrouting
        output = self._find_first_chain_in_flow(reversed(OUTPUT_FLOW))
        if output and postrouting:
            logging.debug("Adding link from '%s' to '%s'", output.id, postrouting.id)
            output.add_link(postrouting, LINK_STYLE_INVISIBLE)
            # add visible link
            last_rule = output.last_rule()
            first_rule = postrouting.first_rule()
            if first_rule and last_rule:
                last_rule.add_link(first_rule)
    def _find_first_chain_in_flow(self, flow: PacketFlowElement | Iterator[PacketFlowElement]):
        for item in flow:
            section = self.root.section(item.section)
            if not section:
                continue
            chain = section.chain(item.chain)
            if chain:
                return chain
        return None
    def _wire_section_relationships(self, section: Section):
        """Add relationships for rules in section
        Args:
            section (Section): Section to wire relationships
        """
        logging.debug("Adding links between rules in section %s", section.name)
        for chain in section.chains:
            rules = chain.rules
            start_rule = None
            for rule in sorted(rules, key=lambda x: x.index):
                if start_rule:
                    logging.debug("Adding link from '%s' to '%s'", start_rule.id, rule.id)
                    label = "otherwise" if start_rule.action == "jump" else None
                    start_rule.add_link(rule, label=label)
                start_rule = rule
                if rule.action == "jump":
                    logging.debug("Rule '%s' jumps to '%s'", rule.id, rule.parent)
                    wired = self._wire_jump_rule(rule)
                    # clear from rule as to not add link from the jump rule to the next rule if it
                    # is a blank jump
                    if wired and not rule.has_rule_matchers:
                        start_rule = None
    def _wire_jump_rule(self, rule: Rule) -> bool:
        """Wire relationships for jump rule
        Args:
            rule (Rule): Jump rule
        Returns:
            bool: True if the rule has been wired properly, False if jump target couldn't be found
        """
        section = rule.parent.parent
        jump_target = find_jump_target_rule(rule)
        if not jump_target:
            logging.warning("Can't find chain '%s' in '%s'", rule.jump_target, section)
            return False
        logging.debug("Adding link for jump from '%s' to '%s'", rule.id, jump_target.id)
        label = "if yes" if rule.has_rule_matchers else None
        rule.add_link(jump_target, label=label)
        # find the next rule to return to
        next_rule = rule.next_rule()
        if not next_rule:
            return True
        # add links from explicit returns in the jump chain to the next rule
        return_rules: list[Rule] = [x for x in jump_target.parent.rules if x.action == "return"]
        for return_rule in return_rules:
            logging.debug("Adding returning from '%s' to '%s'", return_rule.id, next_rule.id)
            return_rule.add_link(next_rule, label="return")
        # add link from implicit return (non-terminal last nodes), unless is return
        last_rule = jump_target.parent.last_rule()
        if last_rule and not last_rule.is_terminal_rule and last_rule.action != "return":
            logging.debug("Adding implicit returning from '%s' to '%s'", last_rule.id, next_rule.id)
            last_rule.add_link(next_rule, label="return")
        return True
================================================

File: __init__.py
================================================
"""Appliation entry point."""
from firewall2mermaid import app
if __name__ == "__main__":
    app.main()
================================================

File: __main__.py
================================================
"""Module entry point."""
from firewall2mermaid import app
if __name__ == "__main__":
    app.main()
================================================

File: asserters.py
================================================
from __future__ import annotations
import re
from typing import Callable, Generic, Optional
from typing_extensions import Self
from tests.assertions import (
    AsserterBase,
    AsserterContext,
    AsserterRootContext,
    TAsserter,
    TParent,
    line_depth,
)
from tests.assertions.augments import (
    IsCollapsed,
    WithDirection,
    WithId,
    WithLabel,
    WithLinkEnd,
    WithLinkStart,
    WithLinkStyle,
    WithStyle,
    WithoutStyle,
)
LINK_REGEX = r"(?P<start>\S+) (?P<link>[~\-.>]+)(?P<label>\|[^\|]+\|)? (?P<end>\S+)"
class ContinuationAsserter(Generic[TParent, TAsserter], AsserterBase[TParent]):
    """A mocking asserter used for creating a placeholder asserter that mimics the behavior
    of another asserter.
    Args:
        target (TAsserter): The target asserter to mimic.
    """
    def __init__(
        self, hierarchical_parent: TParent, continue_asserter: TAsserter, message="followed by"
    ) -> None:
        super().__init__(hierarchical_parent)
        self.target = continue_asserter
        self._message = message
    def match(self, soft_fail: bool = False, rematch_parent=True) -> bool:
        return self.parent.match(soft_fail, rematch_parent)
    def _next_match(self, context: AsserterContext) -> bool:
        """
        Internal method for matching, always returns False.
        Returns:
            bool: Always returns False.
        """
        return False
    def message(self) -> str:
        return self._message
    def join_message(self) -> str:
        return ""
    def extract_context(self, context: AsserterContext):
        return self.target.context
    def __getattr__(self, name: str):
        attr = getattr(self.target, name)
        if callable(attr):
            # wrapped calls to bound method as they use their own self (target here) as parents
            # and we will need to replace the first parent created by the method call to ensure the
            # parent chain is correct
            attr = wrap_mock_call(attr, self, self.target)
        return attr
    @property
    def last_match(self):
        return self.parent.last_match
    @last_match.setter
    def last_match(self, value):
        pass
def wrap_mock_call(
    function: Callable[..., AsserterBase[TParent]], mock: AsserterBase, mock_target: AsserterBase
):
    def wrapper(*args, **kwargs):
        mock_target._creation_asserter = mock
        asserter = function(*args, **kwargs)
        mock_target._creation_asserter = None
        return asserter
    return wrapper
class FollowableAsserter(AsserterBase[TParent]):
    @property
    def followed_by(self) -> TParent:
        """Create a followed by asserter for the current asserter."""
        target = self.parent
        if not target:
            raise ValueError("Unable to obtain a proper parent")
        return ContinuationAsserter[Self, TParent](self, target)  # type: ignore
    @property
    def and_then(self) -> TParent:
        """Create a followed by asserter for the current asserter."""
        return self.followed_by
class CountableAsserter(AsserterBase[TParent]):
    """Asserters that can be counted - i.e. LineAsserter, GraphAsserter"""
    def first(self) -> FirstAsserter[Self]:
        a = FirstAsserter(self._get_creation_asserter())
        a.match()
        return a
    def last(self) -> LastAsserter[Self]:
        a = LastAsserter(self._get_creation_asserter())
        a.match()
        return a
    def times(self, count: int) -> ExactCountAsserter[Self]:
        a = ExactCountAsserter(self._get_creation_asserter(), count)
        a.match()
        return a
    def exactly(self, count: int) -> ExactCountAsserter[Self]:
        return self.times(count)
    def once(self) -> ExactCountAsserter[Self]:
        return self.times(1)
    def count(self, count: int) -> ExactCountAsserter[Self]:
        return self.times(count)
    def at_least(self, count: int) -> MinCountAsserter[Self]:
        a = MinCountAsserter(self._get_creation_asserter(), count)
        a.match()
        return a
    def min(self, count: int) -> MinCountAsserter[Self]:
        return self.at_least(count)
    def at_most(self, count: int) -> MaxCountAsserter[Self]:
        a = MaxCountAsserter(self._get_creation_asserter(), count)
        a.match()
        return a
    def max(self, count: int) -> MaxCountAsserter[Self]:
        return self.at_most(count)
class GraphAsserterBase(AsserterBase[TParent]):
    """Base class for graph-based asserters."""
    def __init__(self, parent: TParent):
        super().__init__(parent)
    @property
    def advance_on_match(self):
        return False
    def has_line(self, line: str):
        asserter = LineAsserter(self._get_creation_asserter(), line)
        asserter.match()
        return asserter
    def matches_line(self, pattern: str):
        asserter = RegexLineAsserter(self._get_creation_asserter(), pattern)
        asserter.match()
        return asserter
    def has_graph(
        self, graph: str | None = None, direct_descendants_only=True
    ) -> GraphAsserter[Self]:
        asserter = GraphAsserter[Self](
            self._get_creation_asserter(), direct_descendants_only=direct_descendants_only
        )
        asserter.match()
        return asserter.with_id(graph) if graph else asserter
    def has_rule(self, id: int | str | None = None) -> RuleAsserter[Self]:
        asserter = RuleAsserter(self._get_creation_asserter())
        asserter.match()
        return asserter.with_id(id) if id else asserter
    def has_link(self, start: str | None = None) -> LinkAsserter[Self]:
        asserter = LinkAsserter(self._get_creation_asserter())
        asserter.match()
        return asserter.with_from(start) if start else asserter
    def with_label(self, label: str) -> Self:
        self.add_augment(WithLabel(label))
        return self
    def is_collapsed(self) -> Self:
        self.add_augment(IsCollapsed())
        return self
class RootAsserter(AsserterBase):
    """Top-most asserter"""
    def __init__(self, graph: str = "") -> None:
        self.context = AsserterRootContext(graph)
        self.last_match: int | None = 0
        """Last match index in the parent context (heystack). Used for re-matching."""
        self.parent = None
    def message(self) -> str:
        return ""
    def match(self, soft_fail: bool = False, rematch_parent=True) -> bool:
        return False
    def _next_match(self, context: AsserterContext) -> bool:
        return False
    def extract_context(self, context: AsserterContext):
        return self.context
class RootGraphAsserter(
    RootAsserter,
    GraphAsserterBase[RootAsserter],
):
    """Root-level asserter for graph-based assertions."""
    def __init__(self, graph: str) -> None:
        RootAsserter.__init__(self, graph)
        self.graph = graph
        self._creation_asserter = self
    def message(self) -> str:
        return f"in graph:\n{self.graph}"
    def has_style(self, style) -> StyleAsserter[Self]:
        asserter = StyleAsserter(self._get_creation_asserter(), style)
        asserter.match()
        return asserter
class GraphAsserter(
    GraphAsserterBase[TParent],
    CountableAsserter[TParent],
    FollowableAsserter[TParent],
):
    """Asserter for matching a graph/subgraph in the context."""
    def __init__(self, parent: TParent, direct_descendants_only=False):
        super().__init__(parent)
        self.direct_descendants = direct_descendants_only
    def _next_match(self, context: AsserterContext) -> bool:
        while context.has_line():
            # ignore the first line of the parent graph asseter otherwise we will be matching the same graph
            if isinstance(self.parent, GraphAsserterBase) and context.index == 0:
                context.next_line()
                continue
            line = context.current_line() or ""
            if f"subgraph " in line:
                if not self.direct_descendants or line_depth(line) == self.parent.context.depth + 1:
                    return True
            context.next_line()
        return False
    def message(self) -> str:
        return f"subgraph"
    def extract_context(self, context: AsserterContext):
        graph_level = 0
        start = context.index
        while context.has_line():
            line: str = context.current_line() or ""
            if line.strip().startswith("subgraph "):
                graph_level += 1
            elif line.strip() == "end":
                graph_level -= 1
            if graph_level == 0:
                break
            context.next_line()
        return AsserterContext(context.buffer[start : context.index + 1])
    def with_matching_label(self, label: str) -> Self:
        self.add_augment(WithLabel(label, reg_ex=True))
        return self
    def with_direction(self, direction: str) -> Self:
        self.add_augment(WithDirection(direction))
        return self
    def with_id(self, id: str) -> Self:
        self.add_augment(WithId(id))
        return self
class CountAsserterBase(AsserterBase[TParent]):
    """Asserters that do counting operations"""
    def __init__(self, parent: TParent):
        super().__init__(parent)
        self.tally: int = 0
    def extract_context(self, context: AsserterContext):
        return AsserterContext([])
    def _get_follow_parent_asserter(self) -> AsserterBase:
        """Get the follow parent asserter."""
        return self.parent.parent
    def _next_match(self, context: AsserterContext) -> bool:
        return False
    @property
    def context(self):
        return self.parent.context
    def join_message(self) -> str:
        return ""
class ExactCountAsserter(CountAsserterBase[TParent]):
    def __init__(self, parent: TParent, count: int) -> None:
        super().__init__(parent)
        self._count = count
    def match(self, soft_fail: bool = False, rematch_parent=True) -> bool:
        count = 1
        while self.parent.match(True, False):
            count += 1
        self.tally = count
        success = count == self._count
        if not success and not soft_fail:
            self.fail()
        return success
    def message(self) -> str:
        return f"exactly {self._count} (found {self.tally} times)"
class MinCountAsserter(CountAsserterBase[TParent]):
    def __init__(self, parent: TParent, min: int) -> None:
        super().__init__(parent)
        self._min = min
    def match(self, soft_fail: bool = False, rematch_parent=True) -> bool:
        count = 1
        while self.parent.match(True, False):
            count += 1
        self.tally = count
        success = count >= self._min
        if not success and not soft_fail:
            self.fail()
        return success
    def message(self) -> str:
        return f"at least {self._min} times(found {self.tally} times)"
class MaxCountAsserter(CountAsserterBase[TParent]):
    def __init__(self, parent: TParent, min: int) -> None:
        super().__init__(parent)
        self._max = min
    def match(self, soft_fail: bool = False, rematch_parent=True) -> bool:
        count = 1
        while self.parent.match(True, False):
            count += 1
        self.tally = count
        success = count <= self._max
        if not success and not soft_fail:
            self.fail()
        return success
    def message(self) -> str:
        return f"at most {self._max} times (found {self.tally} times)"
class LineAsserter(
    CountableAsserter[TParent],
    FollowableAsserter[TParent],
):
    """Asserter for matching a line in the context."""
    def __init__(self, parent: TParent, pattern: str):
        super().__init__(parent)
        self.pattern: str = pattern
    def _next_match(self, context: AsserterContext) -> bool:
        while context.has_line():
            line: str = context.current_line() or ""
            if self._compare_line(line):
                return True
            context.next_line()
        return False
    def message(self) -> str:
        return f"line that matches '{self.pattern}'"
    def _compare_line(self, line: str):
        """
        Compare the given line with the pattern.
        Args:
            line (str): The line to compare.
        Returns:
            bool: True if the pattern is found in the line, False otherwise.
        """
        return self.pattern in line
    def extract_context(self, context: AsserterContext):
        return AsserterContext([context.buffer[context.index]])
class FirstAsserter(CountAsserterBase[TParent]):
    def __init__(self, parent: TParent) -> None:
        super().__init__(parent)
    def match(self, soft_fail: bool = False, rematch_parent=True) -> bool:
        # TODO: not happy with this implementation, it works for now but detecting when being called
        # form sub-asserter needs to be improved
        if soft_fail and rematch_parent:
            # when called to rematch parent, our strategy is to call next until the parent's contex changes
            if isinstance(self.parent, RootAsserter) or isinstance(
                self.parent.parent, RootAsserter
            ):
                return False if soft_fail else self.fail()
            while self.parent.match(True, False):
                pass
            return self.parent.match(True, True)
        else:
            self.parent.last_match = -1
            return self.parent.match()
    def message(self) -> str:
        return "[first element]"
class LastAsserter(CountAsserterBase[TParent]):
    def __init__(self, parent: TParent) -> None:
        super().__init__(parent)
    def match(self, soft_fail: bool = False, rematch_parent=True) -> bool:
        # TODO: not happy with this implementation, it works for now but detecting when being called
        # form sub-asserter needs to be improved
        if soft_fail and rematch_parent:
            if not self.parent.match(soft_fail, rematch_parent):
                return False
        # match until there are no more parents
        while self.parent.match(True, False):
            pass
        return True
    def message(self) -> str:
        return "[last element]"
class RegexLineAsserter(LineAsserter[TParent]):
    """Asserter for matching a line with a regular expression pattern."""
    def __init__(self, parent: TParent, pattern: str):
        super().__init__(parent, "")
        self.pattern: str = pattern
        self.compiled_pattern = re.compile(self.pattern)
        self.matcher: Optional[re.Match[str]] = None
    def _compare_line(self, line: str) -> bool:
        self.matcher = self.compiled_pattern.search(line)
        return self.matcher is not None
class StyleAsserter(LineAsserter[TParent]):
    def __init__(self, parent: TParent, style_id: str):
        super().__init__(parent, f"classDef {style_id}")
        self.style = style_id
    def message(self) -> str:
        return f"style '{self.style}'"
RULE_REGEX = r"^\s*([\w\-]+:){0,2}(collapsed)?rule"
class RuleAsserter(
    RegexLineAsserter[TParent],
):
    """Asserter for matching a graph/subgraph in the context."""
    def __init__(self, parent: TParent):
        super().__init__(parent, RULE_REGEX)
    def message(self) -> str:
        return "rule"
    def with_label(self, label: str) -> Self:
        self.add_augment(WithLabel(label))
        return self
    def matching_label(self, pattern: str) -> Self:
        self.add_augment(WithLabel(pattern, reg_ex=True))
        return self
    def with_id(self, id: int | str) -> Self:
        if isinstance(id, str) and re.match(RULE_REGEX, id):
            self.add_augment(WithId(id, use_regex=False))
        else:
            self.add_augment(WithId(rf"{RULE_REGEX}{id}", use_regex=True))
        return self
    def with_style(self, style: str) -> Self:
        self.add_augment(WithStyle(style))
        return self
    def without_style(self, style: str) -> Self:
        self.add_augment(WithoutStyle(style))
        return self
    def without_any_style(self) -> Self:
        self.add_augment(WithoutStyle())
        return self
class LinkAsserter(
    RegexLineAsserter[TParent],
):
    """Asserter for matching a graph/subgraph in the context."""
    def __init__(self, parent: TParent):
        super().__init__(parent, LINK_REGEX)
    def message(self) -> str:
        return "link"
    def with_label(self, label: str) -> Self:
        self.add_augment(WithLabel(label, "|", "|"))
        return self
    def matching_label(self, pattern: str) -> Self:
        self.add_augment(WithLabel(pattern, "|", "|", reg_ex=True))
        return self
    def with_from(self, id: str) -> Self:
        self.add_augment(WithLinkStart(id))
        return self
    def matching_from(self, pattern: str) -> Self:
        self.add_augment(WithLinkStart(pattern, use_regex=True))
        return self
    def with_to(self, id: str) -> Self:
        self.add_augment(WithLinkEnd(id))
        return self
    def matching_to(self, pattern: str) -> Self:
        self.add_augment(WithLinkEnd(pattern, use_regex=True))
        return self
    def with_style(self, style: str) -> Self:
        self.add_augment(WithLinkStyle(style))
        return self
================================================

File: augments.py
================================================
from __future__ import annotations
import re
from tests.assertions import AsserterContext, AugmentBase
def extract_label(line: str, open: str = "[", close: str = "]") -> str:
    if open == close:
        return line.split(open)[1]
    return line.split(open)[1].split(close)[0]
class WithLabel(AugmentBase):
    """With asserter for simple label matching."""
    def __init__(self, pattern: str, open="[", close="]", reg_ex=False):
        self.label: str = pattern
        self.open = open
        self.close = close
        self.reg_ex = reg_ex
        self.compiled_pattern = re.compile(pattern) if reg_ex else None
    def match(self, context: AsserterContext) -> bool:
        line = context.current_line() or ""
        if self.open not in line or self.close not in line:
            return False
        label = extract_label(line, self.open, self.close)
        if not self.compiled_pattern:
            return self.label in label
        return self.compiled_pattern.search(label) is not None
    def message(self) -> str:
        if self.reg_ex:
            return f"label matching '{self.label}'"
        return f"label '{self.label}'"
class WithStyle(AugmentBase):
    """With asserter for style matching"""
    def __init__(self, style: str):
        self.style: str = style
    def match(self, context: AsserterContext) -> bool:
        line = context.current_line() or ""
        if ":::" not in line:
            return False
        style = line.split(":::")[1]
        return self.style == style
    def message(self) -> str:
        return f"style '{self.style}'"
class WithoutStyle(AugmentBase):
    """With asserter for negative style matching."""
    def __init__(self, style: str | None = None):
        self.style: str | None = style
    def match(self, context: AsserterContext) -> bool:
        line = context.current_line() or ""
        if not self.style:
            return ":::" not in line
        # Without specific style
        style = line.split(":::")[1]
        return self.style != style
    def message(self) -> str:
        return f"no style matching '{self.style}'" if self.style else "no styles"
class WithId(AugmentBase):
    """With asserter for matching node id"""
    def __init__(self, id: str, use_regex=False):
        self.id: str = id
        self.use_regex = use_regex
        if use_regex:
            self.pattern = re.compile(id)
    def match(self, context: AsserterContext) -> bool:
        line: str = context.current_line() or ""
        if "[" in line:
            line = line.split("[")[0].rstrip()
        line = line.split(" ")[-1].strip()
        if self.use_regex:
            return self.pattern.match(line) is not None
        return line == self.id
    def message(self) -> str:
        return f"id '{self.id}'"
class WithDirection(AugmentBase):
    """With asserter for matching subgraph direction"""
    def __init__(self, direction: str):
        self.direction: str = direction
    def match(self, context: AsserterContext) -> bool:
        while context.has_line():
            line: str = context.current_line() or ""
            if line.strip() == f"direction {self.direction}":
                return True
            context.next_line()
        return False
    def message(self) -> str:
        return f"direction '{self.direction}'"
class AtDepth(AugmentBase):
    """With asserter for matching exact node depth"""
    def __init__(self, level: int):
        self.level: int = level
    def match(self, context) -> bool:
        return context.depth == self.level
    def message(self) -> str:
        return f"at depth of {self.level}"
class AtMinDepth(AugmentBase):
    """With asserter for matching exact node depth"""
    def __init__(self, level: int):
        self.level: int = level
    def match(self, context) -> bool:
        return context.depth >= self.level
    def message(self) -> str:
        return f"at minimum depth of {self.level}"
class AtMaxDepth(AugmentBase):
    """With asserter for matching exact node depth"""
    def __init__(self, level: int):
        self.level: int = level
    def match(self, context) -> bool:
        return context.depth <= self.level
    def message(self) -> str:
        return f"at maximum depth of {self.level}"
class WithLinkStyle(AugmentBase):
    """With asserter for matching node in link start"""
    def __init__(self, style: str):
        self.style: str = style
    def match(self, context: AsserterContext) -> bool:
        from tests.assertions.asserters import LINK_REGEX
        m = re.match(LINK_REGEX, context.current_line() or "")
        return self.style in m.group("link") if m else False
    def message(self) -> str:
        return f"link style '{self.style}'"
class WithLinkStart(AugmentBase):
    """With asserter for matching node in link start"""
    def __init__(self, pattern: str, use_regex=False):
        self.pattern: str = pattern
        self.use_regex = use_regex
        if self.use_regex:
            self.compiled_pattern = re.compile(self.pattern)
    def match(self, context: AsserterContext) -> bool:
        from tests.assertions.asserters import LINK_REGEX
        m = re.match(LINK_REGEX, context.current_line() or "")
        if not m:
            return False
        start = m.group("start")
        return (
            self.compiled_pattern.match(start) is not None
            if self.use_regex
            else self.pattern == start
        )
    def message(self) -> str:
        return f"from matching '{self.pattern}'" if self.use_regex else f"from '{self.pattern}'"
class WithLinkEnd(AugmentBase):
    """With asserter for matching node in link start"""
    def __init__(self, pattern: str, use_regex=False):
        self.pattern: str = pattern
        self.use_regex: bool = use_regex
        if self.use_regex:
            self.compiled_pattern = re.compile(self.pattern)
    def match(self, context: AsserterContext) -> bool:
        from tests.assertions.asserters import LINK_REGEX
        m = re.match(LINK_REGEX, context.current_line() or "")
        if not m:
            return False
        end = m.group("end")
        return (
            self.compiled_pattern.match(end) is not None if self.use_regex else self.pattern == end
        )
    def message(self) -> str:
        return f"to matching '{self.pattern}'" if self.use_regex else f"to '{self.pattern}'"
class IsCollapsed(AugmentBase):
    """Assert graph node is collapsed"""
    def match(self, context: AsserterContext) -> bool:
        # context should be two lines subgraph X/end
        return len(context) == 2
    def message(self) -> str:
        return f"that is collapsed"
================================================

File: test_asserters.py
================================================
from assertpy import assert_that
from unittest.mock import patch
from unittest.mock import patch
import pytest
from firewall2mermaid.common import LINK_STYLE_NORMAL
from tests.assertions import (
    AsserterContext,
    AsserterRootContext,
    AssertionFailure,
    RootGraphAsserter,
)
from tests.assertions.asserters import (
    ContinuationAsserter,
    ExactCountAsserter,
    FirstAsserter,
    GraphAsserter,
    LastAsserter,
    LineAsserter,
    LinkAsserter,
    MaxCountAsserter,
    MinCountAsserter,
    ContinuationAsserter,
    RegexLineAsserter,
    RootAsserter,
    RuleAsserter,
    StyleAsserter,
)
from tests.assertions.augments import (
    WithId,
    WithLabel,
    WithLinkEnd,
    WithLinkStart,
    WithLinkStyle,
    WithStyle,
    WithoutStyle,
)
sample_graph = """subgraph A
\tsubgraph A1
\t\t\tA1 -> A2
\t\t\tA1 -> A2
\tend
end
%% comment line
subgraph B
\tsubgraph B1
\t\tB1 -> B2
\t\tB1 -> B2
\tend
\tsubgraph B2
\t\tB2 -> B3
\tend
end
subgraph C
end
"""
multi_line_text = "\n".join(
    [
        "This is line 1",
        "This is line 2",
        "This is line 3",
        "This is duplicated line",
        "This is duplicated line",
        "This is line 6",
    ]
)
class TestRootAsserter:
    def test_instantiation_without_arguments(self):
        asserter = RootAsserter()
        assert_that(asserter).is_not_none()
    def test_context_instance_of_AsserterRootContext(self):
        asserter = RootAsserter()
        assert_that(asserter.context).is_instance_of(AsserterRootContext)
    def test_extract_context_does_nothing(self):
        asserter = RootAsserter()
        context = AsserterContext(["line 1", "line 2", "line 3"])
        asserter.extract_context(context)
        assert_that(context.index).is_equal_to(0)
    def test_message_method_returns_empty_string(self):
        asserter = RootAsserter()
        assert_that(asserter.message()).is_empty()
    def test_match_method_returns_false_by_default(self):
        asserter = RootAsserter()
        assert_that(asserter.match()).is_false()
    def test_last_match_returns_zero(self):
        asserter = RootAsserter()
        assert_that(asserter.last_match).is_equal_to(0)
class TestRootGraphAsserter:
    def test_instantiation_with_valid_graph(self, sample_graph_text):
        asserter = RootGraphAsserter(sample_graph_text)
        assert_that(asserter).is_not_none()
    def test_context_instance_of_AsserterRootContext(self, sample_graph_text):
        asserter = RootGraphAsserter(sample_graph_text)
        assert_that(asserter.context).is_instance_of(AsserterRootContext)
    def test_extract_returns_current_context(self, sample_graph_text):
        asserter = RootGraphAsserter(sample_graph_text)
        context = AsserterContext(["line 1", "line 2", "line 3"])
        assert_that(asserter.extract_context(context)).is_equal_to(asserter.context)
    def test_message_method_returns_graph_message(self, sample_graph_text):
        asserter = RootGraphAsserter(sample_graph_text)
        assert_that(asserter.message()).is_equal_to(f"in graph:\n{sample_graph_text}")
    def test_match_method_returns_false_by_default(self, sample_graph_text):
        asserter = RootGraphAsserter(sample_graph_text)
        assert_that(asserter.match()).is_false()
    def text_has_style_with_valid_style(self, sample_graph_text):
        asserter = RootGraphAsserter(sample_graph_text)
        assert_that(asserter.has_style("log")).is_instance_of(StyleAsserter)
    def test_has_style_continued_uses_mock_as_self(self):
        # Arrange
        parent = RootGraphAsserter("Line 1\nclassDef dummy fill:#123456")
        asserter = ContinuationAsserter(LineAsserter(parent, "Line"), parent)
        # Act
        sut = asserter.has_style("dummy")
        # Assert
        assert_that(sut.parent).is_not_none().is_instance_of(ContinuationAsserter)
class TestLineAsserter:
    def test_instantiation_with_valid_arguments(self):
        parent = RootAsserter("line")
        pattern = "test"
        line_asserter = LineAsserter(parent, pattern)
        assert_that(line_asserter).is_not_none()
        assert_that(line_asserter.parent).is_equal_to(parent)
        assert_that(line_asserter.pattern).is_equal_to(pattern)
    def test_message_method_returns_expected_message(self):
        parent = RootAsserter("line")
        pattern = "line 1"
        line_asserter = LineAsserter(parent, pattern)
        assert_that(line_asserter.message()).is_equal_to(f"line that matches '{pattern}'")
    def test_match_line_with_pattern(self):
        # Arrange
        parent = RootAsserter("line 1\nline 2\nline 3")
        pattern = "line 2"
        line_asserter = LineAsserter(parent, pattern)
        # Act
        result = line_asserter.match()
        # Assert
        assert_that(result).is_true()
    def test_fail_to_match_when_pattern_not_found(self):
        # Arrange
        parent = RootAsserter("line 1\nline 2\nline 3")
        pattern = "line 4"
        line_asserter = LineAsserter(parent, pattern)
        # Act
        result = line_asserter.match(soft_fail=True)
        # Assert
        assert_that(result).is_false()
    def test_matches_first_line_when_multiple_lines_with_pattern_present(self):
        # Set up
        buffer = "\n".join(
            [
                "This is line 1",
                "This is line 2 with the pattern",
                "This is line 3",
                "This is line 4 with the pattern",
                "This is line 5",
            ]
        )
        parent = RootAsserter(buffer)
        pattern = "pattern"
        line_asserter = LineAsserter(parent, pattern)
        # Execute
        result = line_asserter.match()
        # Assert
        assert_that(result).is_true()
        assert_that(line_asserter.context.buffer).contains_only("This is line 2 with the pattern")
class TestRegexLineAsserter:
    def test_instantiation_with_valid_arguments(self):
        parent = RootAsserter("line")
        pattern = "test"
        regex_line_asserter = RegexLineAsserter(parent, pattern)
        assert_that(regex_line_asserter).is_not_none()
        assert_that(regex_line_asserter.parent).is_equal_to(parent)
        assert_that(regex_line_asserter.pattern).is_equal_to(pattern)
    def test_message_method_returns_expected_message(self):
        parent = RootAsserter("line")
        pattern = "line 1"
        regex_line_asserter = RegexLineAsserter(parent, pattern)
        assert_that(regex_line_asserter.message()).is_equal_to(f"line that matches '{pattern}'")
    def test_match_line_with_pattern(self):
        # Arrange
        parent = RootAsserter("line 1\nline 2\nline 3")
        pattern = "line 2"
        regex_line_asserter = RegexLineAsserter(parent, pattern)
        # Act
        result = regex_line_asserter.match()
        # Assert
        assert_that(result).is_true()
    def test_fail_to_match_when_pattern_not_found(self):
        # Arrange
        parent = RootAsserter("line 1\nline 2\nline 3")
        pattern = "line 4"
        regex_line_asserter = RegexLineAsserter(parent, pattern)
        # Act
        result = regex_line_asserter.match(soft_fail=True)
        # Assert
        assert_that(result).is_false()
    def test_matches_first_line_when_multiple_lines_with_pattern_present(self):
        # Set up
        buffer = "\n".join(
            [
                "This is line 1",
                "This is line 2 with the pattern",
            ]
        )
        parent = RootAsserter(buffer)
        pattern = r"pat+ern"
        regex_line_asserter = RegexLineAsserter(parent, pattern)
        # Execute
        result = regex_line_asserter.match()
        # Assert
        assert_that(result).is_true()
        assert_that(regex_line_asserter.context.buffer).contains_only(
            "This is line 2 with the pattern"
        )
class TestGraphAsserter:
    def test_matched_context_includes_full_graph_definition(self):
        # Arrange
        root = RootAsserter("subgraph A\nend")
        sut = GraphAsserter(root)
        # Act
        sut.match()
        # Assert
        assert_that(sut.context.index).is_equal_to(0)
        assert_that(sut.context.buffer).contains("subgraph A", "end").is_length(2)
    # Sub-subgraph should ignore the first line of its parent subgraph matcher
    def test_child_graph_asserter_ignores_first_line_of_parent_graph_asseter(self):
        # Arrange
        root = RootAsserter(sample_graph)
        parent = GraphAsserter(root)
        sut = GraphAsserter(parent)
        # Act
        parent.match()
        sut.match()
        # Assert
        assert_that(sut.context.index).is_equal_to(0)
        # parent matches subgraph A, so the first line of subgraph A1 is ignored
        assert_that(sut.context.reconstruct_buffer().lstrip()).starts_with("subgraph A1")
    def test_has_line_continued_uses_mock_as_self(self):
        # Arrange
        continue_from = GraphAsserter(RootAsserter("subgraph A\nsubgraph B\nend\nA1end\n"))
        parent = GraphAsserter(continue_from)
        asserter = ContinuationAsserter(parent, continue_from)
        # Act
        parent.match()
        sut = asserter.has_line("A1")
        # Assert
        assert_that(sut.parent).is_not_none().is_instance_of(ContinuationAsserter)
    def test_matches_line_continued_uses_mock_as_self(self):
        # Arrange
        continue_from = GraphAsserter(RootAsserter("subgraph A\nsubgraph B\nend\nA1end\n"))
        parent = GraphAsserter(continue_from)
        asserter = ContinuationAsserter(parent, continue_from)
        # Act
        parent.match()
        sut = asserter.matches_line("A.*")
        # Assert
        assert_that(sut.parent).is_not_none().is_instance_of(ContinuationAsserter)
    def test_has_graph_continued_uses_mock_as_self(self):
        # Arrange
        continue_from = GraphAsserter(
            RootAsserter("subgraph A\nsubgraph B\nend\nsubgraph C\nend\nend\n")
        )
        parent = GraphAsserter(continue_from)
        asserter = ContinuationAsserter(parent, continue_from)
        # Act
        parent.match()
        sut = asserter.has_graph(direct_descendants_only=False)
        # Assert
        assert_that(sut.parent).is_not_none().is_instance_of(ContinuationAsserter)
    def test_has_rule_continued_uses_mock_as_self(self):
        # Arrange
        continue_from = GraphAsserter(
            RootAsserter("subgraph A\nsubgraph B\nend\nrule[rule]\nend\n")
        )
        parent = GraphAsserter(continue_from)
        asserter = ContinuationAsserter(parent, continue_from)
        # Act
        parent.match()
        sut = asserter.has_rule()
        # Assert
        assert_that(sut.parent).is_not_none().is_instance_of(ContinuationAsserter)
    def test_has_link_continued_uses_mock_as_self(self):
        # Arrange
        continue_from = GraphAsserter(
            RootAsserter("subgraph A\nsubgraph B\nend\nrule --> rule\nend\n")
        )
        parent = GraphAsserter(continue_from)
        asserter = ContinuationAsserter(parent, continue_from)
        # Act
        parent.match()
        sut = asserter.has_link()
        # Assert
        assert_that(sut.parent).is_not_none().is_instance_of(ContinuationAsserter)
class TestStyleAsserter:
    def test_instantiation_with_valid_arguments(self):
        parent = RootAsserter("line")
        style_id = "test"
        style_asserter = StyleAsserter(parent, style_id)
        assert_that(style_asserter).is_not_none()
        assert_that(style_asserter.parent).is_equal_to(parent)
        assert_that(style_asserter.style).is_equal_to(style_id)
    def test_message_method_returns_expected_message(self):
        parent = RootAsserter("line")
        style_id = "style1"
        style_asserter = StyleAsserter(parent, style_id)
        assert_that(style_asserter.message()).is_equal_to(f"style '{style_id}'")
    def test_match_line_with_style(self):
        # Arrange
        parent = RootAsserter("line 1\nclassDef style rgbabel")
        style_id = "style"
        style_asserter = StyleAsserter(parent, style_id)
        # Act
        result = style_asserter.match()
        # Assert
        assert_that(result).is_true()
class TestRuleAsserter:
    def test_instantiation_with_valid_arguments(self):
        parent = RootAsserter('first line\nsection:chain:rule1["with comment"]:::drop')
        rule_asserter = RuleAsserter(parent)
        assert_that(rule_asserter).is_not_none()
        assert_that(rule_asserter.parent).is_equal_to(parent)
    def test_message_method_returns_expected_message(self):
        parent = RootAsserter('first line\nsection:chain:rule1["with comment"]:::drop')
        rule_asserter = RuleAsserter(parent)
        assert_that(rule_asserter.message()).is_equal_to("rule")
    @pytest.mark.parametrize(
        "rule",
        [
            "rule1",
            "section:collapsedrule",
            "section:chain:collapsedrule",
            "section:chain:rule1",
            "section:rule1",
            'section:chain:rule1["with comment"]:::drop',
            "section:chain-special-chars:rule1",
        ],
    )
    def test_match_when_is_rule_returns_true(self, rule):
        # Arrange
        rule_asserter = RuleAsserter(RootAsserter(rule))
        # Act
        result = rule_asserter.match(soft_fail=True)
        # Assert
        assert_that(result).is_true()
    @pytest.mark.parametrize(
        "rule",
        ["notarule", "subgraph rule", "section: not a rule"],
    )
    def test_match_when_not_valid_rule_line_returns_false(self, rule):
        # Arrange
        rule_asserter = RuleAsserter(RootAsserter(rule))
        # Act
        result = rule_asserter.match(soft_fail=True)
        # Assert
        assert_that(result).is_false()
    def test_with_label_adds_WithLabel_augment_and_runs_match(self):
        # Arrange
        parent = RootAsserter('first line\nsection:chain:rule1["with comment"]:::drop')
        rule_asserter = RuleAsserter(parent)
        label = "comment"
        # Act
        result = rule_asserter.with_label(label)
        # Assert
        assert_that(result.augments).is_not_empty()
        assert_that(result.augments[0]).is_type_of(WithLabel)
        assert_that(result.context.reconstruct_buffer()).is_equal_to(
            'section:chain:rule1["with comment"]:::drop'
        )
    def test_matching_label_adds_WithMatchingLabel_augment_and_runs_match(self):
        # Arrange
        parent = RootAsserter('first line\nsection:chain:rule1["with comment"]:::drop')
        rule_asserter = RuleAsserter(parent)
        pattern = "com+ent"
        # Act
        result = rule_asserter.matching_label(pattern)
        # Assert
        assert_that(result.augments).is_not_empty()
        assert_that(result.augments[0]).is_type_of(WithLabel)
        assert_that(result.context.reconstruct_buffer()).is_equal_to(
            'section:chain:rule1["with comment"]:::drop'
        )
    def test_with_id_adds_WithId_augment_and_runs_match(self):
        # Arrange
        parent = RootAsserter('first line\nsection:chain:rule1["with comment"]:::drop')
        rule_asserter = RuleAsserter(parent)
        id = 1
        # Act
        result = rule_asserter.with_id(id)
        # Assert
        assert_that(result.augments).is_not_empty()
        assert_that(result.augments[0]).is_type_of(WithId)
        assert_that(result.context.reconstruct_buffer()).is_equal_to(
            'section:chain:rule1["with comment"]:::drop'
        )
    def test_with_style_adds_WithStyle_augment_and_runs_match(self):
        # Arrange
        parent = RootAsserter('first line\nsection:chain:rule1["with comment"]:::drop')
        rule_asserter = RuleAsserter(parent)
        style = "drop"
        # Act
        result = rule_asserter.with_style(style)
        # Assert
        assert_that(result.augments).is_not_empty()
        assert_that(result.augments[0]).is_type_of(WithStyle)
        assert_that(result.context.reconstruct_buffer()).is_equal_to(
            'section:chain:rule1["with comment"]:::drop'
        )
    def test_without_style_adds_WithoutStyle_augment_and_runs_match(self):
        # Arrange
        parent = RootAsserter('first line\nsection:chain:rule1["with comment"]:::drop')
        rule_asserter = RuleAsserter(parent)
        style = "style"
        # Act
        result = rule_asserter.without_style(style)
        # Assert
        assert_that(result.augments).is_not_empty()
        assert_that(result.augments[0]).is_type_of(WithoutStyle)
        assert_that(result.context.reconstruct_buffer()).is_equal_to(
            'section:chain:rule1["with comment"]:::drop'
        )
    def test_with_id_when_given_string_id_match_without_prefixing(self):
        # Arrange
        parent = RootAsserter("section:ruleid[my rule]")
        rule_asserter = RuleAsserter(parent)
        # Act
        result = rule_asserter.with_id("section:ruleid")
        # Assert
        assert_that(result.augments).is_not_empty()
        augment = result.augments[0]
        assert_that(augment).is_type_of(WithId)
        assert isinstance(augment, WithId)
        assert_that(augment.id).is_equal_to("section:ruleid")
        assert_that(augment.use_regex).is_false()
    def test_without_any_style_adds_WithoutStyle_augment_without_style_argument_and_runs_match(
        self,
    ):
        # Arrange
        parent = RootAsserter('first line\nsection:chain:rule1["with comment"]')
        rule_asserter = RuleAsserter(parent)
        # Act
        result = rule_asserter.without_any_style()
        # Assert
        assert_that(result.augments).is_not_empty()
        assert_that(result.augments[0]).is_type_of(WithoutStyle)
        assert_that(result.context.reconstruct_buffer()).is_equal_to(
            'section:chain:rule1["with comment"]'
        )
class TestLinkAsserter:
    def test_instantiation_with_valid_arguments(self):
        parent = RootAsserter("first line\nrule1 --> rule2")
        link_asserter = LinkAsserter(parent)
        assert_that(link_asserter).is_not_none()
        assert_that(link_asserter.parent).is_equal_to(parent)
    def test_message_method_returns_expected_message(self):
        parent = RootAsserter("first line\nrule1 --> rule2")
        link_asserter = LinkAsserter(parent)
        assert_that(link_asserter.message()).is_equal_to("link")
    def test_with_label_adds_WithLabel_augment_and_runs_match(self):
        # Arrange
        parent = RootAsserter("first line\nrule1 -->|link label| rule2")
        link_asserter = LinkAsserter(parent)
        label = "label"
        # Act
        result = link_asserter.with_label(label)
        # Assert
        assert_that(result.augments).is_not_empty()
        assert_that(result.augments[0]).is_type_of(WithLabel)
        assert_that(result.context.reconstruct_buffer()).is_equal_to("rule1 -->|link label| rule2")
    def test_matching_label_adds_WithMatchingLabel_augment_and_runs_match(self):
        # Arrange
        parent = RootAsserter("first line\nrule1 -->|link label| rule2")
        link_asserter = LinkAsserter(parent)
        pattern = "l.*l"
        # Act
        result = link_asserter.matching_label(pattern)
        # Assert
        assert_that(result.augments).is_not_empty()
        assert_that(result.augments[0]).is_type_of(WithLabel)
        assert_that(result.context.reconstruct_buffer()).is_equal_to("rule1 -->|link label| rule2")
    def test_with_from_adds_WithLinkStart_augment_and_runs_match(self):
        # Arrange
        parent = RootAsserter("first line\nrule1 --> rule2")
        link_asserter = LinkAsserter(parent)
        id = "rule1"
        # Act
        result = link_asserter.with_from(id)
        # Assert
        assert_that(result.augments).is_not_empty()
        assert_that(result.augments[0]).is_type_of(WithLinkStart)
        assert_that(result.context.reconstruct_buffer()).is_equal_to("rule1 --> rule2")
    def test_matching_from_adds_WithLinkStart_augment_with_regex_and_runs_match(self):
        # Arrange
        parent = RootAsserter("first line\nrule1 --> rule2")
        link_asserter = LinkAsserter(parent)
        pattern = "r.*1"
        # Act
        result = link_asserter.matching_from(pattern)
        # Assert
        assert_that(result.augments).is_not_empty()
        assert_that(result.augments[0]).is_type_of(WithLinkStart)
        assert_that(result.context.reconstruct_buffer()).is_equal_to("rule1 --> rule2")
    def test_with_to_adds_WithLinkEnd_augment_and_runs_match(self):
        # Arrange
        parent = RootAsserter("first line\nrule1 --> rule2")
        link_asserter = LinkAsserter(parent)
        id = "rule2"
        # Act
        result = link_asserter.with_to(id)
        # Assert
        assert_that(result.augments).is_not_empty()
        assert_that(result.augments[0]).is_type_of(WithLinkEnd)
        assert_that(result.context.reconstruct_buffer()).is_equal_to("rule1 --> rule2")
    def test_matching_to_adds_WithLinkEnd_augment_with_regex_and_runs_match(self):
        # Arrange
        parent = RootAsserter("first line\nrule1 --> rule2")
        link_asserter = LinkAsserter(parent)
        pattern = "r.*2"
        # Act
        result = link_asserter.matching_to(pattern)
        # Assert
        assert_that(result.augments).is_not_empty()
        assert_that(result.augments[0]).is_type_of(WithLinkEnd)
        assert_that(result.context.reconstruct_buffer()).is_equal_to("rule1 --> rule2")
    def test_with_style_adds_WithLinkStyle_augment_and_runs_match(self):
        # Arrange
        parent = RootAsserter("first line\nrule1 --> rule2")
        link_asserter = LinkAsserter(parent)
        style = LINK_STYLE_NORMAL
        # Act
        result = link_asserter.with_style(style)
        # Assert
        assert_that(result.augments).is_not_empty()
        assert_that(result.augments[0]).is_type_of(WithLinkStyle)
        assert_that(result.context.reconstruct_buffer()).is_equal_to("rule1 --> rule2")
class TestMockAsserter:
    def test_match_always_returns_false(self):
        # Arrange
        mock_asserter = ContinuationAsserter(RootAsserter(), RootAsserter())
        # Act
        result = mock_asserter.match()
        # Assert
        assert_that(result).is_false()
    def test_message_returns_custom_message(self):
        # Arrange
        message = "Custom message"
        mock_asserter = mock_asserter = ContinuationAsserter(
            RootAsserter(), RootAsserter(), message
        )
        # Act
        result = mock_asserter.message()
        # Assert
        assert_that(result).is_equal_to(message)
    def test_extract_context_returns_target_context(self):
        # Arrange
        target = RootAsserter("line 1\nline 2\nline 3")
        mock_asserter = ContinuationAsserter(RootAsserter(), target)
        # Act
        extracted_context = mock_asserter.extract_context(target.context)
        # Assert
        assert_that(extracted_context).is_equal_to(target.context)
    def test_getattr_returns_wrapped_method_that_mocks_as_target_type(self):
        # Arrange
        target = LineAsserter(RootAsserter("\n\n"), "")
        target.match()
        mock_asserter = ContinuationAsserter(RootAsserter(), target)
        # Act
        result = mock_asserter.first
        # Assert
        assert callable(result)
        asserter = result()
        assert_that(asserter).is_instance_of(FirstAsserter)
        assert_that(asserter.parent).is_equal_to(mock_asserter)
class TestContinuationAsserter:
    # When using and_then asserter (A -> B -> and_then -> C), asserter C should use context of A
    # starting after B
    def test_subasserter_resumes_matching_aster_parent_match(self):
        # Arrange
        root = RootAsserter(sample_graph)
        asserter = GraphAsserter(root, direct_descendants_only=True)
        sut = GraphAsserter(asserter.and_then, direct_descendants_only=True)
        # Act
        asserter.match()
        sut.match()
        # Assert
        assert_that(asserter.context.reconstruct_buffer()).starts_with("subgraph A")
        assert_that(sut.context.reconstruct_buffer()).starts_with("subgraph B")
    # When using and_then asserter (A -> B -> and_then -> C) and C fails, then it should force to
    # reevaluate B and continue matching from next line (after current B)
    def test_when_subasserter_fails_it_should_force_asserter_to_reevaluate_from_its_current_position_and_continue_matching(
        self,
    ):
        # Arrange
        root = RootAsserter(sample_graph)
        asserter = GraphAsserter(root, direct_descendants_only=True)
        sut = GraphAsserter(asserter.and_then, direct_descendants_only=True)
        # Act
        asserter.match()
        with patch.object(sut, "_next_match", side_effect=[False, True]):
            sut.match()
        # Assert
        assert_that(asserter.context.reconstruct_buffer()).starts_with("subgraph B")
        assert_that(sut.context.reconstruct_buffer()).starts_with("subgraph C")
    def test_when_subasserter_fails_message_should_be_joined_correctly(
        self,
    ):
        # Arrange
        root = RootAsserter(sample_graph)
        asserter = GraphAsserter(root, direct_descendants_only=True)
        sut = LineAsserter(asserter.and_then, "B4")
        # Act
        assert_that(sut.match).raises(AssertionFailure).when_called_with().contains(
            "subgraph followed by line that matches"
        )
class TestFirstAsserter:
    def test_instantiation_with_valid_arguments(self):
        # Arrange
        parent = RootAsserter("line")
        # Act
        first_asserter = FirstAsserter(parent)
        # Assert
        assert_that(first_asserter).is_not_none()
        assert_that(first_asserter.parent).is_equal_to(parent)
    def test_message_method_returns_expected_message(self):
        # Arrange
        parent = RootAsserter("line")
        # Act
        first_asserter = FirstAsserter(parent)
        # Assert
        assert_that(first_asserter.message()).is_equal_to("[first element]")
    def test_match_when_match_exists_always_returns_first_match_as_context(self):
        # Arrange
        root = RootAsserter("line 1\nline 2\nline 3")
        parent = LineAsserter(root, "line")
        sut = FirstAsserter(parent)
        # Act
        sut.match()
        result = sut.match()
        # Assert
        assert_that(result).is_true()
        assert_that(sut.context.reconstruct_buffer()).is_equal_to("line 1")
    # With A -> B -> first -> C, when C fails (rematch parent is called) then B should force to re-evaluate A for next section
    def test_match_when_subasserter_fails_it_resets_parent_to_next_location(self):
        # Arrange
        root = GraphAsserter(RootAsserter(sample_graph), direct_descendants_only=True)
        parent = GraphAsserter(root, direct_descendants_only=True)
        sut = parent.first()
        sub = LineAsserter(sut, "B1")
        # Act
        sub.match()
        result = sut.match()
        # Assert
        assert_that(result).is_true()
        assert_that(sut.context.reconstruct_buffer().lstrip()).starts_with("subgraph B1")
class TestLastAsserter:
    def test_instantiation_with_valid_arguments(self):
        # Arrange
        parent = RootAsserter("line")
        # Act
        sut = LastAsserter(parent)
        # Assert
        assert_that(sut).is_not_none()
        assert_that(sut.parent).is_equal_to(parent)
    def test_message_method_returns_expected_message(self):
        # Arrange
        parent = RootAsserter("line")
        # Act
        sut = LastAsserter(parent)
        # Assert
        assert_that(sut.message()).is_equal_to("[last element]")
    def test_match_when_match_exists_always_returns_first_match_as_context(self):
        # Arrange
        root = RootAsserter("line 1\nline 2\nline 3")
        parent = LineAsserter(root, "line")
        sut = LastAsserter(parent)
        # Act
        sut.match()
        result = sut.match()
        # Assert
        assert_that(result).is_true()
        assert_that(sut.context.reconstruct_buffer()).is_equal_to("line 3")
    # With A -> B -> first -> C, when C fails (rematch parent is called) then B should force to re-evaluate A for next section
    def test_match_when_subasserter_fails_it_resets_parent_to_next_location(self):
        # Arrange
        root = GraphAsserter(RootAsserter(sample_graph), direct_descendants_only=True)
        parent = GraphAsserter(root, direct_descendants_only=True)
        sut = parent.last()
        sub = LineAsserter(sut, "B2")
        # Act
        sub.match()
        result = sut.match()
        # Assert
        assert_that(result).is_true()
        assert_that(sut.context.reconstruct_buffer().lstrip()).starts_with("subgraph B2")
class TestExactCountAsserter:
    def test_matches_exactly_expected_count(self):
        # Arrange
        parent = LineAsserter(RootAsserter(multi_line_text), "This is")
        parent.match()
        sut = ExactCountAsserter(parent, 6)
        # Assert
        assert_that(sut.match()).is_true()
    def test_matches_when_count_is_1(self):
        # Arrange
        parent = LineAsserter(RootAsserter(multi_line_text), "This is line 1")
        parent.match()
        sut = ExactCountAsserter(parent, 1)
        # Assert
        assert_that(sut.match()).is_true()
    @pytest.mark.parametrize("count", [-1, -2, 0, 1, 2, 5, 7])
    def test_fails_when_count_not_equal_to_number_of_matches(self, count):
        # Arrange
        parent = LineAsserter(RootAsserter(multi_line_text), "This is")
        parent.match()
        exact_count_asserter = ExactCountAsserter(parent, count)
        # Assert
        assert_that(exact_count_asserter.match(soft_fail=True)).is_false()
    def test_when_combined_with_augments_expect_correct_count(self):
        # Arrange
        parent = GraphAsserter(RootAsserter(sample_graph))
        # Act
        sut = parent.with_id("B").count(1)
        # Assert
        assert_that(sut.match()).is_true()
class TestMinCountAsserter:
    def test_match_with_min_count(self):
        # Arrange
        parent = LineAsserter(RootAsserter(multi_line_text), "line")
        sut = MinCountAsserter(parent, 2)
        # Act
        result = sut.match()
        # Assert
        assert_that(result).is_true()
    def test_match_with_less_than_min_count(self):
        # Arrange
        parent = LineAsserter(RootAsserter(multi_line_text), "line")
        sut = MinCountAsserter(parent, 10)
        # Act
        result = sut.match(soft_fail=True)
        # Assert
        assert_that(result).is_false()
class TestMaxCountAsserter:
    def test_match_with_min_count(self):
        # Arrange
        parent = LineAsserter(RootAsserter(multi_line_text), "line")
        sut = MaxCountAsserter(parent, 2)
        # Act
        result = sut.match(soft_fail=True)
        # Assert
        assert_that(result).is_false()
    def test_match_with_less_than_min_count(self):
        # Arrange
        parent = LineAsserter(RootAsserter(multi_line_text), "line")
        sut = MaxCountAsserter(parent, 10)
        # Act
        result = sut.match(soft_fail=True)
        # Assert
        assert_that(result).is_true()
    def test_parent_exists_and_is_None(self):
        # Arrange
        sut = RootAsserter("line")
        # Act
        result = hasattr(sut, "parent")
        # Assert
        assert_that(result).is_true()
        assert_that(sut.parent).is_none()
class TestCountableAsserter:
    @pytest.mark.parametrize("method", ["first", "last", "once"])
    def test_when_continued_uses_mock_as_self(self, method: str):
        # Arrange
        parent = RootAsserter("line")
        asserter = ContinuationAsserter(parent, LineAsserter(parent, "line"))
        # Act
        sut = asserter.__getattr__(method)()
        # Assert
        assert_that(sut.parent).is_not_none().is_instance_of(ContinuationAsserter)
    @pytest.mark.parametrize(
        "method", ["times", "count", "exactly", "min", "at_least", "max", "at_most"]
    )
    def test_parameterized_continuation_when_continued_uses_mock_as_self(self, method: str):
        # Arrange
        parent = RootAsserter("line")
        asserter = ContinuationAsserter(parent, LineAsserter(parent, "line"))
        # Act
        sut = asserter.__getattr__(method)(1)
        # Assert
        assert_that(sut.parent).is_not_none().is_instance_of(ContinuationAsserter)
================================================

File: test_assertions.py
================================================
from assertpy import assert_that
from tests.assertions import AsserterContext
================================================

File: test_augments.py
================================================
from unittest.mock import MagicMock
from assertpy import assert_that
import pytest
from firewall2mermaid.common import LINK_STYLE_BETWEEN_SECTIONS, LINK_STYLE_INVISIBLE
from tests.assertions.augments import (
    AtDepth,
    AtMaxDepth,
    AtMinDepth,
    IsCollapsed,
    WithDirection,
    WithId,
    WithLabel,
    AsserterContext,
    WithLinkEnd,
    WithLinkStart,
    WithLinkStyle,
    WithStyle,
    WithoutStyle,
)
class TestWithLabel:
    def test_match_returns_true_when_label_matches(self):
        # Arrange
        context = AsserterContext(["[test]"])
        augment = WithLabel("test")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_false_when_label_does_not_match(self):
        # Arrange
        context = AsserterContext(["[other]"])
        augment = WithLabel("test")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_match_returns_false_when_label_missing(self):
        # Arrange
        context = AsserterContext(["node"])
        augment = WithLabel("test")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_message_returns_expected_message(self):
        # Arrange
        augment = WithLabel("test")
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("label 'test'")
    def test_match_returns_true_when_label_matches_when_using_same_close_open_character(self):
        # Arrange
        context = AsserterContext(["|test|"])
        augment = WithLabel("test", "|", "|")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_true_when_label_matches_when_regex(self):
        # Arrange
        context = AsserterContext(["[a test123]"])
        augment = WithLabel(r"test\d", reg_ex=True)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_false_when_label_does_not_match_when_regex(self):
        # Arrange
        context = AsserterContext(["[other]"])
        augment = WithLabel(r"test\d+", reg_ex=True)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_message_returns_expected_message_when_regex(self):
        # Arrange
        augment = WithLabel(r"test\d+", reg_ex=True)
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("label matching 'test\\d+'")
    def test_match_returns_true_when_label_matches_when_using_same_close_open_character_when_regex(
        self,
    ):
        # Arrange
        context = AsserterContext(["|test123|"])
        augment = WithLabel(r"test\d+", "|", "|", reg_ex=True)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
class TestWithStyle:
    def test_match_returns_true_when_style_matches(self):
        # Arrange
        context = AsserterContext([":::bold"])
        augment = WithStyle("bold")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_false_when_style_does_not_match(self):
        # Arrange
        context = AsserterContext([":::italic"])
        augment = WithStyle("bold")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_message_returns_expected_message_with_style(self):
        # Arrange
        augment = WithStyle("italic")
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("style 'italic'")
class TestWithoutStyle:
    def test_match_returns_true_when_no_style_present(self):
        # Arrange
        context = AsserterContext(["Some line without style"])
        augment = WithoutStyle()
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_true_when_style_does_not_match(self):
        # Arrange
        context = AsserterContext(["Some line with style:::bold"])
        augment = WithoutStyle("italic")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_false_when_style_matches(self):
        # Arrange
        context = AsserterContext([":::bold"])
        augment = WithoutStyle("bold")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_message_returns_expected_message_with_style(self):
        # Arrange
        augment = WithoutStyle("italic")
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("no style matching 'italic'")
    def test_message_returns_expected_message_without_style(self):
        # Arrange
        augment = WithoutStyle()
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("no styles")
class TestWithId:
    @pytest.mark.parametrize(
        "case", ["test_id[label]", "node test_id[label]", "node test_id [label]"]
    )
    def test_match_returns_true_when_id_matches(self, case):
        # Arrange
        context = AsserterContext([case])
        augment = WithId("test_id")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_when_have_node_type_returns_true_when_id_matches(self):
        # Arrange
        context = AsserterContext(["nodetype nodeid"])
        augment = WithId("nodeid")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    @pytest.mark.parametrize(
        "case", ["test_id[label]", "node test_id[label]", "node test_id [label]"]
    )
    def test_match_returns_true_when_id_matches_when_using_regex(self, case):
        # Arrange
        context = AsserterContext([case])
        augment = WithId(".*id", use_regex=True)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_when_have_node_type_returns_true_when_id_matches_when_using_Regex(self):
        # Arrange
        context = AsserterContext(["nodetype nodeid"])
        augment = WithId(".*id", use_regex=True)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_false_when_id_does_not_match(self):
        # Arrange
        context = AsserterContext(["node"])
        augment = WithId("test_id")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_message_returns_expected_message(self):
        # Arrange
        augment = WithId("test_id")
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("id 'test_id'")
class TestWithDirection:
    def test_match_returns_true_when_direction_matches(self):
        # Arrange
        context = AsserterContext(["direction right"])
        augment = WithDirection("right")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_false_when_direction_does_not_match(self):
        # Arrange
        context = AsserterContext(["direction left"])
        augment = WithDirection("right")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_match_returns_false_when_direction_not_found(self):
        # Arrange
        context = AsserterContext(["a sample line. right"])
        augment = WithDirection("right")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_message_returns_expected_message(self):
        # Arrange
        augment = WithDirection("right")
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("direction 'right'")
class TestAtDepth:
    def test_match_returns_true_when_depth_matches(self):
        # Arrange
        context = AsserterContext(["\t" * 3 + "Some line"])
        augment = AtDepth(3)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_false_when_depth_does_not_match(self):
        # Arrange
        context = AsserterContext(["\t" * 2 + "Some line"])
        augment = AtDepth(3)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_message_returns_expected_message(self):
        # Arrange
        augment = AtDepth(3)
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("at depth of 3")
class TestAtMinDepth:
    def test_match_returns_true_when_depth_is_greater_than_or_equal_to_level(self):
        # Arrange
        context = AsserterContext(["\t" * 3 + "Some line"])
        augment = AtMinDepth(3)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_false_when_depth_is_less_than_level(self):
        # Arrange
        context = AsserterContext(["\t" * 2 + "Some line"])
        augment = AtMinDepth(3)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_message_returns_expected_message(self):
        # Arrange
        augment = AtMinDepth(3)
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("at minimum depth of 3")
class TestAtMaxDepth:
    def test_match_returns_true_when_depth_is_less_than_or_equal_to_level(self):
        # Arrange
        context = AsserterContext(["\t" * 3 + "Some line"])
        augment = AtMaxDepth(3)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_false_when_depth_is_greater_than_level(self):
        # Arrange
        context = AsserterContext(["\t" * 4 + "Some line"])
        augment = AtMaxDepth(3)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_message_returns_expected_message(self):
        # Arrange
        augment = AtMaxDepth(3)
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("at maximum depth of 3")
class TestWithLinkStyle:
    def test_match_returns_true_when_style_matches(self):
        # Arrange
        context = AsserterContext([f"from {LINK_STYLE_BETWEEN_SECTIONS} to"])
        augment = WithLinkStyle(LINK_STYLE_BETWEEN_SECTIONS)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_false_when_style_does_not_match(self):
        # Arrange
        context = AsserterContext([f"from {LINK_STYLE_INVISIBLE} to"])
        augment = WithLinkStyle(LINK_STYLE_BETWEEN_SECTIONS)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_match_returns_false_when_link_not_found(self):
        # Arrange
        context = AsserterContext([f"rule1 [label]"])
        augment = WithLinkStyle(LINK_STYLE_BETWEEN_SECTIONS)
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_message_returns_expected_message(self):
        # Arrange
        augment = WithLinkStyle(LINK_STYLE_BETWEEN_SECTIONS)
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to(f"link style '{LINK_STYLE_BETWEEN_SECTIONS}'")
class TestWithLinkStart:
    def test_match_returns_true_when_start_matches_pattern(self):
        # Arrange
        context = AsserterContext(["start --> end"])
        augment = WithLinkStart("start")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_false_when_start_does_not_match_pattern(self):
        # Arrange
        context = AsserterContext(["other --> end"])
        augment = WithLinkStart("start")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_message_returns_expected_message(self):
        # Arrange
        augment = WithLinkStart("start")
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("from 'start'")
    def test_message_returns_expected_message_when_using_regex(self):
        # Arrange
        context = AsserterContext(["start --> end"])
        augment = WithLinkStart("start", use_regex=True)
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("from matching 'start'")
class TestWithLinkEnd:
    def test_match_returns_true_when_end_matches_pattern(self):
        # Arrange
        context = AsserterContext(["start --> test"])
        augment = WithLinkEnd("test")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    def test_match_returns_false_when_end_does_not_match_pattern(self):
        # Arrange
        context = AsserterContext(["start --> other"])
        augment = WithLinkEnd("test")
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_message_returns_expected_message(self):
        # Arrange
        augment = WithLinkEnd("test")
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("to 'test'")
    def test_message_returns_expected_message_when_using_regex(self):
        # Arrange
        augment = WithLinkEnd("test", use_regex=True)
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("to matching 'test'")
class TestIsCollapsed:
    def test_match_returns_true_when_context_is_collapsed(self):
        # Arrange
        context = AsserterContext(["subgraph X", "end"])
        augment = IsCollapsed()
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_true()
    @pytest.mark.parametrize("context", [["subgraph X"], ["subgraph X", "end", "extra line"]])
    def test_match_returns_false_when_context_is_not_collapsed(self, context):
        # Arrange
        context = AsserterContext(context)
        augment = IsCollapsed()
        # Act
        result = augment.match(context)
        # Assert
        assert_that(result).is_false()
    def test_message_returns_expected_message(self):
        # Arrange
        augment = IsCollapsed()
        # Act
        result = augment.message()
        # Assert
        assert_that(result).is_equal_to("that is collapsed")
================================================

File: test___init__.py
================================================
import unittest
from unittest.mock import MagicMock, patch
from assertpy import assert_that
from tests.assertions import (
    AsserterBase,
    AsserterContext,
    AssertionFailure,
    AugmentBase,
)
from tests.assertions.asserters import RootAsserter
class DummyAsserter(AsserterBase):
    def __init__(self, parent: AsserterBase):
        super().__init__(parent)
    def _next_match(self, context: AsserterContext) -> bool:
        return True
    def extract_context(self, context: AsserterContext) -> AsserterContext:
        return context
    def message(self):
        return "Dummy message"
class DummyAugment(AugmentBase):
    def match(self, context: AsserterContext):
        return True
    def message(self):
        return "Dummy augment message"
class TestAsserterContext:
    def test_eq_returns_true_for_equal_objects(self):
        # Arrange
        context1 = AsserterContext(["line 1", "line 2", "line 3"])
        context1.index = 1
        context1.depth = 2
        context2 = AsserterContext(["line 1", "line 2", "line 3"])
        context2.index = 1
        context2.depth = 2
        # Assert
        assert_that(context1).is_equal_to(context2)
    def test_eq_returns_false_for_unequal_objects(self):
        # Arrange
        context1 = AsserterContext(["line 1", "line 2", "line 3"])
        context1.index = 1
        context1.depth = 2
        context2 = AsserterContext(["line 1", "line 2", "line 3"])
        context2.index = 0
        context2.depth = 2
        # Assert
        assert_that(context1).is_not_equal_to(context2)
    def test_eq_returns_false_for_objects_of_different_types(self):
        # Arrange
        context1 = AsserterContext(["line 1", "line 2", "line 3"])
        context1.index = 1
        context1.depth = 2
        other = "not a context object"
        # Assert
        assert_that(context1).is_not_equal_to(other)
    def test_current_line_returns_current_line(self):
        # Arrange
        context = AsserterContext(["line 1", "line 2", "line 3"])
        context.index = 1
        # Assert
        assert_that(context.current_line()).is_equal_to("line 2")
    def test_current_line_returns_none_when_buffer_end_is_reached(self):
        # Arrange
        context = AsserterContext(["line 1", "line 2", "line 3"])
        context.index = 3
        # Assert
        assert_that(context.current_line()).is_none()
    def test_next_line_moves_to_next_line(self):
        # Arrange
        context = AsserterContext(["line 1", "line 2", "line 3"])
        context.index = 1
        # Assert
        assert_that(context.next_line()).is_equal_to("line 3")
        assert_that(context.index).is_equal_to(2)
    def test_next_line_returns_none_at_buffer_end(self):
        # Arrange
        context = AsserterContext(["line 1", "line 2"])
        context.index = 1
        # Assert
        assert_that(context.next_line()).is_none()
        assert_that(context.index).is_equal_to(2)
    def test_peek_next_line_returns_next_line(self):
        # Arrange
        context = AsserterContext(["line 1", "line 2", "line 3"])
        context.index = 1
        # Assert
        assert_that(context.peek_next_line()).is_equal_to("line 3")
        assert_that(context.index).is_equal_to(1)
    def test_peek_next_line_returns_none_at_buffer_end(self):
        # Arrange
        context = AsserterContext(["line 1", "line 2", "line 3"])
        context.index = 2
        # Assert
        assert_that(context.peek_next_line()).is_none()
    def test_has_line_returns_true_when_index_less_than_buffer_length(self):
        # Arrange
        context = AsserterContext(["line 1", "line 2", "line 3"])
        context.index = 2
        # Assert
        assert_that(context.has_line()).is_true()
    def test_has_line_returns_false_when_index_equal_to_buffer_length(self):
        # Arrange
        context = AsserterContext(["line 1", "line 2", "line 3"])
        context.index = 3
        # Assert
        assert_that(context.has_line()).is_false()
    def test_has_line_returns_false_when_index_greater_than_buffer_length(self):
        # Arrange
        context = AsserterContext(["line 1", "line 2", "line 3"])
        context.index = 4
        # Assert
        assert_that(context.has_line()).is_false()
    def test_has_next_line_returns_true_when_buffer_has_next_line(self):
        # Arrange
        context = AsserterContext(["line 1", "line 2", "line 3"])
        context.index = 1
        # Assert
        assert_that(context.has_next_line()).is_true()
    def test_has_next_line_returns_false_when_buffer_end_is_reached(self):
        # Arrange
        context = AsserterContext(["line 1", "line 2", "line 3"])
        context.index = 3
        # Assert
        assert_that(context.has_next_line()).is_false()
    def test_copy_method_returns_new_context_with_same_properties(self):
        # Arrange
        context = AsserterContext(["line 1", "line 2", "line 3"])
        context.index = 1
        # Act
        copied_context = context.copy()
        # Assert
        assert_that(copied_context).is_not_same_as(context)
        assert_that(copied_context.buffer).is_equal_to(context.buffer)
        assert_that(copied_context.index).is_equal_to(context.index)
class TestAsserterBase(unittest.TestCase):
    def test_fail_raises_assertion_failure_with_message_from_asserter(self):
        # Arrange
        asserter = DummyAsserter(RootAsserter(""))
        # Act
        assert_that(asserter.fail).raises(AssertionFailure).when_called_with().contains(
            "AssertionFailure: Unable to find Dummy message"
        )
    def test_fail_raises_assertion_failure_with_message_from_augment_when_augments_present(self):
        # Arrange
        asserter = DummyAsserter(RootAsserter(""))
        asserter.add_augment(DummyAugment(), match=False)
        # Act
        assert_that(asserter.fail).raises(AssertionFailure).when_called_with().contains(
            "Dummy augment message"
        )
    def test_when_augment_fails_continue_searching_for_next_node(self):
        # Arrange
        asserter = DummyAsserter(RootAsserter(""))
        augment = DummyAugment()
        asserter.add_augment(augment, match=False)
        # Act
        with patch.object(augment, "match", side_effect=[False, True]):
            found = asserter._find_next_match(AsserterContext([]))
        # Assert
        assert_that(found).is_true()
    def test_when_augment_fails_after_being_added_it_should_force_parent_to_rematch(self):
        # Arrange
        asserter = DummyAsserter(RootAsserter(""))
        asserter.match = MagicMock(name="match")  # type: ignore
        asserter.last_match = MagicMock(name="last_match", return_value=1)  # type: ignore
        asserter.context = MagicMock(name="context")  # type: ignore
        augment = DummyAugment()
        # Act
        with patch.object(augment, "match", side_effect=[False, True]):
            asserter.add_augment(augment)
        # Assert
        asserter.match.assert_called_once()
================================================

File: __init__.py
================================================
from __future__ import annotations
from abc import abstractmethod
from typing import Any, Generic, TypeVar
from typing_extensions import Self
from typing import TypeVar, Generic
import re
from typing import Optional
TParent = TypeVar("TParent", bound="AsserterBase")
TAsserter = TypeVar("TAsserter", bound="AsserterBase")
TMock = TypeVar("TMock", bound="AsserterBase")
SHAPE_STYLES = {
    "default": ("[", "]"),
    "round": ("(", ")"),
    "stadium": ("([", "])"),
    "subroutine": ("[[", "]]"),
    "cylindrical": ("[(", ")]"),
    "circle": ("((", "))"),
    "asymetric": (">", "]"),
    "node": ("{", "}"),
    "hexagon": ("{{", "}}"),
    "parallelogram": ("[/", "/]"),
    "parallelogram_alt": ("[\\", "\\]"),
    "trapezoid": ("[/", "\\]"),
    "trapezoid_alt": ("[\\", "/]"),
    "doublecircle": ("(((", ")))"),
}
def line_depth(line: str) -> int:
    return len(line) - len(line.lstrip("\t"))
class AssertionFailure(BaseException):
    """Exception for assertion failures."""
    def __init__(self, message: str, prefix: str = "AssertionFailure: Unable to find "):
        self.message = message
        self.prefix = prefix
    def __str__(self):
        return f"{self.prefix}{self.message}"
class AssertionError(BaseException):
    """Exception for generic assertion errors."""
    def __init__(self, message: str, prefix: str = "AssertionError: "):
        self.message = message
        self.prefix = prefix
    def __str__(self):
        return f"{self.prefix}{self.message}"
class AsserterContext:
    """Context for asserter operations."""
    def __init__(self, buffer: list[str]) -> None:
        self.buffer = buffer
        """The buffer to search in."""
        self.index = 0
        """Current line index in the buffer."""
        self.depth = line_depth(buffer[0]) if buffer else 0
        """Depth of the current context"""
    def reconstruct_buffer(self) -> str:
        return "\n".join(self.buffer)
    def current_line(self) -> str | None:
        """Get the current line from the context.
        Returns:
            str|None: The current line or None if buffer end is reached.
        """
        return self.buffer[self.index] if self.index < len(self.buffer) else None
    def next_line(self) -> str | None:
        """Move to the next line in the context.
        Returns:
            str|None: The next line or None if buffer end is reached.
        """
        if self.has_next_line():
            self.index += 1
        else:
            self.index = len(self.buffer)
        return self.current_line()
    def peek_next_line(self) -> str | None:
        """Obtains the next line without advancing the index.
        Returns:
            str|None: Next line in buffer or None if the buffer end is reached.
        """
        return self.buffer[self.index + 1] if self.has_next_line() else None
    def has_line(self) -> bool:
        """Checks if the buffer has a current line.
        Returns:
            bool: True if the current line exists in the buffer (might be still None), False otherwise
        """
        return self.index < len(self.buffer)
    def has_next_line(self) -> bool:
        """Checks if the buffer has a next line.
        Returns:
            bool: True if at least one more line exists in the buffer. False, if the buffer end
            is/will be reached during the next call to next_line.
        """
        return self.index < len(self.buffer) - 1
    def copy(self) -> AsserterContext:
        context = AsserterContext(self.buffer)
        context.index = self.index
        return context
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AsserterContext):
            return False
        return (
            self.buffer == other.buffer and self.index == other.index and self.depth == other.depth
        )
    def __len__(self):
        return len(self.buffer)
class AsserterRootContext(AsserterContext):
    """Context for the root asserter."""
    def __init__(self, buffer: str):
        super().__init__(buffer.splitlines())
        self.graph = buffer
        self.depth = -1
    def next_line(self):
        return self.current_line()
    def peek_next_line(self):
        return self.current_line()
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AsserterRootContext):
            return False
        return super().__eq__(other)
class AsserterBase(Generic[TParent]):
    """Base class for asserters."""
    def __init__(self, parent: TParent):
        self._creation_asserter: TParent | None = None
        self.parent: TParent = parent
        self.context: AsserterContext
        self.last_match: int | None = None
        """Last match index in the parent context (heystack). Used for re-matching."""
        self.augments: list[AugmentBase] = []
    def _get_creation_asserter(self) -> Self:
        if self._creation_asserter:
            return self._creation_asserter  # type: ignore
        return self
    def _init_matching_context(self) -> AsserterContext:
        from tests.assertions.asserters import ContinuationAsserter
        context = self.parent.context.copy()
        # if parent is ContinuationAsserter asserter we need to calculate the first index past the first match
        if self.last_match is not None:
            context.index = self.last_match + 1
        elif isinstance(self.parent, ContinuationAsserter):
            # need to adjust the start index to be after the last match of the parent + its context size
            context.index = (self.parent.last_match or 0) + len(self.parent.parent.context)
        return context
    def match(self, soft_fail: bool = False, propagate=True) -> bool:
        """Finds the next match in the context for the current asserter. If a match isn't found in
        the current context it will call the parent asserter to advance its context and will try
        again.
        Args:
            soft_fail (bool, optional): When set to True will call fail method which will raise
                AssertionFailure error. If set to false it will return False instead. Defaults to False.
            rematch_parent (bool, optional): When set to True will attempt to return the matcher in
            the the parent asserter and try again
                asserter. Defaults to True.
        Returns:
            bool: True if a match is found, False otherwise
        """
        # match parent if needed
        from tests.assertions.asserters import RootAsserter
        if not isinstance(self.parent, RootAsserter) and self.parent.last_match is None:
            self.parent.match()
        # loop instead of calling match again to keep
        heystack: Optional[AsserterContext] = None
        while True:
            if not heystack:
                heystack = self._init_matching_context()
            if not heystack.has_line():
                break
            if self._find_next_match(heystack):
                self.last_match = heystack.index
                self.context = self.extract_context(heystack)
                return True
            if propagate:
                # parent found a new match, re-match
                if self.parent.match(True, propagate):
                    heystack = None
                    self.last_match = None
                    continue
            # exit after matching failing ot match and/or propagate
            break
        return False if soft_fail else self.fail()
    def _find_next_match(self, context: AsserterContext) -> bool:
        """Find the next match in the context for the current parent asserter.
        Args:
            context (AsserterContext): The context to search in.
        Returns:
            bool: True if a match is found, False otherwise.
        """
        while True:
            if not self._next_match(context):
                return False
            augment_context = self.extract_context(context.copy())
            if self._match_augments(augment_context):
                return True
            context.next_line()
    def _match_augments(self, context: AsserterContext) -> bool:
        for augment in self.augments:
            if not augment.match(context.copy()):
                return False
        return True
    @abstractmethod
    def _next_match(self, context: AsserterContext) -> bool:
        """Implement the logic to check for the next match in the context.
        Returns:
            bool: True if a match is found, False otherwise.
        """
        raise NotImplementedError()
    def fail(self, message: str = ""):
        """Raise an AssertionFailure with a formatted error message.
        Args:
            message (str): The error message. Defaults to an empty string.
        """
        chain = self._parents()
        chain.append(self)
        message = ""
        root = chain[0]
        for asserter in chain[1:]:
            message_part = self._get_asserter_message(asserter)
            if (
                message
                and message_part
                and asserter.join_message()
                and not isinstance(asserter.parent, ContinuationAsserter)
            ):
                message_part = f"{asserter.join_message()} {message_part}"
            if message_part:
                message += f" {message_part}"
        raise AssertionFailure(message.lstrip() + " " + root.message())
    def _get_asserter_message(self, asserter: AsserterBase) -> str:
        message = asserter.message()
        if len(asserter.augments) > 0:
            message += " with " + ", ".join([augment.message() for augment in asserter.augments])
        return message
    @abstractmethod
    def extract_context(self, parent_context: AsserterContext) -> AsserterContext:
        """Sets the context after a successful rematch from the parent asserter (to propagate down)."""
        raise NotImplementedError()
    def _parents(self) -> list[AsserterBase[Any]]:
        """Retrieve a list of parent nodes in declared order.
        Returns:
            list[BaseAsserter[Any]]: A list containing parent nodes in declared order
        """
        parents: list[AsserterBase] = []
        p = self.parent
        while True:
            parents.append(p)
            p = p.parent
            if not p:
                break
        parents.reverse()
        return parents
    @abstractmethod
    def message(self) -> str:
        """Define the template for the error message.
        Returns:
            str: The error message template.
        """
        raise NotImplementedError()
    def join_message(self) -> str:
        return "that contains"
    def add_augment(self, augment: AugmentBase, match: bool = True) -> AugmentBase:
        self.augments.append(augment)
        if match:
            if self.last_match is None or not augment.match(self.context):
                self.match()
        return augment
    def at_depth(self, level: int) -> Self:
        from tests.assertions.augments import AtDepth
        self.add_augment(AtDepth(level))
        return self
    def at_min_depth(self, level: int) -> Self:
        from tests.assertions.augments import AtMinDepth
        self.add_augment(AtMinDepth(level))
        return self
    def at_max_depth(self, level: int) -> Self:
        from tests.assertions.augments import AtMinDepth
        self.add_augment(AtMinDepth(level))
        return self
class AugmentBase:
    @abstractmethod
    def match(self, context: AsserterContext) -> bool:
        raise NotImplementedError()
    @abstractmethod
    def message(self) -> str:
        raise NotImplementedError()
from tests.assertions.asserters import ContinuationAsserter, RootGraphAsserter
def assert_graph(graph: str) -> RootGraphAsserter:
    """Factory function to create a RootGraphAsserter instance."""
    return RootGraphAsserter(graph)
================================================

File: conftest.py
================================================
from typing import Any, Callable
import pytest
from firewall2mermaid.common import FIREWALL_LINE_START, create_adhoc_rule
from firewall2mermaid.model import ParserRule, RootNode, Rule
from firewall2mermaid.parser import parse_rule
from firewall2mermaid.tree import TreeMaker
def _parser_rule_line_factory(section: str, chain: str, **kwargs: str) -> str:
    attrs_line = ""
    if kwargs:
        for key in kwargs.keys():
            if " " in kwargs[key] and not str(kwargs[key]).startswith('"'):
                kwargs[key] = f'"{kwargs[key]}"'
        attrs_line = " ".join([f"{key}={kwargs[key]}" for key in kwargs])
    return f"{FIREWALL_LINE_START} {section} add chain={chain} {attrs_line}"
def _parser_rule_factory(section: str, chain: str, **kwargs: str) -> ParserRule:
    return parse_rule(_parser_rule_line_factory(section, chain, **kwargs))
def _rule_factory(section: str, chain: str, index: int, **kwargs: str) -> Rule:
    return create_adhoc_rule(section, chain, index, **kwargs)
@pytest.fixture
def parser_rule_line_factory() -> Callable[[str, str], str]:
    return _parser_rule_line_factory
@pytest.fixture
def parser_rule_factory() -> Callable[[str, str], ParserRule]:
    return _parser_rule_factory
@pytest.fixture
def rule_factory() -> Callable[[str, str, int], Rule]:
    return _rule_factory
@pytest.fixture
def single_filter_input_rule(parser_rule_factory: Callable[..., ParserRule]) -> ParserRule:
    return parser_rule_factory("filter", "input")
@pytest.fixture
def default_rule_list(parser_rule_factory: Callable[..., ParserRule]) -> list[ParserRule]:
    return [
        # prerouting
        parser_rule_factory(
            "raw", "prerouting", action="fasttrack-connection", comment="fasttrack"
        ),
        parser_rule_factory(
            "mangle", "prerouting", action="fasttrack-connection", comment="fasttrack"
        ),
        parser_rule_factory("nat", "dstnat", action="fasttrack-connection", comment="fasttrack"),
        # input
        parser_rule_factory(
            "mangle", "input", action="fasttrack-connection", disabled="no", comment="fasttrack"
        ),
        parser_rule_factory(
            "mangle", "input", action="accept", comment="disabled rule", disabled="yes"
        ),
        parser_rule_factory("filter", "input", action="fasttrack-connection", comment="fasttrack"),
        parser_rule_factory(
            "filter", "input", action="log", comment="log rule", log_prefix="filter"
        ),
        parser_rule_factory(
            "filter",
            "input",
            action="jump",
            comment="jump",
            jump_target="terminal-chain",
            src_address="192.168.0.0",
        ),
        parser_rule_factory("filter", "input", action="drop", comment="drop all"),
        # forward
        parser_rule_factory(
            "mangle", "forward", action="fasttrack-connection", comment="fasttrack"
        ),
        parser_rule_factory(
            "mangle", "forward", action="accept", comment="disabled rule", disabled="yes"
        ),
        parser_rule_factory(
            "filter", "forward", action="fasttrack-connection", comment="fasttrack"
        ),
        parser_rule_factory(
            "filter", "forward", action="log", comment="log rule", log_prefix="filter"
        ),
        parser_rule_factory(
            "filter", "forward", action="jump", comment="jump", jump_target="terminal-chain"
        ),
        parser_rule_factory(
            "filter", "forward", action="jump", comment="jump", jump_target="jump-chain"
        ),
        parser_rule_factory("filter", "forward", action="drop", comment="drop all"),
        # output
        parser_rule_factory("raw", "output", action="fasttrack-connection", comment="fasttrack"),
        parser_rule_factory("mangle", "output", action="fasttrack-connection", comment="fasttrack"),
        parser_rule_factory("filter", "output", action="fasttrack-connection", comment="fasttrack"),
        # postrouting
        parser_rule_factory(
            "mangle", "postrouting", action="fasttrack-connection", comment="fasttrack"
        ),
        parser_rule_factory("nat", "srcnat", action="fasttrack-connection", comment="fasttrack"),
        # terminal chain
        parser_rule_factory(
            "filter",
            "terminal-chain",
            action="drop",
            src_address="192.168.0.0",
            comment="drop if src matches",
        ),
        # jump chains
        parser_rule_factory("filter", "jump-chain", action="return", src_address="10.0.0.0"),
        parser_rule_factory(
            "filter",
            "jump-chain",
            action="accept",
            comment="jump target",
            src_address="192.168.0.0",
        ),
        parser_rule_factory("raw", "jump-chain", action="accept", comment="jump target"),
        parser_rule_factory("filter", "terminal-chain", action="drop", comment="drop all"),
        # disabled chain
        parser_rule_factory("filter", "disabled-chain", action="drop", disabled="yes"),
        # log chain
        parser_rule_factory("filter", "log-chain", action="log"),
        # rule order chain
        parser_rule_factory("filter", "rule-order", comment="1"),
        parser_rule_factory("filter", "rule-order", comment="2"),
        parser_rule_factory("filter", "rule-order", comment="3"),
        parser_rule_factory("filter", "rule-order", comment="4"),
    ]
@pytest.fixture
def add_flow_rule_list(parser_rule_factory: Callable[..., ParserRule]) -> list[ParserRule]:
    return [
        parser_rule_factory("filter", "input", action="fasttrack-connection", comment="fasttrack"),
        parser_rule_factory("nat", "srcnat", action="masquerade", comment="masquerade"),
        parser_rule_factory("nat", "dstnat", action="dst-nat", comment="dstnat"),
        parser_rule_factory("raw", "prerouting", action="accept", comment="raw"),
    ]
@pytest.fixture
def rule_list_ordered_tests() -> list[ParserRule]:
    return [
        parse_rule("/ip firewall filter add chain=input comment=0"),
        parse_rule("/ip firewall filter add chain=input comment=1"),
        parse_rule("/ip firewall filter add chain=output comment=2"),
        parse_rule("/ip firewall raw add chain=input comment=3"),
        parse_rule("/ip firewall raw add chain=input comment=4"),
        parse_rule("/ip firewall raw add chain=output comment=5"),
    ]
@pytest.fixture
def default_tree_root(default_rule_list: list[ParserRule]) -> RootNode:
    return TreeMaker(default_rule_list, []).make_tree()
known_rule_attributes = set(
    [
        "action",
        "address-list-timeout",
        "chain",
        "comment",
        "connection-bytes",
        "connection-limit",
        "connection-mark",
        "connectio-rate",
        "connection-state",
        "connection-type",
        "content",
        "dscp",
        "dst-address",
        "dst-address-list",
        "dst-address-type",
        "dst-limit",
        "dst-port",
        "fragment",
        "hotspot",
        "icmp-options",
        "in-bridge-port",
        "in-bridge-port-list",
        "in-interface",
        "in-interface-list",
        "ingress-priority",
        "ipsec-policy",
        "ipv4-options",
        "jump-target",
        "layer7-protocol",
        "log-prefix",
        "nth",
        "new-connection-mark",
        "new-dscp",
        "new-mss",
        "new-packet-mark",
        "new-priority",
        "new-routing-mark",
        "new-ttl",
        "out-bridge-port",
        "out-bridge-port-list",
        "out-interface",
        "out-interface-list",
        "packet-mark",
        "packet-size",
        "per-connection-classifier",
        "port",
        "protocol",
        "psd",
        "random",
        "reject-with",
        "routing-table",
        "routing-mark",
        "src-address",
        "src-address-list",
        "src-address-type",
        "src-port",
        "src-mac-address",
        "tcp-flags",
        "tcp-mss",
        "time",
        "tls-host",
        "ttl",
    ]
)
known_rule_attributes_for_generation = known_rule_attributes - set(["chain"])
terminal_actions = set(["drop", "accept", "reject", "tarpit"])
rule_matching_attributes = set(known_rule_attributes).difference(
    {"action", "comment", "chain", "log-prefix", "log", "jump-target"}
)
# asserter tests
@pytest.fixture
def sample_graph_text():
    return """
%%{init: {'flowchart': {'htmlLabels': false}, 'theme': 'dark'}}%%
flowchart TB
classDef fasttrack-connection fill:#686d6d
classDef log fill:#686d6d
classDef drop fill:#8c2c61
subgraph root
	direction TB
	subgraph legend
		direction TB
		subgraph legend-legend
			direction TB
			rule7[*fasttrack-connection]:::fasttrack-connection
			rule8[*log]:::log
			rule9[*drop]:::drop
		end
	end
	subgraph filter [filter]
		direction TB
		subgraph filter-input [input]
			direction TB
			rule1[*fasttrack]:::fasttrack-connection
			rule2[*log rule]:::log
			rule3[*drop all]:::drop
		end
		subgraph filter-forward [forward]
			direction TB
			rule4[*fasttrack]:::fasttrack-connection
			rule5[*log rule]:::log
			rule6[*drop all]:::drop
		end
	end
end
%% Relationships
filter:input:1 --> filter:input:2
filter:input:2 --> filter:input:3
filter:forward:4 --> filter:forward:5
filter:forward:5 --> filter:forward:6
"""
================================================

File: mermaid.py
================================================
import logging
import re
from pytest import Parser
CHART_TYPES = ["flowchart"]
class AstParsingException(BaseException):
    def __init__(self, message: str):
        self.message = f"Parsing exception: {message}"
        super().__init__(self.message)
class Node:
    def __init__(self):
        self.type = type(self)
        self.children: list[Node] = []
    def __str__(self):
        return f"[{self.type}]"
    def add_child(self, node):
        self.children.append(node)
        return node
class CommentNode(Node):
    def __init__(self, comment: str, multiline=False):
        self.comment = comment
        self.multiline = multiline
    def __str__(self):
        text = self.comment.replace("\n", "")
        return f"[{self.type}=>multiline: {str(self.multiline)}, comment: {text}]"
class RootNode(Node):
    pass
class EmptyNode(Node):
    pass
class ChartTypeNode(Node):
    def __init__(self, type: str = "flowchart", direction: str | None = None):
        self.direction = direction
        self.chart_type = type
    def __str__(self):
        text = f"[{self.type}=>type: {self.chart_type}"
        if self.direction:
            text += f", direction: {self.direction}"
        return text + "]"
class GraphNode(Node):
    def __init__(self, id: str, label: str | None = None):
        self.id = id
        self.label = label
    def __str__(self):
        text = f"[{self.type}=>type: {self.id}"
        if self.label:
            text += f", label: {self.label}"
        return text + "]"
class ClassDefNode(Node):
    def __init__(self, name: str, styles: dict[str, str]):
        self.name = name
        self.styles = styles
    def __str__(self):
        styles = ", ".join([f"{key}:{value}" for key, value in self.styles.items()])
        if styles:
            styles = ", " + styles
        return f"[{self.type}=>{self.name}{styles}]"
class DirectionNode(Node):
    def __init__(self, direction: str):
        self.direction = direction
    def __str__(self):
        return f"[{self.type}=>direction: {self.direction}]"
class EndNode(Node):
    pass
class RuleNode(Node):
    def __init__(self, id: str, label: str | None, classname: str | None):
        self.id = id
        self.label = label
        self.classname = classname
    def __str__(self):
        text = f"[{self.type}=>id: {self.id}"
        if self.label:
            text += f", label: {self.label}"
        if self.classname:
            text += f", classname: {self.classname}"
        return text + "]"
class RelationshipNode(Node):
    def __init__(self, start: str, end: str, label: str | None, style: str):
        self.start = start
        self.label = label
        self.style = style
        self.end = end
    def __str__(self):
        text = f"[{self.type}=>form: {self.start}, to: {self.end}, style: {self.style}"
        if self.label:
            text += f", label: {self.label}"
        return text + "]"
class ParserContext:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.lines = text.splitlines()
    def current(self):
        return self.lines[self.index]
    def next(self):
        if not self.has_next():
            return None
        self.index += 1
        return self.current()
    def peek(self):
        if not self.has_next():
            return None
        return self.lines[self.index + 1]
    def has_next(self):
        return self.index < len(self.lines)
class MermaidAstParser:
    def parse(self, text: str):
        context = ParserContext(text)
        root = RootNode()
        for node in self.parse_node(context):
            root.add_child(node)
        return root
    def parse_node(self, context: ParserContext):
        node = None
        if context.current():
            line = context.current().lstrip()
            if line.startswith("%%"):
                node = self.parse_comment(context)
            elif line.startswith(CHART_TYPES):
                node = self.parse_chart_type_node(context)
            elif line.startswith("subgraph"):
                node = self.parse_graph_node(context)
            elif line == "end":
                node = EndNode()
            elif line.startswith("direction"):
                node = self.parse_direction_node(context)
            elif line.startswith("rule"):
                node = self.parse_rule_node(context)
            elif not line:
                node = EmptyNode()
        logging.debug(f"Parsed node: {node}")
        # advance the context
        context.next()
        yield node
    def parse_comment(self, context: ParserContext):
        is_multi = context.current().lstrip().startswith("%%{")
        text = context.current().lstrip()
        text = text[(2 + int(is_multi)) :]
        if is_multi:
            while not context.current().rstrip().endswith("}%%"):
                text += f"\n{context.next()}"
        return CommentNode(text, is_multi)
    def parse_chart_type_node(self, context: ParserContext) -> ChartTypeNode:
        line = context.current().lstrip()
        if line.contains(" "):
            type, direction = line.split(" ")
        else:
            type = line
            direction = None
        return ChartTypeNode(type, direction)
    def parse_class_def_node(self, context: ParserContext) -> ClassDefNode:
        m = re.match(r"classDef\s(?P<name>[\S]+)\s(?P<styles>.*);?", context.current())
        if not m:
            raise AstParsingException(f"Invalid class definition in{context.current()}")
        name = m.group("name")
        styles = dict(x.split(":") for x in m.group("styles").split(","))
        return ClassDefNode(name, styles)
    def parse_graph_node(self, context: ParserContext):
        text = context.current()
        while str.count('"', text) % 2 == 1 and context.has_next():
            text += f"\n{context.next()}"
        m = re.match(
            r"subgraph\s(?P<id>[^\[]+)(\[\"?)(?P<name>[^\"\]]*)(\"?\]+)",
            text,
            re.MULTILINE | re.IGNORECASE,
        )
        if not m:
            raise AstParsingException(f"Invalid class definition in{text}")
        return GraphNode(m.group("id"), m.group("name"))
    def parse_direction_node(self, context: ParserContext):
        _, direction = context.current().strip().split(" ")
        return DirectionNode(direction)
    def parse_rule_node(self, context: ParserContext):
        text = context.current()
        while str.count('"', text) % 2 == 1 and context.has_next():
            text += f"\n{context.next()}"
        m = re.match(
            r"rule(?P<id>\d+)(\[\"?(?P<label>[^\"\]]+)\"?])?(:::(?P<class>.*))?",
            context.current(),
            re.MULTILINE | re.IGNORECASE,
        )
        if not m:
            raise AstParsingException(f"Invalid rule in {context.current()}")
        return RuleNode(m.group("id"), m.group("label"), m.group("class"))
    # (?P<start>[^-=~\s<]+)\s*((?P<astart>[xo<])?(--|==|-.)(\s*\|?(?P<inlabel>[^-=.|>ox]+)?\|?)?(-*|=*|.+-)(?P<aend>[xo>])|~~~+)(\s*\|(?P<label>[^|]+)?\|)?\s*(?P<end>.+)$
================================================

File: test_common.py
================================================
import re
import pytest
from firewall2mermaid.common import (
    GRAPH_SELECTOR_PATTERN,
    create_adhoc_rule,
    get_effective_selector,
    GraphSelector,
)
from assertpy import assert_that
class TestCreateAdhocRule:
    def test_comment_with_spaces_is_not_quoted(self):
        rule = create_adhoc_rule(
            "dummy",
            "test",
            1,
            action="accept",
            comment="rule added for packet flow",
        )
        assert_that(rule.comment).is_equal_to("rule added for packet flow")
class TestGetEffectiveSelector:
    def test_always_return_fully_qualified_match(self):
        selectors = [
            GraphSelector("section:chain:rule"),
            GraphSelector("section:chain"),
            GraphSelector("section"),
        ]
        result = get_effective_selector(selectors, "section:chain:rule")
        assert_that(result).is_equal_to(GraphSelector("section:chain:rule"))
        result = get_effective_selector(selectors, "section:chain")
        assert_that(result).is_equal_to(GraphSelector("section:chain"))
    @pytest.mark.parametrize(
        "id, expected",
        [
            ("section:chain:rule", GraphSelector("section:chain:")),
            ("section:other:rule", GraphSelector("section::rule")),
            ("section:other:other", GraphSelector("section::")),
            ("other:other:other", GraphSelector("::")),
        ],
    )
    def test_pick_same_level_selector_based_on_score(self, id, expected):
        selectors = [
            GraphSelector("section:chain:"),
            GraphSelector("section::rule"),
            GraphSelector("section::"),
            GraphSelector("::rule"),
            GraphSelector("::"),
        ]
        result = get_effective_selector(selectors, id)
        assert_that(result).is_equal_to(expected)
    def test_no_match_found_when_selectors_given_returns_default_show_selector(self):
        selectors = [
            GraphSelector("section:chain:rule"),
            GraphSelector("section:chain"),
            GraphSelector("section"),
        ]
        result = get_effective_selector(selectors, "other")
        assert_that(result).is_equal_to(GraphSelector("", mod=""))
    def test_no_match_found_when_no_selectors_given_returns_default_include_selector(self):
        result = get_effective_selector([], "other")
        assert_that(result).is_equal_to(GraphSelector("", mod=""))
class TestGraphSelectorPattern:
    @pytest.mark.parametrize(
        "selector",
        [
            "section:chain:rule",
            "section:chain",
            "section",
            "*section",
            "-section",
            "+section",
            "%%section",
            "%%*section",
            "section-with-dash",
            ":",
            "::",
        ],
    )
    def test_pattern_matching(self, selector):
        assert_that(re.match(GRAPH_SELECTOR_PATTERN, selector)).is_not_none()
================================================

File: test_model.py
================================================
import random
from typing import Callable
from unittest.mock import Mock
import pytest
from pytest_mock import mocker
from firewall2mermaid.errors import (
    ChainAlreadyExistsError,
    ElementNotFound,
    SectionAlreadyExistsError,
)
from firewall2mermaid.model import (
    Chain,
    GraphSelector,
    Link,
    LinkableTreeNode,
    PacketFlowElement,
    PacketFlowIterator,
    ParserRule,
    RootNode,
    Rule,
    Section,
    TreeNode,
)
from firewall2mermaid.parser import parse_rule
from assertpy import assert_that
from tests.conftest import (
    _parser_rule_factory,
    _rule_factory,
    known_rule_attributes_for_generation,
    rule_matching_attributes,
    terminal_actions,
)
class DummyLinkNode(LinkableTreeNode):
    def __init__(self, id=None):
        self._id = random.randint(0, 1000000) if id is None else id
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, DummyLinkNode):
            return self.id == __value.id
        return False
    @property
    def id(self) -> int:
        return self._id
def assert_rules_are_equivalent(rule: Rule | None, other: Rule | None):
    assert rule
    assert other
    assert_that(rule.line).is_equal_to(other.line)
    assert_that(rule.index).is_equal_to(other.index)
    assert_that(rule.loggable).is_equal_to(other.loggable)
    assert_that(rule.known_attributes).is_equal_to(other.known_attributes)
    for attribute in rule.known_attributes:
        assert_that(rule.__getattribute__(attribute)).is_equal_to(other.__getattribute__(attribute))
def assert_chains_are_equivalent(chain: Chain, other: Chain):
    assert_that(chain.render).is_equal_to(other.render)
    assert_that(len(chain.rules)).is_equal_to(len(other.rules))
    for rule in chain.rules:
        r = [x for x in other.rules if x.index == rule.index][0]
        assert_rules_are_equivalent(rule, r)
class TestLink:
    def test_link_has_id(self):
        assert_that(Link(DummyLinkNode(), DummyLinkNode()).id).is_not_none()
    def test_link_equals_to_self(self):
        sut = Link(DummyLinkNode(), DummyLinkNode())
        assert_that(sut).is_equal_to(sut)
    def test_similar_link_equals_to_self(self):
        start = DummyLinkNode()
        end = DummyLinkNode()
        sut = Link(start, end)
        other = Link(start, end)
        assert_that(sut).is_equal_to(other)
    def test_clone_link_equals_to_clone(self):
        sut = Link(DummyLinkNode(), DummyLinkNode())
        assert_that(sut.clone()).is_equal_to(sut)
class TestParserRule:
    def test_when_parsing_rule_extra_spaces_are_trimmed(self):
        line = "a line with space "
        rule = parse_rule(line)
        assert_that(rule.line).is_equal_to(line.strip())
def LinkableTreeNodeCreator(root: RootNode | None = None):
    if not root:
        root = RootNode()
    return LinkableTreeNode(root)
def SectionCreator(root: RootNode | None = None):
    if not root:
        root = RootNode()
    return root.add_section(f"SUT{random.randint(0, 10000)}")
def ChainCreator(root: RootNode | None = None):
    if not root:
        root = RootNode()
    section = root.add_section("SUT") if not root.has_section("SUT") else root.section("SUT")
    assert section
    return section.add_chain(f"SUT{random.randint(0, 10000)}")
def RuleCreator(root: RootNode | None = None):
    if not root:
        root = RootNode()
    section = root.add_section("SUT") if not root.has_section("SUT") else root.section("SUT")
    assert section
    chain = section.add_chain("SUT")
    assert chain
    rule = _rule_factory("SUT", "SUT", random.randint(0, 10000))
    chain.add_rule(rule)
    return rule
def RootNodeCreator(parent: TreeNode | None = None):
    return RootNode()
def TreeNodeCreator(parent: TreeNode | None = None):
    if not parent:
        parent = Mock()
    return TreeNode(parent)
class TestTreeNode:
    @pytest.mark.parametrize("sut_maker", [RootNodeCreator])
    def test_tree_root_when_self_is_root_returns_self(self, sut_maker: Callable[..., RootNode]):
        sut = sut_maker()
        assert_that(sut.tree_root).is_equal_to(sut)
    @pytest.mark.parametrize(
        "sut_maker",
        [TreeNodeCreator, LinkableTreeNodeCreator, SectionCreator, ChainCreator, RuleCreator],
    )
    def test_tree_root_when_self_is_not_root_returns_root_of_tree(
        self, sut_maker: Callable[..., TreeNode] | Callable[..., LinkableTreeNode]
    ):
        root = RootNode()
        sut = sut_maker(root)
        assert sut
        assert_that(sut.tree_root).is_equal_to(root)
    def test_eq_when_same_object_returns_true(self):
        sut = TreeNode(DummyLinkNode())
        assert_that(sut).is_equal_to(sut)
    def test_eq_when_different_objects_returns_false(self):
        assert_that(TreeNode(DummyLinkNode(1))).is_not_equal_to(TreeNode(DummyLinkNode(2)))
@pytest.mark.parametrize(
    "sut_maker", [LinkableTreeNodeCreator, SectionCreator, ChainCreator, RuleCreator]
)
class TestLinkableTreeNode:
    def test_add_link_when_when_target_not_in_tree_raise_elementnotfound(self, sut_maker):
        sut = sut_maker(RootNode())
        target = sut_maker(RootNode())
        assert_that(sut.add_link).raises(ElementNotFound).when_called_with(target)
    def test_add_link_when_params_are_good_link_is_properly_created_and_added(self, sut_maker):
        root = RootNode()
        sut = sut_maker(root)
        target = root.add_section("to")
        assert target
        sut.add_link(target, "style", "label")
        assert_that(sut.links).is_length(1)
        assert_that(sut.links[0]).has_start(sut).has_end(target).has_style("style").has_label(
            "label"
        )
    def test_add_existing_link_when_added_removes_links_from_previous_link_owner(self, sut_maker):
        root = RootNode()
        sut = sut_maker(root)
        old_node = root.add_section("old")
        target = root.add_section("to")
        assert target
        assert old_node
        old_node.add_link(target)
        sut.add_existing_link(old_node.links[0])
        assert_that(old_node.links).is_empty
    def test_add_existing_link_repoints_start_of_link(self, sut_maker):
        root = RootNode()
        sut = sut_maker(root)
        old_node = root.add_section("old")
        target = root.add_section("to")
        assert target
        assert old_node
        old_node.add_link(target)
        sut.add_existing_link(old_node.links[0])
        assert_that(sut.links).is_length(1)
        assert_that(sut.links[0]).has_start(sut)
    def test_add_existing_link_when_target_does_not_exist_in_treeraise_elementnotfound(
        self, sut_maker
    ):
        root = RootNode()
        sut = sut_maker(root)
        target = RootNode().add_section("to")
        assert target
        assert_that(sut.add_existing_link).raises(ElementNotFound).when_called_with(
            Link(sut, target)
        )
    def test_add_existing_link_when_previous_owner_does_not_have_link_does_not_raise_error(
        self, sut_maker
    ):
        root = RootNode()
        sut = sut_maker(root)
        target = root.add_section("to")
        assert target
        try:
            sut.add_existing_link(Link(target, target))
        except BaseException:
            pytest.fail("Should not throw exception when link does not exist in previous owner")
    def test_remove_link_when_link_found_is_removed(self, sut_maker):
        root = RootNode()
        sut = sut_maker(root)
        target = root.add_section("to")
        assert target
        sut.links.append(Link(target, target))
        sut.remove_link(sut.links[0])
        assert_that(sut.links).is_length(0)
    def test_remove_link_when_link_not_found_raise_valueerror(self, sut_maker):
        root = RootNode()
        sut = sut_maker(root)
        assert_that(sut.remove_link).raises(ValueError).when_called_with(Link(sut, sut))
    def test_remove_link_when_link_not_found_does_not_raise_error(self, sut_maker):
        root = RootNode()
        sut = sut_maker(root)
        target = root.add_section("to")
        assert target
        sut.add_link(target)
        try:
            sut.remove_links_to(target)
        except BaseException:
            pytest.fail("Should not throw exception")
    def test_remove_link_when_target_matches_multiple_links_all_are_removed(self, sut_maker):
        root = RootNode()
        sut = sut_maker(root)
        target = root.add_section("to")
        assert target
        sut.links.append(Link(sut, target, label="1"))
        sut.links.append(Link(sut, target, label="2"))
        sut.links.append(Link(sut, target, label="3"))
        sut.remove_links_to(target)
        assert_that(sut.links).is_length(0)
    def test_clone_links_links_are_equal_to_clone_links(self, sut_maker):
        root = RootNode()
        sut = sut_maker(root)
        target = root.add_section("to")
        assert target
        sut.add_link(target)
        cloned = sut.clone_links()
        assert_that(cloned).is_equal_to(sut.links)
    def test_clone_links_cloned_links_are_different_objects(self, sut_maker):
        root = RootNode()
        sut = sut_maker(root)
        target = root.add_section("to")
        assert target
        sut.add_link(target)
        cloned = sut.clone_links()
        cloned[0].start = target
        cloned.append(Link(target, target))
        assert_that(cloned).is_not_equal_to(sut.links)
        assert_that(sut.links).does_not_contain(Link(target, target))
class TestRule:
    def test_init_sets_defaults(self, parser_rule_factory: Callable[..., ParserRule]):
        parser_rule: ParserRule = parser_rule_factory("filter", "input", comment="test rule")
        sut = Rule(parser_rule.line, 0, parser_rule.attributes)
        assert_that(sut.parent).is_not_none().has_name("detached")
        assert_that(sut.known_attributes).contains("chain")
        assert_that(sut).has_loggable(True)
        assert_that(sut).has_index(0)
        assert_that(sut).has_raw_line(parser_rule.line)
    def test_id_is_set(self, rule_factory: Callable[..., Rule]):
        sut = rule_factory("filter", "input", 0, comment="test rule")
        assert_that(sut.id).is_not_none().contains(":rule0")
    def test_chain_equals_parent_name(self, rule_factory: Callable[..., Rule]):
        sut = rule_factory("filter", "input", 0, comment="test rule")
        assert_that(val=sut).has_chain(sut.parent.name)
    def test_line_equals_raw_line(self, rule_factory: Callable[..., Rule]):
        sut = rule_factory("filter", "input", 0, comment="test rule")
        assert_that(val=sut).has_line(sut.raw_line)
    @pytest.mark.parametrize("attribute", known_rule_attributes_for_generation)
    def test_has_rule_matchers_when_given_attribute_correctly_determines_result(
        self, attribute: str
    ):
        sut = _rule_factory("filter", "input", 0, **{attribute: "test"})
        assert_that(sut).has_has_rule_matchers(attribute in rule_matching_attributes)
    @pytest.mark.parametrize("action", terminal_actions)
    def test_is_terminal_rule_when_rule_is_terminal_is_true(self, action: str):
        sut = _rule_factory("filter", "input", 0, action=action, comment="test")
        assert_that(sut).has_is_terminal_rule(True)
    @pytest.mark.parametrize("action", terminal_actions)
    def test_is_terminal_status_when_action_is_terminal_when_non_terminal_attribute_present_is_false(
        self, action: str
    ):
        parser_rule = _parser_rule_factory("filter", "input", action=action, ttl="test")
        sut = Rule(parser_rule.line, 0, parser_rule.attributes)
        assert_that(sut).has_is_terminal_rule(False)
    @pytest.mark.parametrize("action", known_rule_attributes_for_generation - terminal_actions)
    def test_is_terminal_status_when_action_is_non_terminal_is_false(self, action: str):
        sut = _rule_factory("filter", "input", 0, action=action, ttl="test")
        assert_that(sut).has_is_terminal_rule(False)
    def test_lt_uses_index_for_comparison(self, rule_factory: Callable[..., Rule]):
        rule = rule_factory("filter", "input", 5, comment="test rule")
        equal_rule = rule_factory("filter", "input", 5, comment="test rule")
        higher_rule = rule_factory("filter", "input", 10, comment="test rule")
        lower_rule = rule_factory("filter", "input", 0, comment="test rule")
        assert_that(rule < lower_rule).is_false()
        assert_that(rule < equal_rule).is_false()
        assert_that(rule < higher_rule).is_true()
    def test_le_uses_index_for_comparison(self, rule_factory: Callable[..., Rule]):
        rule = rule_factory("filter", "input", 5, comment="test rule")
        equal_rule = rule_factory("filter", "input", 5, comment="test rule")
        higher_rule = rule_factory("filter", "input", 10, comment="test rule")
        lower_rule = rule_factory("filter", "input", 0, comment="test rule")
        assert_that(rule <= lower_rule).is_false()
        assert_that(rule <= equal_rule).is_true()
        assert_that(rule <= higher_rule).is_true()
    def test_gt_uses_index_for_comparison(self, rule_factory: Callable[..., Rule]):
        rule = rule_factory("filter", "input", 5, comment="test rule")
        equal_rule = rule_factory("filter", "input", 5, comment="test rule")
        higher_rule = rule_factory("filter", "input", 10, comment="test rule")
        lower_rule = rule_factory("filter", "input", 0, comment="test rule")
        assert_that(rule > lower_rule).is_true()
        assert_that(rule > equal_rule).is_false()
        assert_that(rule > higher_rule).is_false()
    def test_ge_uses_index_for_comparison(self, rule_factory: Callable[..., Rule]):
        rule = rule_factory("filter", "input", 5, comment="test rule")
        equal_rule = rule_factory("filter", "input", 5, comment="test rule")
        higher_rule = rule_factory("filter", "input", 10, comment="test rule")
        lower_rule = rule_factory("filter", "input", 0, comment="test rule")
        assert_that(rule >= lower_rule).is_true()
        assert_that(rule >= equal_rule).is_true()
        assert_that(rule >= higher_rule).is_false()
    def test_next_rule_gives_correctly_next_rule_by_index(self, rule_factory: Callable[..., Rule]):
        rule = rule_factory("filter", "input", 0, comment="test rule")
        next_rule = rule_factory("filter", "input", 1, comment="test rule")
        rule.parent.add_rule(next_rule)
        assert_that(rule.next_rule()).is_not_none().is_equal_to(next_rule)
    def test_next_rule_when_rule_last_in_chain_returns_none(
        self, rule_factory: Callable[..., Rule]
    ):
        rule = rule_factory("filter", "input", 0, comment="test rule")
        assert_that(rule.next_rule()).is_none()
    def test_jump_target_chain_when_chain_doesnt_exist_raises_elementnotfound(
        self, rule_factory: Callable[..., Rule]
    ):
        rule = rule_factory("filter", "input", 0, jump_target="test")
        assert_that(rule.jump_target_chain).raises(ElementNotFound)
    def test_jump_target_chain_returns_chain_in_same_section(
        self, rule_factory: Callable[..., Rule]
    ):
        rule = rule_factory("filter", "input", 0, jump_target="test")
        chain = Chain("test")
        rule.parent.parent.add_chain(chain)
        assert_that(rule.jump_target_chain()).is_equal_to(chain)
    def test_jump_target_chain_when_target_not_in_section_raises_elementnotfound(
        self, rule_factory: Callable[..., Rule]
    ):
        rule = rule_factory("filter", "input", 0, jump_target="test")
        rule.tree_root.add_section("foreign").add_chain("test")
        assert_that(rule.jump_target_chain).raises(ElementNotFound)
    def test_clone_returns_rule_equivalent_to_rule(self, rule_factory: Callable[..., Rule]):
        rule = rule_factory("filter", "input", 0, jump_target="test")
        clone = rule.clone()
        assert_rules_are_equivalent(rule, clone)
    def test_clone_returns_new_object(self, rule_factory: Callable[..., Rule]):
        rule = rule_factory("filter", "input", 0, jump_target="test")
        clone = rule.clone()
        assert_that(rule).is_not_same_as(clone)
    def test_eq_when_other_is_self_return_true(self, rule_factory):
        sut = rule_factory("filter", "input", 0, jump_target="test")
        assert_that(sut).is_equal_to(sut)
    def test_eq_when_other_is_equal_return_true(self, rule_factory):
        sut = rule_factory("filter", "input", 0, jump_target="test")
        other = rule_factory("filter", "input", 0, jump_target="test")
        assert_that(sut).is_equal_to(other)
    def test_eq_when_other_has_different_section_return_true(self, rule_factory):
        sut = rule_factory("filter", "input", 0, jump_target="test")
        other = rule_factory("raw", "input", 0, jump_target="test")
        assert_that(sut).is_equal_to(other)
    def test_eq_when_other_has_different_chain_return_true(self, rule_factory):
        sut = rule_factory("filter", "input", 0, jump_target="test")
        other = rule_factory("filter", "output", 0, jump_target="test")
        assert_that(sut).is_equal_to(other)
    def test_eq_when_other_is_different_attributes_return_false(self, rule_factory):
        sut = rule_factory("filter", "input", 0, jump_target="test")
        other = rule_factory("filter", "input", 0, jump_target="test", action="drop")
        assert_that(sut).is_not_equal_to(other)
    def test_eq_rules_differ_only_in_liks_return_true(self, rule_factory):
        sut = rule_factory("filter", "input", 0, jump_target="test")
        sut.links.append(Link(sut, sut))
        other = sut.clone()
        sut.links.append(Link(other, other))
        assert_that(sut).is_equal_to(other)
class TestChain:
    def test_init_sets_defaults_values(self):
        sut = Chain("test")
        assert_that(sut).has_name("test")
        assert_that(sut.parent).has_name("detached")
        assert_that(sut).has_render(True)
    def test_chain_has_id(self):
        sut = Chain("test")
        assert_that(sut.id).is_not_none()
    def test_add_rule_appends_rule_to_rules(self, rule_factory: Callable[..., Rule]):
        sut = Chain("test")
        rule = rule_factory("filter", "input", 1)
        second_rule = rule_factory("filter", "input", 2)
        assert_that(sut.add_rule(rule)).is_equal_to(rule)
        assert_that(sut.rules).is_length(1).contains(rule)
        assert_that(sut.add_rule(second_rule)).is_equal_to(second_rule)
        assert_that(sut.rules).is_length(2).contains(second_rule)
    def test_add_rule_when_adding_same_rule_multiple_times_only_adds_once(
        self, rule_factory: Callable[..., Rule]
    ):
        sut = Chain("test")
        rule = rule_factory("filter", "input", 1)
        sut.add_rule(rule)
        assert_that(sut.rules).is_length(1).contains(rule)
        assert_that(sut.add_rule(rule)).is_none()
        assert_that(sut.rules).is_length(1).contains(rule)
    def test_add_rule_when_rule_by_index_exists_does_not_add_rule(
        self, rule_factory: Callable[..., Rule]
    ):
        sut = Chain("test")
        rule = rule_factory("filter", "input", 1)
        sut.add_rule(rule)
        assert_that(val=sut.rules).is_length(1).contains(rule)
        assert_that(sut.add_rule(rule_factory("raw", "input", 1))).is_none()
        assert_that(sut.rules).is_length(1).contains(rule)
    def test_remove_rule_when_rule_exists_in_list_removes_from_list(
        self, rule_factory: Callable[..., Rule]
    ):
        sut = Chain("test")
        rule = rule_factory("filter", "input", 1)
        second_rule = rule_factory("filter", "input", 2)
        sut.add_rule(rule)
        sut.add_rule(second_rule)
        assert_that(sut.remove_rule(rule)).is_equal_to(rule)
        assert_that(sut.rules).is_length(1).contains(second_rule)
        assert_that(sut.remove_rule(second_rule)).is_equal_to(second_rule)
        assert_that(sut.rules).is_length(0)
    def test_remove_rule_when_rule_exists_unsets_parent(self, rule_factory: Callable[..., Rule]):
        sut = Chain("test")
        rule = rule_factory("filter", "input", 1)
        second_rule = rule_factory("filter", "input", 2)
        sut.add_rule(rule)
        sut.add_rule(second_rule)
        removed = sut.remove_rule(rule)
        assert removed
        assert_that(removed.parent).is_not_equal_to(sut)
    def test_remove_rule_when_rules_does_not_exist_returns_none(
        self, rule_factory: Callable[..., Rule]
    ):
        sut = Chain("test")
        rule = rule_factory("filter", "input", 1)
        assert_that(sut.remove_rule(rule)).is_none()
    def test_first_rule_when_no_rules_exist_returns_none(self):
        sut = Chain("test")
        assert_that(sut.first_rule()).is_none()
    def test_first_rule_returns_first_rule_by_index(self, rule_factory: Callable[..., Rule]):
        sut = Chain("test")
        first_rule = rule_factory("filter", "input", 1)
        second_rule = rule_factory("filter", "input", 2)
        sut.add_rule(second_rule)
        sut.add_rule(first_rule)
        assert_that(sut.first_rule()).is_equal_to(first_rule)
    def test_last_rule_when_no_rules_exist_returns_none(self):
        sut = Chain("test")
        assert_that(sut.last_rule()).is_none()
    def test_last_rule_returns_last_rule_by_index(self, rule_factory: Callable[..., Rule]):
        sut = Chain("test")
        first_rule = rule_factory("filter", "input", 1)
        second_rule = rule_factory("filter", "input", 2)
        sut.add_rule(second_rule)
        sut.add_rule(first_rule)
        assert_that(sut.last_rule()).is_equal_to(second_rule)
    def test_next_rule_when_no_rules_exist_returns_none(self, rule_factory: Callable[..., Rule]):
        rule = rule_factory("filter", "input", 0, comment="test rule")
        sut = Chain("test")
        assert_that(sut.next_rule(rule)).is_none()
    def test_next_rule_when_rule_last_in_chain_returns_none(
        self, rule_factory: Callable[..., Rule]
    ):
        rule = rule_factory("filter", "input", 0, comment="test rule")
        sut = Chain("test")
        sut.add_rule(rule)
        assert_that(sut.next_rule(rule)).is_none()
    def test_next_rule_returns_next_rule_by_index(self, rule_factory: Callable[..., Rule]):
        rule: Rule = rule_factory("filter", "input", 0, comment="test rule")
        next_rule: Rule = rule_factory("filter", "input", 1, comment="test rule")
        sut = Chain("test")
        sut.add_rule(rule)
        sut.add_rule(next_rule)
        assert_that(sut.next_rule(rule)).is_equal_to(next_rule)
    def test_detach_removes_from_parent(self):
        sut = Chain("test")
        parent = sut.parent
        sut.detach()
        assert_that(sut.parent).is_not_none().is_not_equal_to(parent)
        assert_that(sut).is_not_in(parent.chains)
    def test_clone_returns_equivalent_chain(self):
        sut = Chain("test")
        assert_that(sut).is_equal_to(sut.clone())
    def test_clone_clones_rules(self, rule_factory: Callable[..., Rule]):
        sut = Chain("test")
        rule: Rule = rule_factory("filter", "input", 0, comment="test rule")
        second_rule: Rule = rule_factory("filter", "input", 1, comment="test rule")
        sut.add_rule(rule)
        sut.add_rule(second_rule)
        clone = sut.clone()
        assert_that(clone.rules).is_length(2)
        assert_rules_are_equivalent(sut.first_rule(), clone.first_rule())
        assert_rules_are_equivalent(sut.last_rule(), clone.last_rule())
    def test_eq_when_other_is_self_return_true(self):
        sut = Chain("test")
        assert_that(sut).is_equal_to(sut)
    def test_eq_when_other_is_equal_return_true(self):
        assert_that(Chain("test")).is_equal_to(Chain("test"))
    def test_eq_when_other_is_different_return_false(self):
        assert_that(Chain("test")).is_not_equal_to(Chain("Dummy"))
    def test_eq_when_other_has_different_section_return_true(self):
        sut = Chain("test")
        parent = Section("new")
        other = Chain("test")
        parent.add_chain(other)
        assert_that(sut).is_equal_to(other)
    def test_eq_when_links_differ_return_true(self):
        sut = Chain("test")
        sut.links.append(Link(sut, sut))
        other = sut.clone()
        assert_that(sut).is_equal_to(other)
    def test_eq_when_rules_differ_return_false(self, rule_factory):
        sut = Chain("test")
        sut.add_rule(rule_factory("filter", "test", 0))
        other = sut.clone()
        other.add_rule(rule_factory("filter", "test", 1))
        assert_that(sut).is_not_equal_to(other)
class TestSection:
    def test_inits_to_defaults_values(self):
        sut = Section("test")
        assert_that(sut.name).is_equal_to("test")
        assert_that(sut.render).is_true()
    def test_section_has_id(self):
        sut = Section("test")
        assert_that(sut.id).is_not_none()
    def test_has_chain_works(self):
        sut = Section("sut")
        sut.add_chain("test")
        assert_that(sut.has_chain("test")).is_true()
        assert_that(sut.has_chain("other")).is_false()
    def test_add_chain(self):
        sut = Section("test")
        chain = Chain("test")
        sut.add_chain(chain)
        assert_that(sut.chains).is_length(1).contains(chain)
        chain = Chain("test2")
        sut.add_chain(chain)
        assert_that(sut.chains).is_length(2).contains(chain)
    def test_add_chain_multiple_times_raises_chainalreadyexistserror(self):
        sut = Section("test")
        chain = Chain("test")
        sut.add_chain(chain)
        assert_that(sut.chains).is_length(1).contains(chain)
        assert_that(sut.add_chain).raises(ChainAlreadyExistsError).when_called_with(chain)
        assert_that(sut.chains).is_length(1).contains(chain)
    def test_add_chain_with_same_name_raises_chainalreadyexistserror(self):
        sut = Section("test")
        chain = Chain("test")
        sut.add_chain(chain)
        assert_that(sut.chains).is_length(1).contains(chain)
        assert_that(sut.add_chain).raises(ChainAlreadyExistsError).when_called_with("test")
        assert_that(sut.chains).is_length(1).contains(chain)
    def test_add_or_get_chain_adds_chain_when_not_found(self):
        sut = Section("test")
        assert_that(sut.get_or_add_chain("test")).is_not_none().has_name("test")
        assert_that(sut.has_chain("test"))
    def test_add_or_get_chain_gets_chain_when_found(self):
        sut = Section("test")
        chain = Chain("test")
        sut.add_chain(chain)
        assert_that(sut.get_or_add_chain("test")).is_not_none().is_same_as(chain)
    def test_chain_returns_correct_chain(self):
        sut = Section("test")
        chain = Chain("test")
        sut.add_chain(chain)
        assert_that(sut.chain("test")).is_equal_to(chain)
    def test_chain_returns_none_if_not_found(self):
        sut = Section("test")
        sut.add_chain("test")
        assert_that(sut.chain("nonexistant")).is_none()
    def test_remove_chain(self):
        sut = Section("test")
        chain = Chain("input")
        second_chain = Chain("output")
        sut.add_chain(chain)
        sut.add_chain(second_chain)
        assert_that(sut.remove_chain(chain)).is_equal_to(chain)
        assert_that(sut.chains).is_length(1).contains(second_chain)
        assert_that(sut.remove_chain(second_chain)).is_equal_to(second_chain)
        assert_that(sut.chains).is_length(0)
    def test_remove_chain_resets_parent(self):
        sut = Section("test")
        chain = Chain("input")
        sut.add_chain(chain)
        removed = sut.remove_chain(chain=chain)
        assert removed
        assert_that(removed.parent).is_not_equal_to(sut)
    def test_remove_chain_with_non_existing_chain_returns_none(
        self, rule_factory: Callable[..., Rule]
    ):
        sut = Section("test")
        chain = Chain("test")
        assert_that(sut.remove_chain(chain)).is_none()
    def test_detach(self):
        sut = Section("test")
        parent = sut.parent
        sut.detach()
        assert_that(sut.parent).is_not_none().is_not_equal_to(parent)
        assert_that(parent.sections).does_not_contain(sut)
    def test_clone_returns_equivalent_chain(self):
        sut = Section("test")
        clone = sut.clone()
        assert_that(sut.render).is_equal_to(clone.render)
    def test_clone_clones_chains(self):
        sut = Section("test")
        sut.add_chain("first")
        sut.add_chain("second")
        clone = sut.clone()
        assert_that(clone.chains).is_length(2)
        assert_chains_are_equivalent(clone.chains[0], sut.chains[0])
        assert_chains_are_equivalent(clone.chains[1], sut.chains[1])
    def test_next_section_returns_none_if_no_next_section(self):
        sut = Section("test")
        assert_that(sut.next_section()).is_none()
    @pytest.mark.parametrize("execution_number", range(10))
    def test_next_section_returns_next_section(self, execution_number: int):
        root = RootNode()
        section_legend = Section("legend")
        section_raw = Section("raw")
        section_mangle = Section("mangle")
        section_nat = Section("nat")
        section_filter = Section("filter")
        section_other = Section("other")
        l = [
            section_legend,
            section_raw,
            section_mangle,
            section_nat,
            section_filter,
            section_other,
        ]
        random.shuffle(l)
        for section in l:
            root.add_section(section)
        assert_that(section_legend.next_section()).is_not_none().is_equal_to(section_raw)
        assert_that(section_raw.next_section()).is_not_none().is_equal_to(section_mangle)
        assert_that(section_mangle.next_section()).is_not_none().is_equal_to(section_nat)
        assert_that(section_nat.next_section()).is_not_none().is_equal_to(section_filter)
        assert_that(section_filter.next_section()).is_not_none().is_equal_to(section_other)
    def test_eq_when_other_is_self_return_true(self):
        sut = Section("test")
        assert_that(sut).is_equal_to(sut)
    def test_eq_when_other_is_equal_return_true(self):
        assert_that(Section("test")).is_equal_to(Section("test"))
    def test_eq_when_other_different_root_return_true(self):
        sut = Section("test")
        other = Section("test")
        RootNode().add_section(other)
        assert_that(sut).is_equal_to(other)
    def test_eq_when_other_is_different_return_false(self):
        assert_that(Section("test")).is_not_equal_to(Section("Dummy"))
    def test_eq_when_links_differ_return_true(self):
        sut = Section("test")
        sut.links.append(Link(sut, sut))
        other = sut.clone()
        assert_that(sut).is_equal_to(other)
    def test_eq_when_chains_differ_return_false(self):
        sut = Section("test")
        sut.add_chain(Chain("first"))
        other = sut.clone()
        other.add_chain(Chain("second"))
        assert_that(sut).is_not_equal_to(other)
class TestRootNode:
    def test_inits_to_defaults_values(self):
        sut = RootNode()
        assert_that(sut.sections).is_empty()
    def test_add_or_get_section_adds_section_when_not_found(self):
        sut = RootNode()
        assert_that(sut.get_or_add_section("test")).is_not_none().has_name("test")
        assert_that(sut.has_section("test"))
    def test_add_or_get_section_gets_section_when_found(self):
        sut = RootNode()
        section = sut.add_section("test")
        assert_that(sut.get_or_add_section("test")).is_not_none().is_same_as(section)
    def test_has_section_works(self):
        sut = RootNode()
        sut.add_section("test")
        assert_that(sut.has_section("test")).is_true()
        assert_that(sut.has_section("other")).is_false()
    def test_add_section_works(self):
        sut = RootNode()
        section = Section("test")
        sut.add_section(section)
        assert_that(sut.sections).is_length(1).contains(section)
        assert_that(section.parent).is_equal_to(sut)
    def test_add_section_multiple_times_raises_sectionalreadyexists_error(self):
        sut = RootNode()
        section = Section("test")
        sut.add_section(section)
        assert_that(sut.add_section).raises(SectionAlreadyExistsError).when_called_with(section)
        assert_that(sut.sections).is_length(1).contains(section)
    def test_add_section_with_same_name_raises_sectionalreadyexistserror(self):
        sut = RootNode()
        section = Section("test")
        sut.add_section(section)
        assert_that(sut.sections).is_length(1).contains(section)
        assert_that(sut.add_section).raises(SectionAlreadyExistsError).when_called_with("test")
        assert_that(sut.sections).is_length(1).contains(section)
    def test_remove_section_returns_none_if_section_not_found(self):
        assert_that(RootNode().remove_section(Section("test"))).is_none()
    def test_next_section_returns_none_if_section_not_in_list(self):
        assert_that(RootNode().next_section(Section("test"))).is_none()
    def test_next_section_returns_none_if_no_next_section(self):
        sut = RootNode()
        section = Section("test")
        sut.add_section(section)
        assert_that(sut.next_section(section)).is_none()
    @pytest.mark.parametrize("execution_number", range(10))
    def test_next_section_returns_next_section_by_name(self, execution_number: int):
        sut = RootNode()
        section_legend = Section("legend")
        section_raw = Section("raw")
        section_mangle = Section("mangle")
        section_nat = Section("nat")
        section_filter = Section("filter")
        section_other = Section("other")
        l = [
            section_legend,
            section_raw,
            section_mangle,
            section_nat,
            section_filter,
            section_other,
        ]
        random.shuffle(l)
        for section in l:
            sut.add_section(section)
        assert_that(sut.next_section(section_legend)).is_not_none().is_equal_to(section_raw)
        assert_that(sut.next_section(section_raw)).is_not_none().is_equal_to(section_mangle)
        assert_that(sut.next_section(section_mangle)).is_not_none().is_equal_to(section_nat)
        assert_that(sut.next_section(section_nat)).is_not_none().is_equal_to(section_filter)
        assert_that(sut.next_section(section_filter)).is_not_none().is_equal_to(section_other)
    def test_first_section_returns_none_if_no_sections(self):
        assert_that(RootNode().first_section()).is_none()
    def test_first_section_returns_the_first_available_section(self):
        sut = RootNode()
        section_legend = Section("legend")
        section_mangle = Section("mangle")
        section_nat = Section("nat")
        section_filter = Section("filter")
        section_other = Section("other")
        sut.add_section(section_other)
        assert_that(sut.first_section()).is_equal_to(section_other)
        sut.add_section(section_filter)
        assert_that(sut.first_section()).is_equal_to(section_filter)
        sut.add_section(section_mangle)
        assert_that(sut.first_section()).is_equal_to(section_mangle)
        sut.add_section(section_nat)
        assert_that(sut.first_section()).is_equal_to(section_mangle)
        sut.add_section(section_legend)
        assert_that(sut.first_section()).is_equal_to(section_legend)
    def test_section_returns_none_if_not_found(self):
        sut = RootNode()
        sut.add_section("filter")
        assert_that(sut.section("test")).is_none()
    def test_section_returns_correct_section(self):
        sut = RootNode()
        section = Section("filter")
        sut.add_section(section)
        assert_that(sut.section("filter")).is_not_none().is_equal_to(section)
    def test_next_rule_index_returns_the_next_available_id(self):
        sut = RootNode()
        sut.add_section("test").add_chain("test").add_rule(_rule_factory("test", "test", 50))
        sut.add_section("test2").add_chain("test2").add_rule(_rule_factory("test2", "test", 10))
        assert_that(sut.next_rule_index()).is_equal_to(51)
    def test_eq_when_other_is_self_return_true(self):
        sut = RootNode()
        assert_that(sut).is_equal_to(sut)
    def test_eq_when_other_is_equal_return_true(self):
        assert_that(RootNode()).is_equal_to(RootNode())
    def test_eq_when_sections_differ_return_false(self):
        sut = RootNode()
        sut.add_section("first")
        other = sut.clone()
        other.add_section("second")
        assert_that(sut).is_not_equal_to(other)
    def test_clone_returns_root_node_with_sections(self):
        sut = RootNode()
        sut.add_section("test")
        other = sut.clone()
        assert_that(sut.sections).is_equal_to(other.sections)
    def test_clone_returns_different_object_for_sections(self):
        sut = RootNode()
        sut.add_section("test")
        other = sut.clone()
        assert_that(id(sut.sections)).is_not_equal_to(id(other.sections))
        assert_that(id(sut.sections[0])).is_not_equal_to(id(other.sections[0]))
class TestPacketFlowElement:
    def test_last_node_returns_last_node_in_sequence(self):
        first = PacketFlowElement("1", "1")
        second = PacketFlowElement("2", "2")
        third = PacketFlowElement("3", "3")
        first.next = second
        second.next = third
        assert_that(first.last_node()).is_equal_to(third)
        assert_that(second.last_node()).is_equal_to(third)
        assert_that(third.last_node()).is_equal_to(third)
class TestPacketFlowIterator:
    def test_iterator_follows_order(self):
        first = PacketFlowElement("1", "1")
        second = PacketFlowElement("2", "2")
        third = PacketFlowElement("3", "3")
        first.next = second
        second.next = third
        iter = PacketFlowIterator(first)
        assert_that(next(iter)).is_equal_to(first)
        assert_that(next(iter)).is_equal_to(second)
        assert_that(next(iter)).is_equal_to(third)
class TestGraphSelector:
    def test_graph_selector_is_default(self):
        selector = GraphSelector("")
        assert_that(selector.default).is_true()
        selector = GraphSelector("", mod="+")
        assert_that(selector.default).is_true()
        selector = GraphSelector("filter")
        assert_that(selector.default).is_false()
    def test_graph_selector_is_splat(self):
        selector = GraphSelector("", mod="+")
        assert_that(selector.splat).is_false()
        selector = GraphSelector("", mod="*+")
        assert_that(selector.splat).is_true()
    def test_graph_selector_is_normal_render(self):
        selector = GraphSelector("")
        assert_that(selector.show).is_true()
        selector = GraphSelector("", mod="+")
        assert_that(selector.show).is_true()
        selector = GraphSelector("", mod="*")
        assert_that(selector.show).is_false()
    def test_graph_selector_is_remove(self):
        # Test when mod does not contain "-"
        selector = GraphSelector("", mod="+")
        assert_that(selector.remove).is_false()
        # Test when mod contains "-"
        selector = GraphSelector("", mod="-+")
        assert_that(selector.remove).is_true()
    def test_graph_selector_is_collapse(self):
        # Test when mod does not contain "%"
        selector = GraphSelector("", mod="+")
        assert_that(selector.collapse).is_false()
        # Test when mod contains "%"
        selector = GraphSelector("", mod="%+")
        assert_that(selector.collapse).is_true()
    def test_graph_selector_is_render(self):
        # Test when mod contains "-"
        selector = GraphSelector("", mod="-+")
        assert_that(selector.render).is_false()
        # Test when mod does not contain "-"
        selector = GraphSelector("", mod="+")
        assert_that(selector.render).is_true()
================================================

File: test_parser.py
================================================
from typing import Callable
from firewall2mermaid.parser import parse_rule
from assertpy import assert_that
class TestParser:
    def test_when_parsing_rule_line_if_no_action_is_present_default_to_accept(
        self, parser_rule_line_factory: Callable[..., str]
    ):
        line = parser_rule_line_factory("section", "chain")
        rule = parse_rule(line)
        assert_that(rule.attributes).contains_entry({"action": "accept"})
    def test_when_parsing_rule_line_action_is_present(
        self, parser_rule_line_factory: Callable[..., str]
    ):
        line = parser_rule_line_factory("section", "chain", action="action")
        rule = parse_rule(line)
        assert_that(rule.attributes).contains_entry({"action": "action"})
    def test_when_parsing_rule_line_section_is_present(
        self, parser_rule_line_factory: Callable[..., str]
    ):
        line = parser_rule_line_factory("section", "chain")
        rule = parse_rule(line)
        assert_that(rule.section).is_equal_to("section")
    def test_when_parsing_rule_line_chain_is_present(
        self, parser_rule_line_factory: Callable[..., str]
    ):
        line = parser_rule_line_factory("section", "chain")
        rule = parse_rule(line)
        assert_that(rule.chain).is_equal_to("chain")
        assert_that(rule.attributes).contains_entry({"chain": "chain"})
    def test_when_parsing_rule_with_extra_attribute_attribute_is_present(
        self, parser_rule_line_factory: Callable[..., str]
    ):
        line = parser_rule_line_factory("section", "chain", dummy="dummy")
        rule = parse_rule(line)
        assert_that(rule.attributes).contains_entry({"dummy": "dummy"})
================================================

File: test_render.py
================================================
import pytest
from firewall2mermaid.common import (
    LINK_STYLE_BETWEEN_SECTIONS,
    LINK_STYLE_INVISIBLE,
    LINK_STYLE_NORMAL,
)
from firewall2mermaid.model import Chain, GraphSelector, Link, RootNode, Rule, Section
from firewall2mermaid.render import Renderer
from firewall2mermaid.render.common import determine_link_label, determine_rule_label
from firewall2mermaid.render.model import LinkNode, RuleNode
from firewall2mermaid.tree import TreeMaker
from tests.assertions import AssertionFailure, assert_graph
from assertpy import assert_that
class TestBasicRendering:
    def test_does_not_include_extra_newlines(self):
        sut = Renderer(RootNode(), [])
        graph = sut.render_graph()
        assert_that(graph).starts_with("%%{init: ")
        assert_that(graph).does_not_contain("\n\n\n\n")
    def test_renders_graph_header(self):
        sut = Renderer(RootNode(), [])
        graph = sut.render_graph()
        assert_graph(graph).has_line(
            "%%{init: {'flowchart': {'htmlLabels': false}, 'theme': 'dark'}}%%"
        ).and_then.has_line("flowchart TB")
    def test_renders_rules_as_logs(self, default_tree_root):
        sut = Renderer(default_tree_root, [], log_rules=True)
        graph = sut.render_graph()
        assert_graph(graph).has_line("%% /ip firewall").exactly(32)
    def test_renders_root_graph_section(self, default_tree_root):
        sut = Renderer(default_tree_root, [])
        graph = sut.render_graph()
        assert_graph(graph).has_graph("root").with_direction("TB").at_depth(0)
    @pytest.mark.parametrize(
        "style", ["fasttrack-connection", "accept", "disabled", "log", "jump", "drop"]
    )
    def test_renders_styles(self, default_tree_root, style):
        sut = Renderer(default_tree_root, [])
        graph = sut.render_graph()
        assert_graph(graph).has_style(style)
    def test_renders_relationships_at_end_of_graph(self, default_tree_root):
        sut = Renderer(default_tree_root, [])
        graph = sut.render_graph()
        assert_graph(graph).has_graph("root").followed_by.has_line("%% Relationships")
    def test_dont_render_root_node_when_show_root_is_false(self, default_tree_root):
        sut = Renderer(default_tree_root, [], show_root=False)
        graph = sut.render_graph()
        assert_that(assert_graph(graph).has_graph).raises(AssertionFailure).when_called_with("root")
    def test_extra_logs_added_to_header(self, default_tree_root):
        sut = Renderer(default_tree_root, [], extra_logs=["log 1", "log 2"])
        graph = sut.render_graph()
        assert_that(graph).starts_with("%% log 1\n%% log 2")
class TestSplat:
    def test_splat_chains_rendered_on_their_own(self, default_tree_root):
        sut = Renderer(default_tree_root, [GraphSelector("filter:input", "*")], show_root=False)
        graph = sut.render_graph()
        assert_graph(graph).has_graph("filter:input")
    def test_splatted_chain_rendered_id_for_label(self, default_tree_root):
        sut = Renderer(default_tree_root, [GraphSelector("filter:input", "*")], show_root=False)
        graph = sut.render_graph()
        assert_graph(graph).has_graph("filter:input").with_label("filter:input")
    def test_splat_section_renders_each_chain_on_its_own(self, default_tree_root):
        sut = Renderer(default_tree_root, [GraphSelector("filter", "*")], show_root=False)
        graph = sut.render_graph()
        assert_graph(graph).has_graph("filter:input")
        assert_graph(graph).has_graph("filter:forward")
        assert_graph(graph).has_graph("filter:output")
    def test_splat_chains_add_legend_links(self, default_tree_root):
        sut = Renderer(default_tree_root, [GraphSelector("nat", "*")], show_root=False)
        graph = sut.render_graph()
        assert_graph(graph).has_link("legend").with_to("nat:dstnat").with_style(
            LINK_STYLE_INVISIBLE
        )
    def test_emplty_parent_link_removed_from_legend(self, default_tree_root):
        sut = Renderer(default_tree_root, [GraphSelector("nat", "*")], show_root=False)
        graph = sut.render_graph()
        assert_that(
            assert_graph(graph).has_link("legend").with_style(LINK_STYLE_INVISIBLE).with_to
        ).raises(AssertionFailure).when_called_with("nat")
class TestSelectors:
    def test_multiple_mods_per_selector(self, default_tree_root):
        # Arrange
        sut = Renderer(default_tree_root, [GraphSelector("nat:dstnat", mod="*%+")])
        # Act
        graph = sut.render_graph()
        # Assert
        assert_graph(graph).has_graph("root").has_rule().with_label(
            "nat:dstnat *collapsed"
        ).with_style("collapsed")
    def test_multiple_selector_picks_first_one(self, default_tree_root):
        # Arrange
        sut = Renderer(
            default_tree_root,
            [GraphSelector("nat:dstnat", "+"), GraphSelector("nat:dstnat", "-")],
        )
        # Act
        graph = sut.render_graph()
        # Assert
        assert_graph(graph).has_graph("root").has_graph("nat").has_graph("nat:dstnat")
    def test_global_selector_does_not_impact_others(self, default_tree_root):
        # Arrange
        sut = Renderer(
            default_tree_root,
            [
                GraphSelector("nat:dstnat", "+"),
                GraphSelector("nat", "+"),
                GraphSelector("", "%"),
            ],
        )
        # Act
        graph = sut.render_graph()
        # Assert
        assert_graph(graph).has_graph("root").has_graph("nat").has_graph("nat:dstnat")
class TestLegendRendering:
    def test_adds_legend_to_root(self, default_tree_root):
        sut = Renderer(default_tree_root, [], show_legend=True)
        graph = sut.render_graph()
        assert_that(graph).starts_with("%%{init: ")
        assert_graph(graph).has_graph("root").has_graph(
            "legend", direct_descendants_only=False
        ).with_label("Legend")
    def test_when_legend_is_false_do_not_render_legend(self, default_tree_root):
        sut = Renderer(default_tree_root, [], show_legend=False)
        graph = sut.render_graph()
        assert_that(graph).does_not_contain("subgraph legend-container")
        assert_that(graph).does_not_contain("subgraph legend")
    @pytest.mark.parametrize(
        "style", ["fasttrack-connection", "accept", "disabled", "log", "jump", "drop"]
    )
    def test_legend_has_rules_for_each_style(self, default_tree_root, style):
        sut = Renderer(default_tree_root, [], show_legend=True)
        graph = sut.render_graph()
        assert_graph(graph).has_graph("root").has_graph("legend").has_rule().with_label(
            style
        ).with_style(style).at_depth(2)
    def test_when_rootless_when_no_subgraphs_add_legend_before_first_rule_graph(
        self, default_tree_root
    ):
        sut = Renderer(
            default_tree_root, [GraphSelector(":", "*%")], show_legend=True, show_root=False
        )
        graph = sut.render_graph()
        assert_that(graph).starts_with("%%{init: ")
        assert_graph(graph).has_graph("legend").with_label("Legend").has_rule()
class TestSectionRendering:
    @pytest.mark.parametrize("section", ["filter", "nat", "raw", "mangle"])
    def test_renders_all_sections(self, default_tree_root, section):
        sut = Renderer(default_tree_root, [])
        graph = sut.render_graph()
        assert_graph(graph).has_graph("root").has_graph(section).with_label(section).with_direction(
            "TB"
        ).at_depth(1)
class TestChainRendering:
    @pytest.mark.parametrize(
        "section, chain, label",
        [
            ("raw", "raw:prerouting", "prerouting"),
            ("raw", "raw:output", "output"),
            ("raw", "raw:jump-chain", "jump-chain"),
            ("mangle", "mangle:prerouting", "prerouting"),
            ("mangle", "mangle:input", "input"),
            ("mangle", "mangle:forward", "forward"),
            ("mangle", "mangle:output", "output"),
            ("mangle", "mangle:postrouting", "postrouting"),
            ("nat", "nat:dstnat", "dstnat"),
            ("nat", "nat:srcnat", "srcnat"),
            ("filter", "filter:input", "input"),
            ("filter", "filter:output", "output"),
            ("filter", "filter:forward", "forward"),
            ("filter", "filter:terminal-chain", "terminal-chain"),
            ("filter", "filter:jump-chain", "jump-chain"),
            ("filter", "filter:disabled-chain", "disabled-chain"),
            ("filter", "filter:log-chain", "log-chain"),
            ("filter", "filter:rule-order", "rule-order"),
        ],
    )
    def test_renders_all_graph_chains(self, default_tree_root, section, chain, label):
        sut = Renderer(default_tree_root, [])
        graph = sut.render_graph()
        assert_graph(graph).has_graph("root").has_graph(section).has_graph(chain).with_label(
            label
        ).with_direction("TB").at_depth(2)
class TestRuleStyleRendering:
    def test_render_stylized_rule(self):
        sut = RuleNode("id", "a label", "style")
        result = sut.render()
        assert_that(result).contains(":::style")
    def test_render_non_stylized_rule(self):
        sut = RuleNode("id", "a label")
        result = sut.render()
        assert_that(result).does_not_contain(":::")
class TestRuleLabelRendering:
    @pytest.mark.parametrize("action", ["unknown", "", None])
    def test_return_id_as_label_for_unrecognized_action_rule(self, action):
        rule = Rule("rule line", 1, {"action": action})
        label = determine_rule_label(rule)
        assert_that(label).is_equal_to("detached:detached:rule1")
    @pytest.mark.parametrize("action", ["log", "drop", "accept", "return"])
    def test_return_action_as_label_for_recognized_action_rule(self, action):
        rule = Rule("rule line", 1, {"action": action})
        label = determine_rule_label(rule)
        assert_that(label).is_equal_to(action)
    def test_return_label_for_jump_action_rule(self):
        rule = Rule("rule line", 1, {"action": "jump", "jump_target": "jump-target"})
        label = determine_rule_label(rule)
        assert_that(label).is_equal_to("jump to jump-target")
    @pytest.mark.parametrize("action", ["add-src-to-address-list", "add-dst-to-address-list"])
    def test_return_label_for_add_to_list_rule(self, action):
        rule = Rule("rule line", 1, {"action": action, "address_list": "address-list"})
        label = determine_rule_label(rule)
        assert_that(label).is_equal_to("add ip to 'address-list'")
    @pytest.mark.parametrize("action", ["add-src-to-address-list", "add-dst-to-address-list"])
    def test_return_label_for_add_to_list_rule_with_timeout(self, action):
        rule = Rule(
            "rule line",
            1,
            {"action": action, "address_list": "address-list", "address_list_timeout": "1d"},
        )
        label = determine_rule_label(rule)
        assert_that(label).is_equal_to("add ip to 'address-list' for 1d")
    def test_return_comment_for_comment_only_rule(self):
        rule = Rule("rule line", 1, {"comment": "comment"})
        label = determine_rule_label(rule)
        assert_that(label).is_equal_to("comment")
    def test_return_log_when_rule_has_log_append(self):
        rule = Rule("rule line", 1, {"action": "accept", "log": "yes", "log_prefix": "log-prefix"})
        label = determine_rule_label(rule)
        assert_that(label).ends_with('!>{log-prefix}"')
    def test_return_question_mark_when_rule_has_multiple_links_and_property_matchers(
        self,
    ):
        rule = Rule("rule line", 1, {"protocol": "tcp", "dst_port": "80", "src_port": "80"})
        rule.add_link(rule)
        rule.add_link(rule)
        label = determine_rule_label(rule)
        assert_that(label).ends_with("?")
    def test_return_packet_information_when_rule_has_packet_information(self):
        rule = Rule("rule line", 1, {"protocol": "tcp", "tcp_flags": "syn", "dst_limit": 10})
        label = determine_rule_label(rule)
        assert_that(label).is_equal_to("is tcp,syn,below 10")
    def test_return_connection_information_when_rule_has_connection_information(self):
        rule = Rule("rule line", 1, {"connection_state": "new"})
        label = determine_rule_label(rule)
        assert_that(label).is_equal_to("connection is new")
    def test_return_src_information_when_rule_has_src_information(self):
        rule = Rule("rule line", 1, {"src_address": "192.168.0.0", "src_port": "80"})
        label = determine_rule_label(rule)
        assert_that(label).is_equal_to("src is 192.168.0.0:80")
    def test_return_src_information_when_rule_has_src_information_with_port(self):
        rule = Rule("rule line", 1, {"src_address": "192.168.0.0", "port": "80"})
        label = determine_rule_label(rule)
        assert_that(label).contains("src is 192.168.0.0:*80")
    def test_return_src_information_when_rule_has_src_information_with_in_interface(self):
        rule = Rule(
            "rule line", 1, {"src_address": "192.168.0.0", "src_port": "80", "in_interface": "eth1"}
        )
        label = determine_rule_label(rule)
        assert_that(label).contains("src is 192.168.0.0:80 on eth1")
    def test_return_src_information_when_rule_has_src_information_with_in_bridge_port(
        self,
    ):
        rule = Rule(
            "rule line", 1, {"src_address": "192.168.0.0", "src_port": "80", "in_bridge_port": 80}
        )
        label = determine_rule_label(rule)
        assert_that(label).contains("src is 192.168.0.0:80 on :80")
    def test_return_dst_information_when_rule_has_dst_information(self):
        rule = Rule("rule line", 1, {"dst_address": "192.168.0.0", "dst_port": "80"})
        label = determine_rule_label(rule)
        assert_that(label).is_equal_to("dst is 192.168.0.0:80")
    def test_return_dst_information_when_rule_has_dst_information_with_dst_port(self):
        rule = Rule("rule line", 1, {"dst_address": "192.168.0.0", "port": "80"})
        label = determine_rule_label(rule)
        assert_that(label).contains("dst is 192.168.0.0:*80")
    def test_return_dst_information_when_rule_has_dst_information_with_out_interface(self):
        rule = Rule(
            "rule line",
            1,
            {"dst_address": "192.168.0.0", "dst_port": "80", "out_interface": "eth1"},
        )
        label = determine_rule_label(rule)
        assert_that(label).contains("dst is 192.168.0.0:80 on eth1")
    def test_return_dst_information_when_rule_has_dst_information_with_out_bridge_port(self):
        rule = Rule(
            "rule line", 1, {"dst_address": "192.168.0.0", "dst_port": "80", "out_bridge_port": 80}
        )
        label = determine_rule_label(rule)
        assert_that(label).contains("dst is 192.168.0.0:80 on :80")
    @pytest.mark.parametrize("comment", ["[", "]", "{", "}", "(", ")"])
    def test_quote_label_when_label_includes_special_characters(self, comment):
        rule = Rule("rule line", 1, {"action": "accept", "comment": comment})
        label = determine_rule_label(rule)
        assert_that(label).starts_with('"').ends_with('"')
    @pytest.mark.parametrize(
        "mode,expected_value",
        [
            ("show", "this is a comment"),
            ("hide", "accept"),
            ("auto", "this is a comment"),
            ("prefer", "this is a comment"),
        ],
    )
    def test_comment_handling_for_fallback_label(self, mode, expected_value):
        # Arrange
        rule = Rule("rule line", 1, {"action": "accept", "comment": "this is a comment"})
        # Act
        label = determine_rule_label(rule, mode)
        # Assert
        assert_that(label).is_equal_to(expected_value)
    @pytest.mark.parametrize(
        "mode,expected_value",
        [
            ("show", "is tcp *this is a comment"),
            ("hide", "is tcp"),
            ("auto", "is tcp"),
            ("prefer", "this is a comment"),
        ],
    )
    def test_comment_handling_for_expected_label(self, mode, expected_value):
        # Arrange
        rule = Rule(
            "rule line", 1, {"action": "accept", "protocol": "tcp", "comment": "this is a comment"}
        )
        # Act
        label = determine_rule_label(rule, mode)
        # Assert
        assert_that(label).is_equal_to(expected_value)
class TestRuleRendering:
    def test_rules_rendered_in_graph(self, rule_list_ordered_tests):
        tree = TreeMaker(rule_list_ordered_tests, []).make_tree()
        graph = Renderer(tree, [], show_legend=False).render_graph()
        assert_graph(graph).has_graph("root").has_rule().exactly(6)
class TestLinkRendering:
    def test_renders_link_with_label(self):
        parent = Chain("chain")
        from_rule = Rule("", 1, attributes={"action": "accept"})
        to_rule = Rule("", 2, attributes={"action": "accept"})
        parent.add_rule(from_rule)
        parent.add_rule(to_rule)
        link = Link(from_rule, to_rule)
        link_node = LinkNode(link)
        link.label = "label"
        result = link_node.render(0)
        assert_that(result).is_equal_to(
            f"detached:chain:rule1 {LINK_STYLE_NORMAL}|label| detached:chain:rule2"
        )
    def test_renders_link_without_label(self):
        parent = Chain("chain")
        from_rule = Rule("", 1, attributes={"action": "accept"})
        to_rule = Rule("", 2, attributes={"action": "accept"})
        parent.add_rule(from_rule)
        parent.add_rule(to_rule)
        link = Link(from_rule, to_rule)
        link_node = LinkNode(link)
        result = link_node.render(0)
        assert_that(result).is_equal_to(
            f"detached:chain:rule1 {LINK_STYLE_NORMAL} detached:chain:rule2"
        )
    def test_render_empty_string_when_render_is_false(self):
        parent = Chain("chain")
        from_rule = Rule("", 1, attributes={"action": "accept"})
        to_rule = Rule("", 2, attributes={"action": "accept"})
        parent.add_rule(from_rule)
        parent.add_rule(to_rule)
        link = Link(from_rule, to_rule)
        link.render = False
        link_node = LinkNode(link)
        result = link_node.render(0)
        assert_that(result).is_empty()
    def test_render_link_with_specified_style(self):
        parent = Chain("chain")
        from_rule = Rule("", 1, attributes={"action": "accept"})
        to_rule = Rule("", 2, attributes={"action": "accept"})
        parent.add_rule(from_rule)
        parent.add_rule(to_rule)
        link = Link(from_rule, to_rule)
        link_node = LinkNode(link)
        link.style = "style"
        result = link_node.render(0)
        assert_that(result).is_equal_to("detached:chain:rule1 style detached:chain:rule2")
    def test_render_intersectional_links_with_invisible_style(self):
        from_rule = Rule("", 1, attributes={"action": "accept"})
        to_rule = Rule("", 2, attributes={"action": "accept"})
        link = Link(from_rule, to_rule)
        link_node = LinkNode(link)
        result = link_node.render(0)
        assert_that(result).is_equal_to(
            f"detached:detached:rule1 {LINK_STYLE_BETWEEN_SECTIONS}|to detached:detached| detached:detached:rule2"
        )
    @pytest.mark.parametrize(
        "match, count", [("raw:.*", 4), ("mangle:.*", 12), ("nat:.*", 4), ("filter:.*", 19)]
    )
    def test_ensure_all_links_are_rendered(self, default_tree_root, match, count):
        sut = Renderer(default_tree_root, [])
        graph = sut.render_graph()
        assert_graph(graph).has_link().matching_from(match).exactly(count)
    def test_renders_legend_links(self, default_tree_root):
        sut = Renderer(default_tree_root, [])
        graph = sut.render_graph()
        assert_graph(graph).has_link("legend").with_to("raw").with_style(LINK_STYLE_INVISIBLE)
        assert_graph(graph).has_link("legend").with_to("mangle").with_style(LINK_STYLE_INVISIBLE)
        assert_graph(graph).has_link("legend").with_to("nat").with_style(LINK_STYLE_INVISIBLE)
        assert_graph(graph).has_link("legend").with_to("filter").with_style(LINK_STYLE_INVISIBLE)
class TestCollapse:
    def test_adds_collapse_style(self, default_tree_root):
        # Arrange
        sut = Renderer(default_tree_root, [GraphSelector("nat", mod="%")])
        # Act
        graph = sut.render_graph()
        # Assert
        assert_graph(graph).has_style("collapsed").and_then.has_graph()
        assert_graph(graph).has_graph(
            "legend", direct_descendants_only=False
        ).has_rule().with_label("*collapsed").at_depth(2)
    def test_replaces_collapsed_section_with_rule(self, default_tree_root):
        # Arrange
        sut = Renderer(default_tree_root, [GraphSelector("nat", mod="%")])
        # Act
        graph = sut.render_graph()
        # Assert
        assert_graph(graph).has_graph("root").has_rule().with_label("nat *collapsed").with_style(
            "collapsed"
        )
    def test_repoints_links_involving_collapsed_section(self, default_tree_root):
        # Arrange
        sut = Renderer(default_tree_root, [GraphSelector("nat", mod="%")])
        # Act
        graph = sut.render_graph()
        # Assert
        # mangle:prerouting:rule1 -.->|to dstnat| nat:dstnat:rule2
        assert_graph(graph).has_link("mangle:prerouting:rule1").with_label("to nat:dstnat").with_to(
            "nat:collapsedrule33"
        )
        # mangle:postrouting:rule19 -.->|to srcnat| nat:srcnat:rule20
        assert_graph(graph).has_link("mangle:postrouting:rule19").with_label(
            "to nat:srcnat"
        ).with_to("nat:collapsedrule33")
        # nat:dstnat:rule2 -.->|to input| filter:input:rule5
        assert_graph(graph).has_link("nat:collapsedrule33").with_label("to mangle:input").with_to(
            "mangle:input:rule3"
        )
        # nat:dstnat:rule2 -.->|to forward| filter:forward:rule11
        assert_graph(graph).has_link("nat:collapsedrule33").with_label("to mangle:forward").with_to(
            "mangle:forward:rule9"
        )
    def test_replaced_collapsed_chain_with_rule(self, default_tree_root):
        # Arrange
        sut = Renderer(default_tree_root, [GraphSelector("nat:dstnat", mod="%")])
        # Act
        graph = sut.render_graph()
        # Assert
        assert_graph(graph).has_style("collapsed")
        assert_graph(graph).has_graph("root").has_graph("nat").has_rule().with_label(
            "dstnat *collapsed"
        ).with_style("collapsed")
    def test_splat_and_collapsed_chain_should_work_together(self, default_tree_root):
        # Arrange
        sut = Renderer(default_tree_root, [GraphSelector("nat:dstnat", mod="*%")])
        # Act
        graph = sut.render_graph()
        # Assert
        assert_graph(graph).has_graph("root").has_rule().with_label(
            "nat:dstnat *collapsed"
        ).with_style("collapsed")
    def test_repoints_links_involving_collapsed_chain(self, default_tree_root):
        # Arrange
        sut = Renderer(default_tree_root, [GraphSelector("nat:dstnat", mod="%")])
        # Act
        graph = sut.render_graph()
        # Assert
        # mangle:prerouting:rule1 -.->|to dstnat| nat:dstnat:rule2
        assert_graph(graph).has_link("mangle:prerouting:rule1").with_label("to nat:dstnat").with_to(
            "nat:dstnat:collapsedrule33"
        )
        # nat:dstnat:rule2 -.->|to input| filter:input:rule5
        assert_graph(graph).has_link("nat:dstnat:collapsedrule33").with_label(
            "to mangle:input"
        ).with_to("mangle:input:rule3")
        # nat:dstnat:rule2 -.->|to forward| filter:forward:rule11
        assert_graph(graph).has_link("nat:dstnat:collapsedrule33").with_label(
            "to mangle:forward"
        ).with_to("mangle:forward:rule9")
    def test_repoints_links_when_when_both_from_and_to_are_collapsed(self, default_rule_list):
        # Arrange
        selector = [
            GraphSelector("mangle:prerouting", mod="*%"),
            GraphSelector("nat:dstnat", mod="*%"),
            GraphSelector(":", mod="-"),
        ]
        tree = TreeMaker(default_rule_list, selector).make_tree()
        sut = Renderer(tree, selector)
        # Act
        graph = sut.render_graph()
        # Assert
        # mangle:prerouting -.->|to dstnat| nat:dstnat
        assert_graph(graph).has_link().matching_from("mangle:prerouting").matching_to("nat:dstnat")
    def test_links_to_non_collapsed_sister_chain_not_modified(self, default_tree_root):
        # Arrange
        sut = Renderer(default_tree_root, [GraphSelector("nat:dstnat", mod="%")])
        # Act
        graph = sut.render_graph()
        # Assert
        # mangle:postrouting:rule19 -.->|to srcnat| nat:srcnat:rule20
        assert_graph(graph).has_link("mangle:postrouting:rule19").with_label(
            "to nat:srcnat"
        ).with_to("nat:srcnat:rule20")
    def test_drop_links_from_and_to_collapsed_node(self, default_tree_root):
        # Arrange
        sut = Renderer(default_tree_root, [GraphSelector("filter:forward", mod="%")])
        # Act
        graph = sut.render_graph()
        # Assert
        with pytest.raises(AssertionFailure):
            assert_graph(graph).has_link("filter:forward:collapsedrule").with_to(
                "filter:forward:collapsedrule"
            )
class TestCollapseAsRule:
    def test_adds_collapse_style(self, default_tree_root):
        # Arrange
        sut = Renderer(default_tree_root, [GraphSelector("nat", mod="%")])
        # Act
        graph = sut.render_graph()
        # Assert
        assert_graph(graph).has_style("collapsed").and_then.has_graph()
        assert_graph(graph).has_graph(
            "legend", direct_descendants_only=False
        ).has_rule().with_label("*collapsed").at_depth(2)
    def test_replaces_collapsed_section_with_rule(self, default_tree_root):
        # Arrange
        sut = Renderer(default_tree_root, [GraphSelector("filter", mod="%")], collapse_as_rule=True)
        # Act
        graph = sut.render_graph()
        # Assert
        assert_graph(graph).has_graph("root").has_graph("mangle").has_rule().matching_label(
            r"filter.*collapsed"
        ).with_style("collapsed").count(5)
    def test_ensure_collapse_rule_inserted_before_link_end_target_when_it_is_start_of_link(
        self, default_tree_root
    ):
        # Arrange
        sut = Renderer(default_tree_root, [GraphSelector("filter", mod="%")], collapse_as_rule=True)
        # Act
        graph = sut.render_graph()
        # Assert
        assert_graph(graph).has_graph("mangle:postrouting", direct_descendants_only=False).has_rule(
            "filter:collapsedrule36"
        ).and_then.has_rule("mangle:postrouting:rule19")
    def test_ensure_collapse_rule_inserted_after_link_start_target_when_it_is_end_of_link(
        self, default_tree_root
    ):
        # Arrange
        sut = Renderer(default_tree_root, [GraphSelector("filter", mod="%")], collapse_as_rule=True)
        # Act
        graph = sut.render_graph()
        # Assert
        assert_graph(graph).has_graph("root").has_graph(
            "mangle:input", direct_descendants_only=False
        ).has_rule("mangle:input:rule3").followed_by.has_rule("filter:collapsedrule33")
    def test_rule_label_shows_chain_name_when_collapsed(self, default_tree_root):
        # Arrange
        sut = Renderer(
            default_tree_root, [GraphSelector("filter:", mod="%")], collapse_as_rule=True
        )
        # Act
        graph = sut.render_graph()
        # Assert
        assert_graph(graph).has_graph(direct_descendants_only=False).has_rule().with_label(
            "filter:forward *collapsed"
        )
        assert_graph(graph).has_graph(direct_descendants_only=False).has_rule().with_label(
            "filter:input *collapsed"
        )
        assert_graph(graph).has_graph(direct_descendants_only=False).has_rule().with_label(
            "filter:output *collapsed"
        )
    def test_replace_collapsed_chain_with_rules(self, default_tree_root):
        # Arrange
        sut = Renderer(
            default_tree_root,
            [GraphSelector("filter:forward", mod="%")],
            collapse_as_rule=True,
        )
        # Act
        graph = sut.render_graph()
        # Assert
        assert_graph(graph).has_graph(
            "mangle:postrouting", direct_descendants_only=False
        ).has_rule().with_label("filter:forward *collapsed").with_style(
            "collapsed"
        ).followed_by.has_rule().with_label(
            "fasttrack"
        )
        assert_graph(graph).has_graph(
            "mangle:forward", direct_descendants_only=False
        ).has_rule().with_label("disabled rule").followed_by.has_rule().with_label(
            "filter:forward *collapsed"
        ).with_style(
            "collapsed"
        )
        assert_graph(graph).has_graph(
            "filter:jump-chain", direct_descendants_only=False
        ).has_rule().with_label("filter:forward *collapsed").with_style(
            "collapsed"
        ).followed_by.has_rule().followed_by.has_rule().with_label(
            "filter:forward *collapsed"
        ).with_style(
            "collapsed"
        )
        assert_graph(graph).has_graph(
            "filter:terminal-chain", direct_descendants_only=False
        ).has_rule().with_label("filter:forward *collapsed").with_style(
            "collapsed"
        ).followed_by.has_rule()
class TestLinkLabel:
    def test_label_uses_combined_parent_names_when_jumps_to_chain_in_different_section(self):
        # Arrange
        section = Section("section")
        chain = section.get_or_add_chain("chain")
        rule = Rule("", 0, {})
        # Act
        label = determine_link_label(Link(rule, chain))
        # Assert
        assert_that(label).is_equal_to("to section:chain")
    def test_label_uses_combined_parent_names_when_jumps_to_rule_of_different_section(self):
        # Arrange
        section = Section("section")
        chain = section.get_or_add_chain("chain")
        rule = Rule("", 0, {})
        end_rule = Rule("", 1, {})
        chain.add_rule(end_rule)
        # Act
        label = determine_link_label(Link(rule, end_rule))
        # Assert
        assert_that(label).is_equal_to("to section:chain")
================================================

File: test_tree.py
================================================
from firewall2mermaid.common import LINK_STYLE_INVISIBLE
from firewall2mermaid.model import GraphSelector, ParserRule, RootNode, Rule
from firewall2mermaid.tree import TreeMaker
from assertpy import assert_that
def assert_links_to(tree: RootNode, from_id: str, to_node_id: str, style: str | None = None):
    node = next((x for x in tree.sections if x.id == from_id), None)
    if not node:
        node = next((x for x in tree.chains if x.id == from_id), None)
    if not node:
        node = next((x for x in tree.rules if x.id == from_id), None)
    assert node
    if style:
        assert_that([(link.end.id, link.style) for link in node.links]).described_as(
            f"chain {from_id} contains link to {to_node_id} with style {style}"
        ).contains((to_node_id, style))
    else:
        assert_that([link.end.id for link in node.links]).described_as(
            f"chain {from_id} contains link to {to_node_id}"
        ).contains(to_node_id)
def assert_rule_links_to(tree: RootNode, rule_id: str, to_node_id: str):
    rule = next((x for x in tree.rules if x.id == rule_id), None)
    assert rule
    assert_that(rule.links).described_as(
        f"rule {rule_id} contains link to {to_node_id}"
    ).extracting("end").extracting("id").contains(to_node_id)
class TestBasics:
    def test_make_tree_when_using_default_rules_set_when_not_using_filters_default_sections_are_present_in_tree(
        self, default_tree_root: RootNode
    ):
        tree = default_tree_root
        assert_that(tree.sections).is_length(4).extracting("name").contains_only(
            "raw", "mangle", "filter", "nat"
        )
        assert_that(tree.sections).extracting("tree_root").contains_only(tree)
        assert_that(tree.sections).extracting("parent").contains_only(tree)
    def test_make_tree_when_using_default_rules_set_when_not_using_filters_default_chains_are_present_in_tree(
        self, default_tree_root: RootNode
    ):
        tree = default_tree_root
        assert_that(tree.chains).is_length(18).extracting("name").contains(
            "prerouting", "srcnat", "dstnat", "input", "output"
        )
        assert_that(tree.chains).extracting("tree_root").contains_only(tree)
    def test_make_tree_when_using_default_rules_set_when_not_using_filters_default_rules_are_present_in_tree(
        self, default_tree_root: RootNode
    ):
        tree = default_tree_root
        assert_that(tree.rules).is_length(length=32).extracting("tree_root").contains_only(tree)
    def test_make_tree_when_using_section_filter_filter_section_elements(
        self, default_rule_list: list[ParserRule]
    ):
        sut = TreeMaker(default_rule_list, elements=[GraphSelector("filter")])
        tree = sut.make_tree()
        assert_that(tree.sections).extracting("name").contains("filter")
        section = tree.sections[0]
        assert_that(tree.chains).extracting("parent").contains(section)
    def test_make_tree_when_using_chains_filter_elements_for_filtered_chain(
        self, default_rule_list: list[ParserRule]
    ):
        sut = TreeMaker(default_rule_list, elements=[GraphSelector(":input")])
        tree = sut.make_tree()
        assert_that(tree.sections).extracting("name").contains("filter", "mangle")
        assert_that(tree.chains).extracting("name").contains("input", "terminal-chain")
        assert_that(tree.rules).extracting("chain").contains("input", "terminal-chain")
    def test_make_tree_when_prune_disabled_rules_is_true_disabled_rules_are_removed(
        self, default_rule_list: list[ParserRule]
    ):
        sut = TreeMaker(default_rule_list, elements=[], prune_disabled_rules=True)
        tree = sut.make_tree()
        assert_that(tree.rules).extracting("disabled").does_not_contain("yes")
        assert_that(tree.rules).is_not_empty()
    def test_make_tree_when_prune_log_rules_is_true_log_rules_are_removed(
        self, default_rule_list: list[ParserRule]
    ):
        sut = TreeMaker(default_rule_list, elements=[], prune_log_rules=True)
        tree = sut.make_tree()
        assert_that(tree.rules).extracting("action").does_not_contain("log")
    def test_make_tree_rules_index_follows_order_in_file(
        self, rule_list_ordered_tests: list[ParserRule]
    ):
        sut = TreeMaker(rule_list_ordered_tests, elements=[])
        tree = sut.make_tree()
        for rule in tree.rules:
            assert_that(str(rule.index)).is_equal_to(rule.comment)
    def test_make_tree_when_selector_has_remove_prune_elements(
        self, default_rule_list: list[ParserRule]
    ):
        sut = TreeMaker(
            default_rule_list,
            elements=[
                GraphSelector("nat:dstnat", "-"),
                GraphSelector("nat"),
                GraphSelector("filter", mod="-"),
            ],
        )
        tree = sut.make_tree()
        assert_that(tree.sections).extracting("name").does_not_contain("filter")
        assert_that(tree.sections).extracting("name").contains("nat")
        assert_that(tree.chains).extracting("id").does_not_contain("nat:dstnat")
    def test_multiple_selector_picks_first_one(self, default_rule_list: list[ParserRule]):
        sut = TreeMaker(
            default_rule_list,
            elements=[
                GraphSelector("nat:dstnat", "+"),
                GraphSelector("nat:dstnat", "-"),
            ],
        )
        tree = sut.make_tree()
        assert_that(tree.sections).extracting("name").contains("nat")
        assert_that(tree.chains).extracting("id").contains("nat:dstnat")
class TestLinking:
    def test_make_tree_when_using_default_rules_set_rules_are_wired_in_chains_based_on_rule_index(
        self, default_tree_root: RootNode
    ):
        # Act
        tree = default_tree_root
        # Assert
        section = tree.section("filter")
        assert section
        chain = section.chain("rule-order")
        assert chain
        rules = {x.comment: x for x in chain.rules}
        assert_rule_links_to(tree, rules["1"].id, rules["2"].id)
        assert_rule_links_to(tree, rules["2"].id, rules["3"].id)
        assert_rule_links_to(tree, rules["3"].id, rules["4"].id)
    def test_make_tree_when_using_default_rules_set_rules_are_wired_according_packet_flows(
        self, default_tree_root: RootNode
    ):
        tree = default_tree_root
        # prerouting
        assert_links_to(tree, "raw:prerouting", "mangle:prerouting")
        assert_links_to(tree, "mangle:prerouting", "nat:dstnat")
        # input
        assert_links_to(tree, "mangle:input", "filter:input")
        # forward
        assert_links_to(tree, "mangle:forward", "filter:forward")
        # output
        assert_links_to(tree, "raw:output", "mangle:output")
        assert_links_to(tree, "mangle:output", "filter:output")
        # postrouting
        assert_links_to(tree, "mangle:postrouting", "nat:srcnat")
    def test_make_tree_when_using_default_rules_set_jump_rules_links_to_target_in_chain(
        self, default_tree_root: RootNode
    ):
        tree = default_tree_root
        # find the rule
        section = tree.section("filter")
        assert section
        chain = section.chain("forward")
        assert chain
        rule: Rule = [
            x for x in chain.rules if x.action == "jump" and x.jump_target == "jump-chain"
        ][0]
        assert rule
        links = rule.links
        assert_that(links).is_length(1)
        target_chain = links[0].end.parent
        assert_that(target_chain).has_name("jump-chain").has_parent(rule.parent.parent)
    def test_implicit_returning_nodes_create_link_to_next_rule_in_parent_chain(
        self, default_tree_root: RootNode
    ):
        tree = default_tree_root
        section = tree.section("filter")
        assert section
        # target end rule
        return_chain = section.chain("forward")
        assert return_chain
        return_rule = [x for x in return_chain.rules if x.action != "jump"][2]
        assert return_rule
        # find the returning rule
        chain = section.chain("jump-chain")
        assert chain
        rule = chain.rules[-1]
        links = rule.links
        assert_that(links).is_length(1)
        assert_that(links[0].end).is_equal_to(return_rule)
    def test_make_tree_when_using_default_rules_set_terminal_node_in_flow_chain_has_link_to_next_section(
        self, default_tree_root: RootNode
    ):
        tree = default_tree_root
        # find the rule
        assert_links_to(tree, "filter:forward", "mangle:postrouting")
    def test_when_node_has_matchers_then_links_include_yes_no_label(
        self, default_tree_root: RootNode
    ):
        # Assert
        section = default_tree_root.section("filter")
        assert section
        chain = section.chain("input")
        assert chain
        rule: Rule = next(
            x for x in chain.rules if x.action == "jump" and x.jump_target == "terminal-chain"
        )
        links = rule.links
        assert_that(links).is_length(2)
        no_link = next(x for x in links if x.end.parent == chain)
        yes_link = next(x for x in links if x.end.parent != chain)
        # link to next rule has otherwise as label
        assert_that(no_link).has_label("otherwise")
        # rule to jump chain has if yes
        assert_that(yes_link).has_label("if yes")
    def test_when_start_node_is_return_link_has_return_as_label(self, default_tree_root: RootNode):
        # Assert
        section = default_tree_root.section("filter")
        assert section
        chain = section.chain("jump-chain")
        assert chain
        rule: Rule = next(x for x in chain.rules if x.action == "return")
        links = rule.links
        assert_that(links).is_length(2)
        return_link = next(x for x in links if x.end.parent != chain)
        # rule to jump chain has if yes
        assert_that(return_link).has_label("return")
    def test_when_start_node_nonterminal_end_node_link_has_return_as_label(
        self, default_tree_root: RootNode
    ):
        # Assert
        section = default_tree_root.section("filter")
        assert section
        chain = section.chain("jump-chain")
        assert chain
        rule: Rule = chain.rules[1]
        assert_that(rule.links[0]).has_label("return")
class TestAddFlowElements:
    def test_make_tree_when_add_flow_elements_is_true_when_using_filters_adds_flow_elements_that_connect_to_filtered_elements(
        self, add_flow_rule_list
    ):
        tree = TreeMaker(
            add_flow_rule_list, [GraphSelector("filter:input")], add_flow_elements=True
        ).make_tree()
        assert_that(tree.sections).extracting("name").contains_only(
            "raw", "mangle", "filter", "nat"
        )
        assert_that(tree.sections).extracting("parent").contains_only(tree)
    def test_make_tree_when_add_flow_elements_is_true_when_flow_elements_added_flow_chain_contains_dummy_rule(
        self, add_flow_rule_list
    ):
        tree = TreeMaker(
            add_flow_rule_list, [GraphSelector("filter:input")], add_flow_elements=True
        ).make_tree()
        section = tree.section("mangle")
        assert section
        chain = section.chain("prerouting")
        assert chain
        assert_that(chain.rules).extracting("comment").contains_only("rule added for packet flow")
    def test_flow_elements_links_in_flow_chains(self, default_rule_list):
        # Arrange
        sut = TreeMaker(default_rule_list, [], add_flow_elements=True)
        # Act
        tree = sut.make_tree()
        # Assert
        # pretouting flow - raw:prerouting -> mangle:prerouting -> nat:dstnat
        assert_links_to(tree, "raw:prerouting", "mangle:prerouting")
        assert_links_to(tree, "mangle:prerouting", "nat:dstnat")
        # input flow - mangle:input -> filter:input
        assert_links_to(tree, "mangle:input", "filter:input")
        # forward flow - mangle:forward -> filter:forward
        assert_links_to(tree, "mangle:forward", "filter:forward")
        # output flow - raw:output -> mangle:output -> filter:output
        assert_links_to(tree, "raw:output", "mangle:output")
        assert_links_to(tree, "mangle:output", "filter:output")
        # postrouting flow - mangle:postrouting -> nat:srcnat
        assert_links_to(tree, "mangle:postrouting", "nat:srcnat")
    def test_flow_elements_links_between_flow_chains(self, default_rule_list):
        # Arrange
        sut = TreeMaker(default_rule_list, [], add_flow_elements=True)
        # Act
        tree = sut.make_tree()
        # Assert
        # prerouting -> input
        assert_links_to(tree, "nat:dstnat", "mangle:input", LINK_STYLE_INVISIBLE)
        assert_links_to(tree, "nat:dstnat:rule2", "mangle:input:rule3")
        # prerouting -> forward
        assert_links_to(tree, "nat:dstnat", "mangle:forward", LINK_STYLE_INVISIBLE)
        assert_links_to(tree, "nat:dstnat:rule2", "mangle:forward:rule9")
        # forward -> postrouting
        assert_links_to(tree, "filter:forward", "mangle:postrouting", LINK_STYLE_INVISIBLE)
        assert_links_to(tree, "filter:forward:rule15", "mangle:postrouting:rule19")
        # output -> postrouting
        assert_links_to(tree, "filter:output", "mangle:postrouting", LINK_STYLE_INVISIBLE)
        assert_links_to(tree, "filter:output:rule18", "mangle:postrouting:rule19")
    def test_ensure_all_flow_element_depending_on_graph_chain(self, add_flow_rule_list):
        tree = TreeMaker(
            add_flow_rule_list,
            [GraphSelector("filter:input"), GraphSelector(":", "-")],
            add_flow_elements=True,
        ).make_tree()
        assert_that(tree.chains).extracting("id").contains_only(
            "raw:prerouting", "mangle:prerouting", "nat:dstnat", "mangle:input", "filter:input"
        )
    def test_ensure_all_flow_element_linked_properly(self, add_flow_rule_list):
        tree = TreeMaker(
            add_flow_rule_list, [GraphSelector("filter:input")], add_flow_elements=True
        ).make_tree()
        # Assert
        # raw ->|prerouting| mangle ->|dstnat| nat ->|input| mangle ->|input| filter
        assert_links_to(tree, "raw:prerouting:rule3", "mangle:prerouting:rule4")
        assert_links_to(tree, "mangle:prerouting:rule4", "nat:dstnat:rule2")
        assert_links_to(tree, "nat:dstnat:rule2", "mangle:input:rule5")
        assert_links_to(tree, "mangle:input:rule5", "filter:input:rule0")