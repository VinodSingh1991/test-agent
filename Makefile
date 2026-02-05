.PHONY: install dev test format lint clean run

install:
	pip install -r requirements.txt

dev:
	pip install -r requirements.txt
	pip install -e ".[dev]"

test:
	pytest tests/ -v

format:
	black design_system_agent/

lint:
	flake8 design_system_agent/
	mypy design_system_agent/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ *.egg-info

run:
	uvicorn design_system_agent.api.main:app --reload --host 0.0.0.0 --port 8000
