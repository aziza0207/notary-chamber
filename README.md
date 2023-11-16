About docker-composes:

1) docker-compose.yml is a basic file.

2) docker-compose.override.yml is a default overrider of basic file. When it exists and you run 
docker-compose up,
docker actually runs like this:
docker-compose -f docker-compose.yml -f docker-compose.override.yml up.

3) docker-compose.prod.yml is a prod overrider. It should be ran as
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up.

So, they both override basic docker-compose.yml.

###

Regarding the multi-upload button in the admin panel:

The multi_upload_button.html is included in edit_inline/stacked_with_multi.html, which overrides edit_inline/stacked.html. It includes a JavaScript script that manages both 1) multiple input and 2) additional context for creating instances on the Django server side. This context is written by the overridden change_view method in AdminMultiInputMixin in mixins.py.

The current solution was accepted for the following reasons:

As the button is included in the existing HTML and appears inside the <form> tag, it is not feasible to wrap the button in another <form> tag. Consequently, the process of sending files to the backend is managed by JavaScript. Given that there are at least two similar models that require this functionality, the inclusion of additional context becomes necessary.
