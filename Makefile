.DEFAULT_GOAL := install

PYTHON = python3
VENV = venv
REQ = requirements.txt

# Create virtual environment
$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)

# Install dependencies
install: $(VENV)/bin/activate
	$(VENV)/bin/pip install -r $(REQ)

# Run notebook
run:
	$(VENV)/bin/jupyter nbconvert --to notebook --execute notebooks/01_data_cleaning.ipynb --output notebooks/01_data_cleaning_output.ipynb

# Run tests
test:
	$(VENV)/bin/pytest tests/

# Clean outputs
clean:
	rm -f notebooks/*_output.ipynb
	find . -name "__pycache__" -type d -exec rm -r {} +

.PHONY: install run test clean