# Contributing to NextGigAI

First off, thank you for considering contributing to NextGigAI! It's people like you that make NextGigAI such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* Use a clear and descriptive title
* Describe the exact steps which reproduce the problem
* Provide specific examples to demonstrate the steps
* Describe the behavior you observed after following the steps
* Explain which behavior you expected to see instead and why
* Include screenshots if possible

### Suggesting Enhancements

If you have a suggestion for a new feature or enhancement:

* Use a clear and descriptive title
* Provide a step-by-step description of the suggested enhancement
* Provide specific examples to demonstrate the steps
* Describe the current behavior and explain which behavior you expected to see instead

### Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Include screenshots and animated GIFs in your pull request whenever possible
* Follow the Python style guide
* Include thoughtfully-worded, well-structured tests
* Document new code
* End all files with a newline

## Development Process

1. Fork the repo
2. Create a new branch from `main`
3. Make your changes
4. Run the tests
5. Push to your fork and submit a pull request

### Template Development Guidelines

When creating or modifying resume templates:

1. **Professional Design**
   - Use clean, readable fonts
   - Maintain consistent spacing
   - Ensure proper hierarchy

2. **Template Structure**
   - Follow the YAML schema
   - Include all required fields
   - Document style choices

3. **Testing**
   - Test with various content lengths
   - Verify PDF/DOCX output
   - Check different section types

## Setting Up Your Development Environment

1. Clone your fork:
```bash
git clone https://github.com/your-username/NextGigAI.git
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
uvicorn resume-web:app --reload
```

## Style Guide

* Follow PEP 8
* Use meaningful variable names
* Add docstrings to all functions
* Comment complex logic
* Keep functions focused and small

## Questions?

Feel free to open an issue with your question or reach out to the maintainers directly.

Thank you for contributing! 🚀
