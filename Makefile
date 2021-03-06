install:
	pip install -U pip
	pip install -r requirements.txt

run-dev:
	cd web/app; python manage.py runserver

makemigrations:
	cd web/app; python manage.py makemigrations

migrate:
	cd web/app; python manage.py migrate

createsuperuser:
	cd web/app; python manage.py createsuperuser

collectstatic:
	cd web/app; python manage.py collectstatic --noinput

run-prod:
	cd web/app; gunicorn app.wsgi