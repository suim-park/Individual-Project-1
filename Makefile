install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py
	juypter -m pytest -vv --con=mian test_*.ipynb

format:	
	black *.py 

lint:
	ruff --disable=R,C --ignore-patterns=test_.*?py *.py

deploy:
	# deploy goes here
		
all: install lint test format deploy