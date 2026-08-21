.PHONY: clean lint test test-dx test-cov test-html help

# Default argument when none are provided
.DEFAULT_GOAL := help

# To inform the user of the available commands.
help:
	@echo "Available commands:"
	@echo "  make clean      - Remove build, cache, test, and python artifacts"
	@echo "  make run      - Runs the main project"
	@echo "  make lint       - Run static code analysis using pylint"
	@echo "  make test       - Run the pytest test suite"
	@echo "  make test-dx      - Runs the pytest test suit and view any outputs"
	@echo "  make test-cov   - Run tests and display terminal coverage report"
	@echo "  make test-html  - Run tests, generate HTML report, and serve locally"


# To properly clean up the files that might get in the way of the user or other commands.
clean:
	@echo "Cleaning up unwanted files and test artifacts..."
	@rm -rf .pytest_cache/
	@rm -rf .coverage *.coverage
	@rm -rf htmlcov/
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "Clean complete."

run:
	@echo "Running Code"
	@echo python -m src.project.server 
	@python -m src.project.server || true
	@echo "Done"

# To statically analyze the code.
lint:
	@echo "Running static analysis..."
	@chmod +x run_pylint.sh
	@echo ./run_pylint.sh
	@./run_pylint.sh || true
	@echo "Static Analysis Complete."

# To run the provided tests classes.
test: clean
	@echo "Running test suite..."
	@chmod +x run_pytest.sh
	@echo ./run_pytest.sh
	@./run_pytest.sh || true
	@echo "Test Suite Complete"

# To run the provided tests classes and view any outputs.
test-dx: clean
	python -m pytest -rP

# To run the provided tests classes and view the code coverage.
test-cov: clean
	@echo "Running tests with terminal coverage reporting..."
	@echo python -m pytest --cov=src --cov-report=term-missing --cov-branch
	@python -m pytest --cov=src --cov-report=term-missing --cov-branch || true
	@echo "Test Coverage Complete"

# To run the provided tests classes and view the code coverage in a html format.
test-html: clean
	@echo "Generating HTML coverage report..."
	@echo python -m pytest --cov=src --cov-report=html --cov-branch
	@python -m pytest --cov=src --cov-report=html --cov-branch || true
	@echo "Starting local coverage server at http://localhost:8080/ (Press Ctrl+C to stop)..."
	python -m http.server 8080 --directory htmlcov
