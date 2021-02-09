install: |
	pip install -r test_requirements.txt

test: |
	pytest tests/

coverage: |
	pytest --cov=validator tests/

report: |
	pytest --cov=validator --cov-report=html tests/

clean: |
	rm -rf .coverage htmlcov
	rm -rf .pytest_cache
