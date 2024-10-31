# Changelog

All notable changes to this project will be documented in this file. 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2023-01-31
### Templatized Python Starter Kit
- Support of [SLIM project](https://nasa-ammos.github.io/slim/) instructional writeups  
- Templatized implementation of best practice documentation
- Automatic publishing to the [PyPi Python Package Index](https://pypi.org/)

## [1.0.1] - 2024-03-15
### Scanning operations
- GitHub Actions-based secrets detection
- GitHub Actions-based SCRUB (CodeQL) analysis
- GitHub Actions-based Pylint static code analysis
- Add updated SLIM Governance documentation

## [1.0.2] - 2024-10-31
### Trusted Publishing
- Updates to GitHub Actions Workflow file to support Trusted Publishing for PyPi as an OpenID Connect trusted identity provider
  - Separate Build and Release into separate segments to support independent management of publishing permissions and allow multiple publishing endpoints
  - Utilize `upload-artifact` action to store and retrieve packaged builds during the workflow process

