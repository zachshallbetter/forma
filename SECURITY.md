# Security Policy

## Reporting a vulnerability

If you find a security issue in Forma, please report it privately rather than opening a
public issue. Use GitHub private vulnerability reporting:

<https://github.com/zachshallbetter/forma/security/advisories/new>

Include:

- a description of the issue and its impact,
- steps to reproduce (a minimal example is ideal),
- the affected component and version or commit.

This is a solo-maintained project. Handling is best-effort with no SLA: there is no
guaranteed response or fix time. Please give a reasonable window to ship a fix before any
public disclosure.

## Scope

Forma is a Python command-line tool that reads local image sets and configuration
(`config.yaml`, parsed with `yaml.safe_load`) and writes 3D models. It does not run a
server or handle authentication. The relevant surface is input handling: crafted image or
configuration files, path handling in `src/utils/file_io.py`, and the helper scripts under
`scripts/`. Reports about those are in scope.

Questions of reconstruction accuracy or fitness for a medical use are not security issues;
open a regular issue.

## Supported versions

Forma is at version 0.1.0 (git tag `v0.1.0`). Only the latest commit on `main` receives fixes.
