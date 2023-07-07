import setuptools
import sys

if sys.version_info < (3, 6):
    raise ImportError("MDLN requires Python 3.6 or later.")

import mdln

setuptools.setup(
    name="mdln",
    version=mdln.__version__,
    author=mdln.__author__,
    description=mdln.__doc__.replace("\n", " ").strip(),
    license="MIT",
    keywords="mdln game engine pygame entity component framework",
    url="https://github.com/qwertyquerty/MDLN",
    packages=["mdln"],
    test_suite="test",
    python_requires=">=3.6",
    project_urls={
        "Documentation": "https://github.com/qwertyquerty/MDLN",
    },
    install_requires = [
        "pygame>=2.2.0, <3",
        "pyyaml==6.0"
    ]
)
