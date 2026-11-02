@echo off
REM =====================================================================
REM Local CI Pipeline Runner for Windows
REM Simulates the GitHub Actions CI pipeline on a developer's local machine.
REM =====================================================================

echo [CI LOCAL] Starting Local Continuous Integration Pipeline Simulation...
echo ---------------------------------------------------------------------

REM Step 1: Check Python availability
echo [CI STEP 1/3] Checking Python environment...
python --version
if errorlevel 1 (
    echo [CI ERROR] Python is not installed or not in PATH!
    exit /b 1
)

REM Step 2: Code Linting
echo [CI STEP 2/3] Running Code Linting with Flake8...
python -m flake8 src tests
if errorlevel 1 (
    echo [CI FAILURE] Flake8 linting check failed! Please fix code style issues before pushing.
    exit /b 1
)
echo [CI SUCCESS] Flake8 linting passed with 0 errors!

REM Step 3: Run Automated Test Suite & Generate Reports
echo [CI STEP 3/3] Running Pytest Suite with Coverage and Report Generation...
if not exist reports mkdir reports

python -m pytest ^
  --cov=mini_calc ^
  --cov-report=term-missing ^
  --cov-report=xml:reports/coverage.xml ^
  --cov-report=html:reports/htmlcov ^
  --cov-fail-under=90 ^
  --junitxml=reports/test-results.xml ^
  tests/

if errorlevel 1 (
    echo [CI FAILURE] Pytest suite failed! One or more tests failed or coverage is under threshold.
    exit /b 1
)

echo ---------------------------------------------------------------------
echo [CI SUCCESS] All pipeline stages passed successfully!
echo [CI ARTIFACTS] Reports generated in .\reports\
echo - JUnit XML: .\reports\test-results.xml
echo - Cobertura XML: .\reports\coverage.xml
echo - HTML Coverage: .\reports\htmlcov\index.html
echo =====================================================================
exit /b 0
