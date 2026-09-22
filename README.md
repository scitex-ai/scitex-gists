# scitex-gists

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>SigmaPlot macro printers — version-controlled VB-style macros emitted from Python.</b></p>

<p align="center">
  <a href="https://scitex-gists.readthedocs.io/">Full Documentation</a> · <code>uv pip install scitex-gists[all]</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-gists/"><img src="https://img.shields.io/pypi/v/scitex-gists?label=pypi" alt="pypi"></a>
  <a href="https://pypi.org/project/scitex-gists/"><img src="https://img.shields.io/pypi/pyversions/scitex-gists?label=python" alt="python"></a>
  <a href="https://github.com/scitex-ai/scitex-gists/actions/workflows/rtd-sphinx-build-on-ubuntu-latest.yml"><img src="https://img.shields.io/github/actions/workflow/status/scitex-ai/scitex-gists/rtd-sphinx-build-on-ubuntu-latest.yml?branch=develop&label=docs" alt="docs"></a>
  <a href="https://scitex-gists.readthedocs.io/en/latest/"><img src="https://img.shields.io/readthedocs/scitex-gists?label=docs" alt="docs-rtd"></a>
</p>
<p align="center">
  <a href="https://github.com/scitex-ai/scitex-gists/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/scitex-ai/scitex-gists/ci.yml?branch=develop&label=tests" alt="tests"></a>
  <a href="https://github.com/scitex-ai/scitex-gists/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/scitex-ai/scitex-gists/ci.yml?branch=develop&label=install-check" alt="install-check"></a>
  <a href="https://codecov.io/gh/scitex-ai/scitex-gists"><img src="https://img.shields.io/codecov/c/github/scitex-ai/scitex-gists/develop?label=cov" alt="cov"></a>
</p>
<!-- scitex-badges:end -->

---

## Problem and Solution

| # | Problem | Solution |
|---|---------|----------|
| 1 | **Unversioned macros** — SigmaPlot v12 macro files live on one lab machine, outside version control | **Python prints the macro** — `sigmacro_process_figure_s()` emits VB-style macro text; copy-paste into SigmaPlot editor; macros are now part of the repo |

## Quick Start

```python
from scitex_gists import sigmacro_process_figure_s, sigmacro_to_blue

sigmacro_process_figure_s()   # prints the figure-processing macro
sigmacro_to_blue()            # prints the color macro
```

## Demo

```mermaid
flowchart LR
    A["python -c 'from scitex_gists import sigmacro_process_figure_s; sigmacro_process_figure_s()'"]
        --> B["VB macro printed to stdout"]
    B --> C["copy / pipe to clipboard"]
    C --> D["paste into SigmaPlot v12<br/>macro editor"]
    D --> E["run macro on figure"]
```

<p align="center"><sub><b>Figure 1.</b> Demo path. One call emits the macro to stdout; pipe it to the clipboard and paste into the SigmaPlot editor.</sub></p>

```bash
$ python -c "from scitex_gists import sigmacro_to_blue; sigmacro_to_blue()" | pbcopy
# now paste into the SigmaPlot macro editor and run
```

## Installation

```bash
uv pip install "scitex-gists[all]"
```

<details>
<summary><b>Per-module extras</b></summary>

<br>

| Extra | Pulls in |
|---|---|
| `all` | `dev` + `docs` (recommended) |
| `dev` | pytest, pytest-cov |
| `docs` | Sphinx + RTD theme + myst-parser (docs build only) |

```bash
uv pip install -e ".[dev]"               # editable install for contributors
```

</details>
## Architecture

```mermaid
flowchart LR
    Init[scitex_gists __init__] --> A[sigmacro_process_figure_s]
    Init --> B[sigmacro_to_blue]
    Init --> Skills[_skills pages]
    A --> Out[(stdout VB macro)]
    B --> Out
    Out --> Clip[copy / clipboard]
    Clip --> SP[SigmaPlot macro editor]
```

<p align="center"><sub><b>Figure 2.</b> Module layout. Both emitters write VB macro text to stdout; agent skill pages re-export the same entry points.</sub></p>

A two-function library: each `_SigMacro_*.py` module wraps a
multi-line VB-style macro string and a stdout emitter helper. Adding a new
macro = add a new `_SigMacro_<name>.py` and re-export from
`__init__.py`.

## 1 Interfaces

<details open>
<summary><strong>Python API</strong></summary>

<br>

```python
from scitex_gists import sigmacro_process_figure_s, sigmacro_to_blue

sigmacro_process_figure_s()
sigmacro_to_blue()
```

Each function prints VB-style macro text to stdout. Pipe into your
clipboard or redirect to a file, then paste into the SigmaPlot macro
editor.

</details>

## Part of SciTeX

`scitex-gists` is part of [**SciTeX**](https://scitex.ai). Install via
the umbrella with `pip install scitex[gists]` to use as
`scitex.gists` (Python) or `scitex gists ...` (CLI).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
