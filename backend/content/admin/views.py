from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .services import make_creation_args


@csrf_exempt
def upload_photo(request):
    '''
    The function processes POST requests from admin inline models containing multiple files
    in request.FILES. The request.FILES also includes a collection named 'json_data' representing
    the parameters necessary for object creation.
    '''
    if request.method == 'POST':
        files = request.FILES.getlist('images')
        # parameters_str = request.FILES.get('json_data').read().decode()
        # inline_model_class, create_args = make_creation_args(parameters_str)
        referer_url = request.META.get('HTTP_REFERER')
        create_args = {
            
        }
        count = 0
        for file in files:
            try:
                # inline_model_class.objects.create(image=file, **create_args)
                count += 1
            except Exception:
                messages.error(request, f'При загрузке изображения {file.name} произошла ошибка')
        messages.info(request, f'Загружено {count} изображений из {len(files)}')
        return HttpResponseRedirect(referer_url)
    return HttpResponse('Method not allowed', status=405)
