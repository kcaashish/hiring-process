web: gunicorn hiring_process.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py collecstatic --noinput
release: python manage.py migrate --noinput
