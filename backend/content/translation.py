from modeltranslation.translator import TranslationOptions, register

from content.models import FAQ, Document, Link, News, PhotoSet, Video, NotaryChamberDepartment, NotaryWorker


@register(NotaryChamberDepartment)
class NotaryChamberDepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(NotaryWorker)
class NotaryWorkerTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position',)


@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ('title', 'file',)


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


@register(PhotoSet)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Link)
class LinkTranslationOptions(TranslationOptions):
    fields = ('name',)
