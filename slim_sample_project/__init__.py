# Sample code: REPLACE with project code.
from pathlib import Path
import sys

# extend PYTHONPATH
path_update = ['.', str(Path(__file__).resolve().parent)]
for p in path_update:
    if p not in sys.path:
        sys.path.append(p)

try:  # module import
    from version import __version__
except ImportError:  # package import
    from .version import __version__


IGNORE = True
