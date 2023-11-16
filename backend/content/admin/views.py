from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .services import make_creation_args


@csrf_exempt
def upload_photo(request):
    '''
    The function processes POST requests from admin inline models containing multiple files
    in request.FILES. The request.FILES also includes a collection named 'json_data' representing
    the parameters necessary for object creation.
    '''
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        parameters_str = request.FILES.get('json_data').read().decode()
        inline_model_class, create_args = make_creation_args(parameters_str)
        for file in files:
            try:
                inline_model_class.objects.create(image=file, **create_args)
            except Exception:
                return HttpResponse('An error occured while saving files', status=500)
        return HttpResponse('Uploaded successfully', status=201)
    return HttpResponse('Method not allowed', status=405)
