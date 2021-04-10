test: lint
	@pytest -v

lint:
	@flakehell lint

black:
	@black workspace/ tests/

cov: lint
	@pytest --cov