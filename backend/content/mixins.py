from django.urls import reverse
from django.utils.safestring import mark_safe


class AdminFieldMixin:
    def get_little_image(self, object):
        try:
            return mark_safe(f"<img src='{object.main_image.url}' width=50>")
        except AttributeError:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
        except ValueError:
            return None

    get_little_image.short_description = ""


class AdminMultiInputMixin:
    def change_view(self, request, object_id, form_url="", extra_context=None):
        '''
        The function generates additional context required in the view for creating multiple inline objects.
        Works in tandem with an overridden template in the inline class featuring a 'load multiple' button.

        Additionally, it forcefully adds the '_continue' option to optimize redirect behavior.
        '''

        request.POST._mutable = True
        request.POST['_continue'] = True
        request.POST._mutable = False

        extra_context = extra_context or {}
        extra_context.update({
            'parent_model_name': self.__dict__.get('model').__name__,
            'parent_instance_id': object_id,
            'inline_model_name': self.inlines[0].model._meta.model_name,
            'upload_url': request.build_absolute_uri(reverse('content:upload_photo'))
        })

        return super().change_view(request, object_id, form_url, extra_context=extra_context)
