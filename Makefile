setup:
	pip install -r requirements.txt
	pre-commit install

pre-commit:
	pre-commit run --all-files
run:
	clear
	python3 src/main.py

api:
	pip install -q -U google-genai
