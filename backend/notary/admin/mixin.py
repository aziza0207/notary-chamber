from django.utils.safestring import mark_safe


class AdminFieldMixin:
    def get_little_photo(self, object):
            try:
                return mark_safe(f"<img src='{object.photo.url}' width=50>")
            except ValueError:
                return None
            except AttributeError:
                return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_little_photo.short_description = ""

