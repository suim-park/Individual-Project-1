install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py *.py
	py.test --nbval *.ipynb

format:
	black *.ipynb &&\
		black *.py &&\
			black test_*.py

lint:
	ruff check test_.*py &&\
		ruff check *.py
			ruff check *.ipynb
	ruff lint --fix

deploy:
	# deploy goes here
		
all: install lint test format