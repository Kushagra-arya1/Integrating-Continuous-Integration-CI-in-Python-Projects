# MiniCalc - Python Continuous Integration (CI) Project

[![Python CI Pipeline](https://github.com/example-user/mini-calc/actions/workflows/ci.yml/badge.svg)](https://github.com/example-user/mini-calc/actions)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![Code Style: Flake8](https://img.shields.io/badge/code%20style-flake8-green.svg)](https://flake8.pycqa.org/)
[![Coverage: 100%](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](./reports/htmlcov/index.html)
[![License: MIT](https://img.shields.io/badge/license-MIT-informational.svg)](LICENSE)

A clean, modular Python project demonstrating a professional **Continuous Integration (CI) Pipeline** using **GitHub Actions**, **Flake8**, **Pytest**, and **Coverage**. Designed with minimal lines of code while ensuring 100% test coverage, strict linting gates, and automated test reporting.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Repository Structure](#-repository-structure)
- [Continuous Integration (CI) Pipeline](#-continuous-integration-ci-pipeline)
- [Local Setup & Replication Guide](#-local-setup--replication-guide)
- [Running Local CI in One Click](#-running-local-ci-in-one-click)
- [Testing & Quality Assurance](#-testing--quality-assurance)
- [Viewing Reports & Artifacts](#-viewing-reports--artifacts)
- [Simulating & Verifying CI Failure](#-simulating--verifying-ci-failure)
- [Documentation & Detailed Report](#-documentation--detailed-report)

---

## 🎯 Project Overview

This project satisfies the **Week 6 Continuous Integration (CI) in Python Projects** task. It simulates an enterprise development workflow with:
- **Clean Architecture & Minimal Code**: Only ~38 core statements across `mini_calc` with strict type annotations and error guards.
- **Automated Linting Gate**: Enforces PEP 8 standards and catches syntax bugs using `flake8`.
- **Automated Testing Suite**: 16 unit and parameterized tests using `pytest` covering normal, boundary, and error cases.
- **100% Code Coverage**: Generates JUnit XML, Cobertura XML, and HTML visual reports.
- **Multi-Version CI Matrix**: Automated GitHub Actions testing across Python 3.10, 3.11, 3.12, and 3.13.
- **Quality Gates**: Workflow automatically fails if any test fails or code coverage drops below 90%.

---

## 📂 Repository Structure

```text
week6/
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI pipeline configuration
├── src/
│   └── mini_calc/
│       ├── __init__.py          # Package initialization & exports
│       └── calculator.py        # Concise core math & utility functions (~38 lines)
├── tests/
│   ├── __init__.py              # Test suite initialization
│   └── test_calculator.py       # Comprehensive pytest suite (16 tests, 100% coverage)
├── reports/                     # Generated test & coverage artifacts (local/CI)
│   ├── coverage.xml             # Cobertura XML coverage report
│   ├── test-results.xml         # JUnit XML test execution report
│   └── htmlcov/                 # Interactive visual HTML coverage report
├── .flake8                      # Flake8 linter configuration
├── .gitignore                   # Standard Python gitignore
├── pyproject.toml               # Python packaging & pytest auto-discovery configuration
├── requirements.txt             # Production dependencies
├── requirements-dev.txt         # Testing, linting, and CI dependencies
├── run_ci_local.bat             # 1-Click local CI runner for Windows
├── run_ci_local.sh              # 1-Click local CI runner for Linux/macOS
├── README.md                    # Project overview and quickstart guide
└── CI_DOCUMENTATION.md          # Comprehensive CI architecture and challenge report
```

---

## ⚙️ Continuous Integration (CI) Pipeline

The CI pipeline is automated via `.github/workflows/ci.yml`.

### Pipeline Triggers
- **Push**: Triggers on any commit pushed to `main` or `master`.
- **Pull Request**: Triggers on PR creation or updates targeting `main` or `master`.
- **Manual Trigger**: Allows manual workflow triggering via `workflow_dispatch`.

### Automated Pipeline Steps
1. **Checkout Code**: Retrieves the repository at the trigger commit (`actions/checkout@v4`).
2. **Setup Python Matrix**: Configures isolated environments for Python 3.10, 3.11, 3.12, and 3.13 (`actions/setup-python@v5`) with dependency caching.
3. **Install Dependencies**: Upgrades `pip` and installs dependencies from `requirements.txt` and `requirements-dev.txt`.
4. **Code Linting (`flake8`)**: 
   - Checks for syntax errors (`E9,F63,F7,F82`).
   - Checks code style, line length, and cyclomatic complexity (max complexity 10).
5. **Run Automated Tests & Coverage (`pytest`)**:
   - Executes all 16 unit tests.
   - Generates JUnit XML test report (`reports/test-results-<pyver>.xml`).
   - Generates Cobertura XML (`reports/coverage-<pyver>.xml`) and HTML reports (`reports/htmlcov-<pyver>/`).
   - Enforces coverage gate (`--cov-fail-under=90`). Fails build if coverage is insufficient.
6. **Publish Job Summary**: Posts status directly to the GitHub Actions Job Summary UI.
7. **Upload Artifacts**: Uploads reports as workflow artifacts with a 14-day retention period.

---

## 💻 Local Setup & Replication Guide

To replicate and run this project in your local development environment:

### 1. Clone or Extract the Project
```bash
git clone <repository-url>
cd week6
```

### 2. Create and Activate a Virtual Environment
- **Windows (Command Prompt / PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## ⚡ Running Local CI in One Click

We provide automated scripts to simulate the entire CI pipeline locally prior to committing:

- **Windows**:
  ```cmd
  run_ci_local.bat
  ```
- **macOS / Linux**:
  ```bash
  chmod +x run_ci_local.sh
  ./run_ci_local.sh
  ```

### Manual Commands
You can also run individual CI steps manually:

1. **Linting Check**:
   ```bash
   flake8 src tests
   ```

2. **Run Tests with Coverage**:
   ```bash
   pytest --cov=mini_calc --cov-report=term-missing tests/
   ```

3. **Generate Full Reports (XML & HTML)**:
   ```bash
   pytest --cov=mini_calc --cov-report=term-missing --cov-report=xml:reports/coverage.xml --cov-report=html:reports/htmlcov --junitxml=reports/test-results.xml tests/
   ```

---

## 📊 Testing & Quality Assurance

### Test Suite Summary
| Test Case | Target Function | Test Type | Description |
| :--- | :--- | :--- | :--- |
| `test_add` | `add(a, b)` | Parameterized | Tests positive, negative, zero, and float addition |
| `test_subtract` | `subtract(a, b)` | Parameterized | Tests subtraction yielding positive, negative, and zero |
| `test_multiply` | `multiply(a, b)` | Parameterized | Tests multiplication with positives, negatives, and zero |
| `test_divide` | `divide(a, b)` | Unit + Exception | Tests exact float division and `ZeroDivisionError` guard |
| `test_power` | `power(base, exp)` | Unit | Tests standard powers, exponent 0, and negative powers |
| `test_is_even` | `is_even(n)` | Unit + Exception | Tests even/odd detection and `TypeError` for floats/booleans |
| `test_factorial` | `factorial(n)` | Unit + Exception | Tests factorials of 0, 1, 5, `ValueError` for negatives, and `TypeError` |
| `test_average` | `average(seq)` | Unit + Exception | Tests mean calculation and `ValueError` guard on empty sequence |
| `test_percentage` | `percentage(p, t)` | Unit + Exception | Tests percentage computation and `ZeroDivisionError` guard |

### Local Test Execution Output
```text
============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.7.0
rootdir: C:\Users\Kushagra Arya\OneDrive\Desktop\week6
plugins: anyio-4.14.2, cov-7.1.0
collected 16 items

tests\test_calculator.py ................                                [100%]

=============================== tests coverage ================================
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
src\mini_calc\__init__.py         3      0   100%
src\mini_calc\calculator.py      35      0   100%
-----------------------------------------------------------
TOTAL                            38      0   100%
============================= 16 passed in 1.06s ==============================
```

---

## 📈 Viewing Reports & Artifacts

After running tests or downloading CI workflow artifacts:
- **Interactive HTML Coverage**: Open `reports/htmlcov/index.html` in any web browser to view line-by-line coverage analysis.
- **JUnit XML Report**: Located at `reports/test-results.xml`, compatible with CI dashboards, test result visualizers, and IDEs.
- **Cobertura XML Report**: Located at `reports/coverage.xml`, compatible with Codecov and SonarQube.

---

## 🛑 Simulating & Verifying CI Failure

A robust CI pipeline **must fail immediately** if code quality regressions or broken tests are introduced.

### Test Failure Simulation
If a developer alters `add(a, b)` to return `a + b + 1`:
```bash
pytest tests/
```
Output:
```text
FAILED tests/test_calculator.py::test_add[2-3-5] - assert 6 == 5
========================= 1 failed, 15 passed in 0.18s =========================
```
- **Exit Code**: `1` (Non-zero).
- **CI Outcome**: The CI pipeline immediately halts at Step 5. No deployment or build artifact is approved.

### Linting Failure Simulation
If a file contains an unformatted line exceeding the configured character limit or an unused import:
```bash
flake8 src tests
```
Output:
```text
src\mini_calc\calculator.py:1:80: E501 line too long (83 > 79 characters)
```
- **Exit Code**: `1`.
- **CI Outcome**: The CI pipeline fails at Step 4 (Linting), preventing poorly formatted code from merging.

---

## 📖 Documentation & Detailed Report
For the complete technical breakdown including CI tool comparison, challenge documentation, and setup logs, refer to:
👉 **[CI_DOCUMENTATION.md](file:///c:/Users/Kushagra%20Arya/OneDrive/Desktop/week6/CI_DOCUMENTATION.md)**
