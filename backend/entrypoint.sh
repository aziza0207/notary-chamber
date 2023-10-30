#!/bin/sh

sleep 4

python manage.py migrate
# python manage.py create_default_admin
python manage.py loaddata notary/fixtures/notaries.json
python manage.py loaddata content/fixtures/categories.json
python manage.py loaddata content/fixtures/documents.json

exec "$@"
