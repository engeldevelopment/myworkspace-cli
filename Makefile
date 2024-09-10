test:
	@pytest -v

black:
	@black myworkspace/ tests/

cov: 
	@pytest --cov