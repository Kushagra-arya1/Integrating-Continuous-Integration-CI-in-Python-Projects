# Integrating Continuous Integration (CI) in Python Projects

[![CI Pipeline](https://github.com/Kushagra-arya1/Integrating-Continuous-Integration-CI-in-Python-Projects/actions/workflows/ci.yml/badge.svg)](https://github.com/Kushagra-arya1/Integrating-Continuous-Integration-CI-in-Python-Projects/actions)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://github.com/Kushagra-arya1/Integrating-Continuous-Integration-CI-in-Python-Projects)
[![Lint: Flake8](https://img.shields.io/badge/lint-flake8-green.svg)](https://flake8.pycqa.org/)
[![Coverage: 100%](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://github.com/Kushagra-arya1/Integrating-Continuous-Integration-CI-in-Python-Projects)

> **GitHub Repository**: [Kushagra-arya1/Integrating-Continuous-Integration-CI-in-Python-Projects](https://github.com/Kushagra-arya1/Integrating-Continuous-Integration-CI-in-Python-Projects)

A minimalist Python project demonstrating an automated **Continuous Integration (CI)** pipeline using **GitHub Actions**, **Flake8**, **Pytest**, and **Coverage**.

---

## 📁 Project Structure

```text
├── .github/workflows/ci.yml   # GitHub Actions CI pipeline configuration
├── src/mini_calc/             # Minimal Python library (~38 statements)
│   ├── __init__.py
│   └── calculator.py
├── tests/                     # Automated test suite (16 tests, 100% coverage)
│   ├── __init__.py
│   └── test_calculator.py
├── reports/                   # Test & coverage artifacts (JUnit XML, HTML)
├── run_ci_local.bat           # 1-Click local CI runner (Windows)
├── run_ci_local.sh            # 1-Click local CI runner (Linux/macOS)
├── pyproject.toml             # Packaging & pytest configuration
├── requirements.txt           # Production runtime dependencies
├── requirements-dev.txt       # Testing, linting, and CI dependencies
├── README.md                  # Minimal project overview
└── CI_DOCUMENTATION.md        # Comprehensive technical CI report
```

---

## 🚀 Quickstart

### 1. Setup Environment
```bash
git clone https://github.com/Kushagra-arya1/Integrating-Continuous-Integration-CI-in-Python-Projects.git
cd Integrating-Continuous-Integration-CI-in-Python-Projects

# Create & activate virtual environment
python -m venv venv
# Windows: .\venv\Scripts\activate | Linux/macOS: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt -r requirements-dev.txt
```

### 2. Run Local CI (1-Click)
- **Windows**: `.\run_ci_local.bat`
- **Linux / macOS**: `./run_ci_local.sh`

### 3. Run Manually
```bash
# Lint code
flake8 src tests

# Run 16 tests with 100% coverage & report generation
pytest --cov=mini_calc --cov-report=term-missing tests/
```

---

## ⚡ CI Pipeline Overview

- **Triggers**: Every `push` and `pull_request` to `main` / `master`.
- **Matrix**: Tests simultaneously across Python `3.10`, `3.11`, `3.12`, and `3.13`.
- **Linting**: Strict `flake8` syntax and PEP 8 style validation.
- **Testing**: `pytest` running 16 tests; fails build if any test fails or coverage < 90%.
- **Artifacts**: Generates JUnit XML, Cobertura XML, and HTML coverage reports.

For the in-depth technical documentation and challenge report, see **[CI_DOCUMENTATION.md](CI_DOCUMENTATION.md)**.
