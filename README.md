<!-- Header block for project -->
<hr>

<div align="center">

[INSERT YOUR LOGO IMAGE HERE (IF APPLICABLE)]
<!-- ☝️ Replace with your logo (if applicable) via ![](https://uri-to-your-logo-image) ☝️ -->
<!-- ☝️ If you see logo rendering errors, make sure you're not using indentation, or try an HTML IMG tag -->

<h1 align="center">[INSERT YOUR REPO / PROJ NAME HERE]</h1>
<!-- ☝️ Replace with your repo name ☝️ -->

</div>

<pre align="center">[INSERT A SINGLE SENTENCE DESCRIBING THE PURPOSE OF YOUR REPO / PROJ]</pre>
<!-- ☝️ Replace with a single sentence describing the purpose of your repo / proj ☝️ -->

<!-- Header block for project -->

[INSERT YOUR BADGES HERE (SEE: https://shields.io)] [![SLIM](https://img.shields.io/badge/Best%20Practices%20from-SLIM-blue)](https://nasa-ammos.github.io/slim/)
<!-- ☝️ Add badges via: https://shields.io e.g. ![](https://img.shields.io/github/your_chosen_action/your_org/your_repo) ☝️ -->

[INSERT SCREENSHOT OF YOUR SOFTWARE, IF APPLICABLE]
<!-- ☝️ Screenshot of your software (if applicable) via ![](https://uri-to-your-screenshot) ☝️ -->

[INSERT MORE DETAILED DESCRIPTION OF YOUR REPOSITORY HERE]
<!-- ☝️ Replace with a more detailed description of your repository, including why it was made and whom its intended for.  ☝️ -->

[INSERT LIST OF IMPORTANT PROJECT / REPO LINKS HERE]
<!-- example links>
[Website](INSERT WEBSITE LINK HERE) | [Docs/Wiki](INSERT DOCS/WIKI SITE LINK HERE) | [Discussion Board](INSERT DISCUSSION BOARD LINK HERE) | [Issue Tracker](INSERT ISSUE TRACKER LINK HERE)
-->

## Features

* [INSERT LIST OF FEATURES IMPORTANT TO YOUR USERS HERE]
* Python build tooling based on PEP-517 and PEP-518 standards
* Build, release and publish automation takes place automatically using GitHub Actions. 
  
<!-- ☝️ Replace with a bullet-point list of your features ☝️ -->

## Contents

* [Quick Start](#quick-start)
* [Changelog](#changelog)
* [FAQ](#frequently-asked-questions-faq)
* [Contributing Guide](#contributing)
* [License](#license)
* [Support](#support)

## Quick Start

This guide provides a quick way to get started with our project. Please see our [docs]([INSERT LINK TO DOCS SITE / WIKI HERE]) for a more comprehensive overview.

### Requirements

1. [INSERT LIST OF REQUIREMENTS HERE]
  
<!-- ☝️ Replace with a numbered list of your requirements, including hardware if applicable ☝️ -->

#### Build System Requirements
Certain properties and permission settings are necessary in GitHub for builds to run automatically. On local development systems builds may be tested in similar fashion with proper tooling installed.

##### Required repository settings
1. [Shared PyPi API Token](https://test.pypi.org/help#apitoken) installed in [GitHub Repository Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository) named `PYPI_API_TOKEN`.
2. Permissions to [execute GitHub Actions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#managing-github-actions-permissions-for-your-repository) and [perform software tag and release](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-personal-account-settings/permission-levels-for-a-personal-account-repository#collaborator-access-for-a-repository-owned-by-a-personal-account).
<!-- ☝️ If necessary, update with a numbered list of your build requirements, including hardware if applicable ☝ -->

##### Required local tooling
1. Build tooling modules
```
pip3 install --upgrade build setuptools_scm twine wheel
```
2. Product required modules (`requirements.txt`)
``` 
pip3 --exists-action w install -r requirements.txt
```  
<!-- ☝️ If necessary, update with a numbered list of your build requirements, including hardware if applicable ☝ -->

### Setup Instructions

1. [INSERT STEP-BY-STEP SETUP INSTRUCTIONS HERE, WITH OPTIONAL SCREENSHOTS]
   
<!-- ☝️ Replace with a numbered list of how to set up your software prior to running ☝️ -->

### Run Instructions

1. [INSERT STEP-BY-STEP RUN INSTRUCTIONS HERE, WITH OPTIONAL SCREENSHOTS]

<!-- ☝️ Replace with a numbered list of your run instructions, including expected results ☝️ -->

### Usage Examples

* [INSERT LIST OF COMMON USAGE EXAMPLES HERE, WITH OPTIONAL SCREENSHOTS]

<!-- ☝️ Replace with a list of your usage examples, including screenshots if possible, and link to external documentation for details ☝️ -->

### Build Instructions
A [GitHub Action](.github/workflows/python-publish.yml) configuration specifies the series of commands to release and publish the product. Commands are staged and carried out automatically when a tagged release is published to the main branch.

#### Automated Build Kickoff
1. Edit the `[INSERT YOUR PACKAGE NAME]/version.py` file with the next release version using the web UI on GitHub `main` branch.
2. [Perform a release](releases/new) using the web UI on GitHub `main` branch
3. Build, packaging and release to PyPi will execute automatically using [GitHub Actions Workflows](actions)

<!-- ☝️ If necessary, update with a numbered list of your build instructions, including expected results / outputs with optional screenshots ☝️ -->

#### Manual Build
These instructions must be entered from the local directory checked out from source control.
1. Manually update `[INSERT YOUR PACKAGE NAME]/version.py` with the next release version, commit and push to the `main` branch:
``` 
git add [INSERT YOUR PACKAGE NAME]/version.py && git commit -m "Issue #<issue_number>: Updated version for release." && git push
```
2. Tag using the Git command line: 
``` 
git tag -a -m "Issue #<issue_number>: Release version <version>" <version>
```
**Note:** The `<version>` must match that in the `[INSERT YOUR PACKAGE NAME]/version.py` file.
3. Package the product:
- Package an `sdist` and a `tarball`: (traditional)
``` 
git checkout [INSERT YOUR PACKAGE NAME]/version.py && python3 -m build --wheel
```
- ... or package an `sdist` and a `zip` ...
``` 
python3 -m build --wheel && python3 setup.py sdist --format=zip
```
4. Publish product to PyPi for public distribution by using [Twine](https://twine.readthedocs.io/en/latest/):
``` 
twine check dist/* && twine upload --verbose
```
... or as a ZIP ...
``` 
twine check dist/* && twine upload --verbose dist/*.whl dist/*.zip
```

<!-- ☝️ If necessary, update with a numbered list of your build instructions, including expected results / outputs with optional screenshots ☝️ -->

### Test Instructions (if applicable)
1. [INSERT STEP-BY-STEP TEST INSTRUCTIONS HERE, WITH OPTIONAL SCREENSHOTS]

<!-- ☝️ Replace with a numbered list of your test instructions, including expected results / outputs with optional screenshots ☝️ -->

#### Local Build Testing
These instructions must be entered from the local directory checked out from source control.
A simplified build and release workflow is available for testing locally. Publishing directly to PyPi is not recommended as PyPi permits one upload per release version.  

1. Clean application:
``` 
rm -r build dist __pycache__ *.egg* .egg* ; git checkout [INSERT YOUR PACKAGE NAME]/version.py ; pip3 uninstall [INSERT YOUR PACKAGE NAME] -y
```
2. Build and install release locally:
``` 
python3 -m build --wheel && python3 setup.py sdist --format=zip
pip3 install [INSERT YOUR PACKAGE NAME] --no-index --find-links file://${PWD}/dist/
```  
... alternately, install an editable build using [Pip tooling](https://pypi.org/project/pip/) ...
``` 
pip install -e
```
3. [Testing publication to Test PyPi](https://packaging.python.org/en/latest/guides/using-testpypi/)  
Twine will prompt for your Test PyPi username and password.
```
twine check dist/*
twine upload --repository testpypi --verbose dist/*
```
<!-- ☝️ If necessary, update with numbered list of your test instructions, including expected results / outputs with optional screenshots ☝️ -->

## Changelog

See our [CHANGELOG.md](CHANGELOG.md) for a history of our changes.

See our [releases page]([INSERT LINK TO YOUR RELEASES PAGE]) for our key versioned releases.

<!-- ☝️ Replace with links to your changelog and releases page ☝️ -->

## Frequently Asked Questions (FAQ)

[INSERT LINK TO FAQ PAGE OR PROVIDE FAQ INLINE HERE]
<!-- example link to FAQ PAGE>
Questions about our project? Please see our: [FAQ]([INSERT LINK TO FAQ / DISCUSSION BOARD])
-->

<!-- example FAQ inline format>
1. Question 1
   - Answer to question 1
2. Question 2
   - Answer to question 2
-->

<!-- example FAQ inline with no questions yet>
No questions yet. Propose a question to be added here by reaching out to our contributors! See support section below.
-->

<!-- ☝️ Replace with a list of frequently asked questions from your project, or post a link to your FAQ on a discussion board ☝️ -->

## Contributing

Interested in contributing to our project? Please see our: [CONTRIBUTING.md](CONTRIBUTING.md)

<!-- example inline contributing guide>
1. Create an GitHub issue ticket describing what changes you need (e.g. issue-1)
2. [Fork](INSERT LINK TO YOUR REPO FORK PAGE HERE, e.g. https://github.com/my_org/my_repo/fork) this repo
3. Make your modifications in your own fork
4. Make a pull-request in this repo with the code in your fork and tag the repo owner / largest contributor as a reviewer

**Working on your first pull request?** See guide: [How to Contribute to an Open Source Project on GitHub](https://kcd.im/pull-request)
-->

[INSERT LINK TO YOUR CODE_OF_CONDUCT.md OR SHARE TEXT HERE]
<!-- example link to CODE_OF_CONDUCT.md>
For guidance on how to interact with our team, please see our code of conduct located at: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
-->

<!-- ☝️ Replace with a text describing how people may contribute to your project, or link to your contribution guide directly ☝️ -->

## License

See our: [LICENSE](LICENSE)
<!-- ☝️ Replace with the text of your copyright and license, or directly link to your license file ☝️ -->

## Support

[INSERT CONTACT INFORMATION OR PROFILE LINKS TO MAINTAINERS AMONG COMMITTER LIST]

<!-- example list of contacts>
Key points of contact are: [@github-user-1](link to github profile) [@github-user-2](link to github profile)
-->

<!-- ☝️ Replace with the key individuals who should be contacted for questions ☝️ -->

