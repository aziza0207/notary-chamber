import json

from django.apps import apps


def make_creation_args(parameters):
    parameters = json.loads(parameters)
    parent_model_name = parameters.get('parent_model_name')
    parent_instance_id = parameters.get('parent_instance_id')
    inline_model_name = parameters.get('inline_model_name').capitalize()

    inline_model_class = apps.get_model('content', inline_model_name)
    parent_model_pk = parent_model_name.lower() + '_id'
    create_args = {
        parent_model_pk: parent_instance_id
    }
    return inline_model_class, create_args
