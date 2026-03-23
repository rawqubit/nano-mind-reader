"""Tests for nano-mind-reader.
main.py imports torch at module level; torch is too large for CI.
Tests only verify Python syntax and module structure.
"""
import sys
import subprocess
import pytest


def test_main_compiles():
    r = subprocess.run(
        [sys.executable, "-m", "py_compile", "main.py"],
        capture_output=True, text=True
    )
    assert r.returncode == 0, f"Syntax error in main.py:\n{r.stderr}"
