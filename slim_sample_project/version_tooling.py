import importlib_metadata as metadata
import version as v

try:
    VERSION = metadata.version(__name__)
except metadata.PackageNotFoundError:
    # package is not installed, try reading from slim_sample_project script
    VERSION = v.__version__ if v.__version__ else "unset"
