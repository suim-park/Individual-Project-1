install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py *.py
	py.test --nbval *.ipynb

format:	
	black *.py 

lint:
	ruff check test_.*py *.py
	ruff lint --fix

deploy:
	# deploy goes here
		
all: install lint test format