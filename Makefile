test:
	@pytest -v

lint:
	@flakehell lint

black:
	@black workspace/ tests/

cov:
	@pytest --cov