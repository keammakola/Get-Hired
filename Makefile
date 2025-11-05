setup:
	python3 -m venv venv
	pip install -r requirements.txt
	pre-commit install

pre-commit:
	pre-commit run --all-files
run:
	clear
	./venv/bin/python src/main.py

api:
	./venv/bin/pip install -q -U google-genai
