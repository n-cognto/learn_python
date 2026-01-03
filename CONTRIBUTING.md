# Contributing to Learn Python

Thank you for your interest in contributing to this Python learning repository! 🎉

## 🌟 How You Can Contribute

We welcome contributions in many forms:

1. **Bug Fixes** - Fix typos, errors, or broken code examples
2. **New Content** - Add new lessons, examples, or exercises
3. **Projects** - Create new practical projects
4. **Tests** - Add or improve test coverage
5. **Documentation** - Improve explanations and documentation
6. **Translations** - Translate content to other languages

---

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/learn_python.git
cd learn_python
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks (optional but recommended)
pip install pre-commit
pre-commit install
```

### 3. Create a Branch

```bash
# Create a new branch for your contribution
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

---

## 📝 Contribution Guidelines

### Code Style

We follow PEP 8 and use automated tools to maintain code quality:

```bash
# Format code with Black
black .

# Check linting with flake8
flake8 .

# Sort imports with isort
isort .

# Type check with mypy
mypy Roadmap_learning/
```

**Key Style Points:**
- Use 4 spaces for indentation
- Maximum line length: 88 characters (Black default)
- Use type hints for function signatures
- Write docstrings for all functions and classes
- Follow Google or NumPy docstring style

### Example Function with Proper Style

```python
"""Module docstring explaining the purpose."""

from typing import List, Optional


def calculate_average(numbers: List[float]) -> Optional[float]:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers: List of numbers to average

    Returns:
        Average value, or None if list is empty

    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
```

### Testing

All new code should include tests:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov

# Run specific test file
pytest tests/test_day_15.py
```

**Test Guidelines:**
- Write tests for all new functions
- Aim for >80% code coverage
- Use descriptive test names
- Include edge cases and error conditions
- Use fixtures for common test data

### Documentation

- Update README.md if adding new features
- Add docstrings to all functions and classes
- Include examples in docstrings
- Update PROGRESS.md if adding new lessons

---

## 🎯 Types of Contributions

### Adding a New Day Lesson

1. Create file: `Roadmap_learning/day_XX.py`
2. Follow existing format:
   - Module docstring
   - Clear section headers
   - Code examples with comments
   - Practice exercises
3. Add corresponding test file: `tests/test_day_XX.py`
4. Update README.md with new day entry

### Adding a New Project

1. Create directory: `projects/XX_project_name/`
2. Include:
   - `README.md` - Project description and learning objectives
   - `main.py` - Main application code
   - `test_*.py` - Test files
   - `requirements.txt` - Project-specific dependencies (if any)
3. Update main README.md with project link

### Adding Advanced Topics

1. Create file: `advanced/XX_topic_name.py`
2. Include:
   - Comprehensive examples
   - Real-world use cases
   - Best practices
   - Common pitfalls
3. Add tests if applicable

### Improving Tests

1. Identify areas with low coverage
2. Write comprehensive tests
3. Include edge cases
4. Add integration tests where appropriate

---

## 🔍 Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines (run Black, flake8, isort)
- [ ] All tests pass (`pytest`)
- [ ] New code has tests
- [ ] Documentation is updated
- [ ] Commit messages are clear and descriptive

### Commit Message Format

Use clear, descriptive commit messages:

```
feat: Add async/await patterns lesson
fix: Correct typo in day_15.py
docs: Update README with new projects
test: Add tests for calculator app
refactor: Improve error handling in todo app
```

Prefixes:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Adding or updating tests
- `refactor:` - Code refactoring
- `style:` - Code style changes
- `chore:` - Maintenance tasks

### Submitting Pull Request

1. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Go to GitHub and create a Pull Request

3. Fill out the PR template:
   - **Title:** Clear, concise description
   - **Description:** What changes you made and why
   - **Related Issues:** Link any related issues
   - **Testing:** How you tested the changes

4. Wait for review and address feedback

---

## 🐛 Reporting Issues

### Bug Reports

When reporting bugs, include:

1. **Description:** Clear description of the bug
2. **Steps to Reproduce:** Detailed steps to reproduce
3. **Expected Behavior:** What should happen
4. **Actual Behavior:** What actually happens
5. **Environment:** Python version, OS, etc.
6. **Code Sample:** Minimal code to reproduce (if applicable)

### Feature Requests

When requesting features, include:

1. **Description:** Clear description of the feature
2. **Use Case:** Why this feature would be useful
3. **Examples:** Examples of how it would work
4. **Alternatives:** Alternative solutions you've considered

---

## 💡 Best Practices

### For Beginners

- Start with small contributions (typo fixes, documentation)
- Ask questions if you're unsure
- Read existing code to understand patterns
- Don't be afraid to make mistakes - we all learn!

### For Experienced Contributors

- Help review other PRs
- Mentor new contributors
- Suggest improvements to project structure
- Share your expertise in advanced topics

---

## 📚 Resources

- [PEP 8 Style Guide](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [pytest Documentation](https://docs.pytest.org/)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)

---

## 🤝 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors.

### Expected Behavior

- Be respectful and considerate
- Welcome newcomers and help them learn
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information
- Other unprofessional conduct

---

## 🎉 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Thanked in the community

---

## 📞 Questions?

If you have questions:
- Open an issue with the `question` label
- Join our community discussions
- Reach out to maintainers

---

**Thank you for contributing to making Python learning better for everyone! 🚀**

*Last updated: January 2026*
