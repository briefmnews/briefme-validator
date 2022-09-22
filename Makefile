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

release:
	git tag -a $(shell python -c "from validator import __version__; print(__version__)") -m "$(m)"
	git push origin --tags
