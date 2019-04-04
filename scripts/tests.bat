docker-compose -f dev.yml run django python manage.py test --exclude-tag=SLOW --exclude-tag=TO-FIX
