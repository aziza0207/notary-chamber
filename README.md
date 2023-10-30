About docker-composes:

1) docker-compose.yml is a basic file.

2) docker-compose.override.yml is a default overrider of basic file. When it exists and you run 
docker-compose up,
docker actually runs like this:
docker-compose -f docker-compose.yml -f docker-compose.override.yml up.

3) docker-compose.prod.yml is a prod overrider. It should be ran as
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up.

So, they both override basic docker-compose.yml.