setup:
	pip install -r requirements.txt
	pre-commit install

pre-commit:
	pre-commit run --all-files
run:
	python3 src/main.py
