def hello() -> str:
    return "Hello from github-actions-with-python!"

from . import _version
__version__ = _version.get_versions()['version']
