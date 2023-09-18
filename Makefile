install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py
	py.test --nbval *.ipynb

format:	
	black *.py 

lint:
	ruff lint test_.*?py *.py

deploy:
	# deploy goes here
		
all: install lint test format deploy