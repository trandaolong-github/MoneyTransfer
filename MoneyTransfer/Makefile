SHELL=/usr/bin/env bash

env:
	virtualenv -p python3 env
	./env/bin/python -m pip install -r requirements.txt
	./env/bin/activate
	python manage.py runserver

clean:
	rm -rf env