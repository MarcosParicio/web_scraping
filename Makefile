# Makefile

# Virtual environment name
VENV_NAME = holidays_env
PYTHON_VERSION = 3.8.12

# Set up the environment
setup: install_python create_venv install_dependencies

# Install Python 3.8.12 using pyenv
install_python:
	@echo "Installing Python $(PYTHON_VERSION)..."
	pyenv install -s $(PYTHON_VERSION)
	pyenv local $(PYTHON_VERSION)

# Create virtual environment using pyenv-virtualenv
create_venv:
	@if pyenv virtualenvs | grep -q "$(VENV_NAME)"; then \
		echo "The virtual environment $(VENV_NAME) already exists."; \
	else \
		echo "Creating the virtual environment $(VENV_NAME)..."; \
		pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME); \
	fi

# Install dependencies from requirements.txt
install_dependencies:
	@echo "Installing dependencies..."
	pyenv exec pip install --upgrade pip
	pyenv exec pip install -r requirements.txt

# Run the main.py script located in the src directory
run:
	@echo "Running main.py..."
	pyenv exec python src/main.py

# Run the identify_correct_table.py script located in the src directory
html_tables:
	@echo "Running identify_correct_table.py..."
	pyenv exec python src/identify_correct_table.py

# Run tests
test:
	@echo "Running tests..."
	pyenv exec pytest tests/

# Clean virtual environment (optional)
clean:
	@echo "Removing virtual environment..."
	pyenv uninstall -f $(VENV_NAME)
