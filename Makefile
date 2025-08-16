.PHONY: setup \
		run \
		lint \
		mypy \

		test \
		coverage \

		help

venv/bin/activate: ## Alias for virtual environment
	python -m venv venv
	export POETRY_VIRTUALENVS_PATH=./venv

setup: venv/bin/activate ## Project setup
	. venv/bin/activate; pip install --upgrade pip
	. venv/bin/activate; pip install poetry
	. venv/bin/activate; poetry install


run: ## Run project
	. venv/bin/activate; python entry.py


lint: ## Run linter
	. venv/bin/activate; ruff format --config ./pyproject.toml . && ruff check --fix --config ./pyproject.toml .

mypy: ## Run mypy
	. venv/bin/activate; mypy ./

test: ## Run tests check
	poetry run pytest $(filter-out $@,$(MAKECMDGOALS)) -s

coverage: ## Run tests coverage
	. venv/bin/activate; pytest --cov=app tests/ --cov-report=xml --cov-report=term

# Just help
help: ## Display help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
