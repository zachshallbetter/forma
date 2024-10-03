# Forma Developer Guide

## Introduction

This guide provides comprehensive technical details for developers who wish to contribute to, extend, or maintain Forma. It covers essential aspects of the project's architecture, coding practices, and development workflow.

## Table of Contents

- [Project Structure](#project-structure)
- [Development Setup](#development-setup)
- [Coding Guidelines](#coding-guidelines)
- [Testing](#testing)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Deployment](#deployment)

## Project Structure

The Forma project is organized as follows:

```
forma/
├── README.md
├── LICENSE
├── setup.py
├── requirements.txt
├── .gitignore
├── docs/
│   ├── user_manual.md
│   ├── developer_guide.md
│   ├── api_reference.md
│   └── changelog.md
├── data/
│   ├── images/
│   ├── calibration/
│   └── outputs/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── utils/
│   ├── acquisition/
│   ├── preprocessing/
│   ├── feature_detection/
│   ├── matching/
│   ├── calibration/
│   ├── reconstruction/
│   ├── mesh_processing/
│   ├── scaling_measurement/
│   ├── export/
│   └── interface/
├── tests/
│   ├── __init__.py
│   ├── test_preprocessing.py
│   ├── ...
├── scripts/
│   ├── generate_calibration_pattern.py
│   └── group_images.py
└── assets/
    └── sample_image.jpg
```

## Development Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/forma.git
    cd forma
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install in Editable Mode**

    ```bash
    pip install -e .
    ```

## Coding Guidelines

- **Python Version:** Use Python 3.7 or higher.
- **Style Guide:** Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) coding standards.
- **Type Hinting:** Use type annotations where appropriate.
- **Logging:** Use the `logging` module for debug and error messages.
- **Exceptions:** Raise appropriate exceptions and handle them gracefully.

## Testing

- **Unit Tests:** Located in the `tests/` directory.
- **Running Tests:**

    ```bash
    python -m unittest discover tests
    ```

- **Test Workflow:**

    Included `tests/test_workflow.py` to test the entire pipeline.

## Documentation

- **User Manual:** Located in `docs/user_manual.md`.
- **Developer Guide:** Located in `docs/developer_guide.md`.
- **API Reference:** Generate using tools like Sphinx or Doxygen.

## Contributing

- **Branching:** Use feature branches (`feature/your-feature-name`).
- **Pull Requests:** Submit PRs to the `main` branch.
- **Code Reviews:** All code must be reviewed before merging.
- **Issue Tracking:** Use GitHub Issues for tracking bugs and feature requests.

## Deployment

- **Packaging:** Use `setup.py` for packaging.
- **Publishing to PyPI:** Coming soon.
- **Versioning:** Follow semantic versioning (MAJOR.MINOR.PATCH).

## Testing with Synthetic Calibration Images

To facilitate testing of the calibration module, synthetic images can be generated programmatically.

### Integration in Tests

In your test suites, you can generate synthetic calibration images as part of the `setUp` method:

```