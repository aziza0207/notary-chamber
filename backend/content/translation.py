from modeltranslation.translator import register, TranslationOptions

from content.models import Category, Document, FAQ, Photo, Video, News, Link


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
