# run python preprocess
activate:
	source .venv/bin/activate
dependency: activate
	pip install -r requirements.txt
pre:
	python preprocess.py