# Forma Developer Guide

## Overview

This guide provides technical details for developers who wish to contribute to or extend Forma.

## Project Structure

[Detailed explanation of the file tree and modules.]

## Exception Handling

All modules implement exception handling to ensure robust performance. Key practices include:

- Use of `try-except` blocks around critical operations.
- Logging of errors with informative messages.
- Graceful degradation when possible, allowing the application to continue running.

## Logging

Forma uses the built-in `logging` module. Log levels can be adjusted through `config.yaml`.

- **INFO:** General information about the application flow.
- **WARNING:** Non-critical issues that may require attention.
- **ERROR:** Critical issues that prevent a module from functioning.

## Adding New Modules

[Guidelines on extending the application.]

## Testing

[Information on running unit tests and writing new tests.]

