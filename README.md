# Playwright-based tests for product_crm

# Requirements
# 1) python -m pip install -r requirements.txt
# 2) python -m playwright install --with-deps

# Environment variables (or .env):
# TEST_USER, TEST_PASSWORD - credentials for tests (required)
# BASE_URL - base URL for the application (optional; default points to crmpharma-dev)
# HEADLESS - true/false (optional; default true)

# Run tests:
# pytest -q

# CI notes: the included workflow installs browsers and runs pytest. Set TEST_USER/TEST_PASSWORD/BASE_URL as repository secrets.