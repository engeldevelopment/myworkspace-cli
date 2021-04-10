test: lint
	@pytest -v

lint:
	@flakehell lint

black:
	@black myworkspace/ tests/

cov: lint
	@pytest --cov