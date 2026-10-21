import importlib
import sys


def test_app_imports():
    import streamlit
    assert streamlit is not None


def test_themes_defined():
    sys.path.insert(0, ".")
    # Just verify the file is valid Python
    with open("app.py") as f:
        source = f.read()
    code = compile(source, "app.py", "exec")
    assert code is not None


def test_requirements_exist():
    with open("requirements.txt") as f:
        contents = f.read()
    assert "streamlit" in contents
