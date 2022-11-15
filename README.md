## slim-starterkit-python
Template for a basic [Python](https://www.python.org/) application implementing build, release and publish automation using [GitHub actions](https://github.com/features/actions).
### Modern build tooling
This repository presents a project template that implements recent recommendations for Python build tooling based on [PEP-517](https://peps.python.org/pep-0517/) and [PEP-518](https://peps.python.org/pep-0518/) standards. 
### Significant Components
- `pyproject.toml`: A [TOML](https://toml.io/en/)-based pre-build configuration file that sets system requirements and specifies a build system implementation. (**No editing necessary.**)
- `setup.cfg`: [Setup Tools](https://pypi.org/project/setuptools/) build-system specific configuration file. (**Must be edited and customized for a new application.**)
- `version.py`: Both hand editable and automatically updated version file. (**Release version must be specified here immediately before tag.**)
- `starterkit` directory: The root of source code. (**Simply rename or replace this directory with project source code.**)
- `.github/workflows/python-publish.yml`: The GitHub action descriptor that specifies build steps for build, release and publish automation. (**The text `--repository testpypi` must be removed from the last line to publish to the [production PyPi](https://pypi.org/) [versus [testPyPi](https://test.pypi.org/)].**)
### Notable features
For flexibility, this template contains a standalone, deprecated `setup.py` Python file that mimics older build system features not be available in current, modern build implementation. Examples include running `python3 setup.py --version` to obtain the application version at the command line.
- [View build, release and deploy execution logs in the Actions tab.](https://github.com/NASA-AMMOS/slim-starterkit-python/actions)
## Build, Release and Deploy instructions
### Check application version
Note that this will increment the version file should the repo contain file updates or the current tag is not at the tip of repo history.
```
python3 -m setuptools_scm
```
... or ... 
```
python3 setup.py --version
```
### Install build tooling
```
pip3 install --upgrade build setuptools_scm twine wheel
```
### Install product requirements
``` 
pip3 --exists-action w install -r requirements.txt
```
### Install an editable Pip build
This is based on [Pip tooling](https://pypi.org/project/pip/).
``` 
pip install -e
```
### Clean previous builds
``` 
rm -r build dist __pycache__ *.egg* .egg* ; git checkout <product_name>/version.py ; pip3 uninstall <product_name> -y
```
... so for the template, this would be ...
``` 
rm -r build dist __pycache__ *.egg* .egg* ; git checkout starterkit/version.py ; pip3 uninstall starterkit -y
```
### Build and release product
1. Manually update <product_name>/version.py, commit and push:
``` 
git add starterkit/version.py && git commit -m "Issue #<issue_number>: Updated version for release." && git push
```
2. Tag using either [web ui on github main branch](https://github.com/NASA-AMMOS/slim-starterkit-python/releases/new) or git cli: 
``` 
git tag -a -m "Issue #<issue_number>: Release version <version>" <version>
```
**Note:** The `<version>` must match that in the `<product_name>/version.py` file.
3. Package the product:
- Package an `sdist` and a `tarball`: (traditional)
``` 
git checkout <product_name>/version.py && python3 -m build --wheel
```
- ... or package an `sdist` and a `zip` ...
``` 
python3 -m build --wheel && python3 setup.py sdist --format=zip
```
### Publish product
[Twine](https://twine.readthedocs.io/en/latest/) is used to publish to PyPi.
``` 
twine check dist/* && twine upload --verbose
```
... or as a ZIP ...
``` 
twine check dist/* && twine upload --verbose dist/*.whl dist/*.zip
```
### Test release locally
A simplified build and release workflow is available for testing locally.
``` 
python3 -m build --wheel && python3 setup.py sdist --format=zip
pip3 install <product_name> --no-index --find-links file:///<path_to_repo>/dist/
```
## GitHub automation
The [GitHub Action descriptor](https://github.com/NASA-AMMOS/slim-starterkit-python/blob/main/.github/workflows/python-publish.yml) runs through all the release products automatically when it detects a tag or release on the product repo.