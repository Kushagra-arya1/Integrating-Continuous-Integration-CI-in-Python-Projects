#!/usr/bin/env bash
# =====================================================================
# Local CI Pipeline Runner for Unix/Linux/macOS
# Simulates the GitHub Actions CI pipeline on a developer's local machine.
# =====================================================================
set -e

echo "[CI LOCAL] Starting Local Continuous Integration Pipeline Simulation..."
echo "---------------------------------------------------------------------"

# Step 1: Checking Python
echo "[CI STEP 1/3] Checking Python environment..."
python3 --version

# Step 2: Code Linting
echo "[CI STEP 2/3] Running Code Linting with Flake8..."
flake8 src tests
echo "[CI SUCCESS] Flake8 linting passed with 0 errors!"

# Step 3: Run Automated Test Suite & Generate Reports
echo "[CI STEP 3/3] Running Pytest Suite with Coverage and Report Generation..."
mkdir -p reports
pytest \
  --cov=mini_calc \
  --cov-report=term-missing \
  --cov-report=xml:reports/coverage.xml \
  --cov-report=html:reports/htmlcov \
  --cov-fail-under=90 \
  --junitxml=reports/test-results.xml \
  tests/

echo "---------------------------------------------------------------------"
echo "[CI SUCCESS] All pipeline stages passed successfully!"
echo "[CI ARTIFACTS] Reports generated in ./reports/"
echo "- JUnit XML: ./reports/test-results.xml"
echo "- Cobertura XML: ./reports/coverage.xml"
echo "- HTML Coverage: ./reports/htmlcov/index.html"
echo "====================================================================="
