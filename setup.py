import os
import setuptools
import sys

if sys.version_info < (3, 6):
    raise ImportError("MDLN requires Python 3.6 or later.")

about = {}
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "mdln", "__about__.py"), "r") as f:
    exec(f.read(), about)

setuptools.setup(
    name=about.get("__title__"),
    version=about.get("__version__"),
    author=about.get("__author__"),
    description=about.get("__doc__").replace("\n", " ").strip(),
    license=about.get("__license__"),
    keywords="mdln game engine pygame entity component framework",
    url="https://github.com/qwertyquerty/MDLN",
    packages=["mdln"],
    python_requires=">=3.6",
    project_urls={
        "Documentation": "https://github.com/qwertyquerty/MDLN",
    },
    install_requires = [
        "pygame>=2.2.0, <3",
        "pyyaml==6.0"
    ]
)
