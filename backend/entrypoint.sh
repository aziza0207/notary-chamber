#!/bin/sh

sleep 4

python manage.py migrate
python manage.py create_default_admin

python manage.py loaddata notary/fixtures/notaries.json # temporary fixture while notary model not updated
python manage.py loaddata notary/fixtures/assistants.json

python manage.py loaddata content/fixtures/aphorisms.json
python manage.py loaddata content/fixtures/faq.json
python manage.py loaddata notary/fixtures/recipients.json
python manage.py loaddata content/fixtures/news.json
python manage.py loaddata content/fixtures/image.json
python manage.py loaddata content/fixtures/links.json
python manage.py loaddata content/fixtures/gallery_photo.json
python manage.py loaddata content/fixtures/detail_photos.json
python manage.py loaddata content/fixtures/gallery_video.json
python manage.py loaddata content/fixtures/contacts.json

python manage.py loaddata structure/fixtures/about_departments.json
python manage.py loaddata structure/fixtures/about_workers.json


# "big" fixtures

# python manage.py loaddata notary/fixtures/notary_all.json

exec "$@"
