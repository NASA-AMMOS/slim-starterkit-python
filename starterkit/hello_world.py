# Sample code: REPLACE with project code.
import os
import sys

from api.text_processor import TextWriter
import importlib_metadata as metadata
import starterkit.version as v

try:
    version = metadata.version(__name__)
except metadata.PackageNotFoundError:
    # package is not installed, try reading from starterkit script
    version = v.__version__ if v.__version__ else "unset"
    pass


def main():
    """
    Top-level method executed at application runtime.
    """
    w = TextWriter()
    w.out("Hello World!")
    w.out(version)
    print("EXITING!")
    sys.exit(os.EX_OK)


if __name__ == "__main__":
    main()
