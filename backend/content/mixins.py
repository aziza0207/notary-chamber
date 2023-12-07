from typing import Any

from django.utils.datastructures import MultiValueDict
from django.utils.safestring import mark_safe


class AdminFieldMixin:
    def get_little_image(self, object):
        try:
            return mark_safe(f"<img src='{object.main_image.url}' width=50>") if object.main_image else '-'
        except AttributeError:
            return mark_safe(f"<img src='{object.image.url}' width=50>") if object.image else '-'
        except ValueError:
            return None

    get_little_image.short_description = ""


class AdminMultiInputMixin:
    '''
    The mixin overrides certain admin methods to facilitate additional handling of image multi-input.
    It collaborates seamlessly with the stacked_with_multi.html and tabular_with_multi.html templates.
    '''

    def save_formset(self, request: Any, form: Any, formset: Any, change: Any) -> None:
        '''
        The function invokes the standard save_formset() method, and subsequently iterates through the provided
        list of images, saving each of them into the database.
        '''
        
        response = super().save_formset(request, form, formset, change)
        if isinstance(formset.files, MultiValueDict):
            images = formset.files.getlist('images')
            creation_args = {
                f'{form.instance._meta.model_name}_{form.instance._meta.pk.name}': form.instance.id
            }
            for image in images:
                object = formset.model.objects.create(image=image, **creation_args)
                object.save()
        return response
