setup:
	sudo apt install python3.13-venv
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	pre-commit install

pre-commit:
	pre-commit run --all-files

run:
	python3 src/main.py
