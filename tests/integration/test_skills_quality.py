"""Enforces SciTeX skills quality checklist §1–§4."""

# PS-206b: import-smoke-allowed — this module ships no `def test_*`
# functions of its own; it registers factory-built cases
# (`make_skill_quality_tests`) whose assertions live in scitex-dev.

from pathlib import Path

import pytest

pytest.importorskip("scitex_dev")
from scitex_dev._skills_quality_pytest import make_skill_quality_tests  # noqa: E402

test_skills_quality = make_skill_quality_tests(
    package_root=Path(__file__).resolve().parents[2]
)
