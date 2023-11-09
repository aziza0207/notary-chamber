from django.utils.safestring import mark_safe


class AdminFieldMixin:
    def get_little_image(self, object):
            try:
                return mark_safe(f"<img src='{object.main_image.url}' width=50>")
            except AttributeError:
                return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_little_image.short_description = ""


class AdminMultiInputMixin:
    def add_multiadd_button(self, object):
        return mark_safe(f'<input type="file" name="images-1-image" accept="image/*" id="id_images-1-image" multiple>')

    add_multiadd_button.short_description = 'Загрузить несколько'
