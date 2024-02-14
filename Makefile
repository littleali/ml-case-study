# run python preprocess
create_venv_if_not_exists:
	if [ ! -d .venv ]; then python3 -m venv .venv; fi
activate: create_venv_if_not_exists
	source .venv/bin/activate
dependency: activate
	pip install -r requirements.txt