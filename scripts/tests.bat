docker-compose -f local.yml run django python manage.py test --exclude-tag=SLOW --exclude-tag=TO-FIX
