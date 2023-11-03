from modeltranslation.translator import TranslationOptions, register

from content.models import FAQ, Category, Document, Link, News, Photo, Video


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


@register(Photo)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Link)
class LinkTranslationOptions(TranslationOptions):
    fields = ('name',)
