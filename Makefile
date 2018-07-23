venv:
	virtualenv -p python3.6 venv

req:
	pip install -r requirements.txt

db:
	docker-compose up -d

mig:
	python manage.py migrate
	
server:
	python manage.py runserver 0.0.0.0:7777
