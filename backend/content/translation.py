from modeltranslation.translator import TranslationOptions, register

from content.models import (FAQ, Link, News, PhotoSet, Video, Aphorism, CenterInfo, CenterTask, ManagerProfile,
                            StudyPlan, Discipline, TeachingStaff, EducationalMaterial)


@register(EducationalMaterial)
class EducationalMaterialTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(TeachingStaff)
class TeachingStaffTranslationOptions(TranslationOptions):
    fields = ('full_name', 'office',)


@register(CenterInfo)
class CenterInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'thesis',)


@register(CenterTask)
class CenterTaskTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(ManagerProfile)
class MangerProfileTranslationOptions(TranslationOptions):
    fields = ('full_name', 'text',)


@register(StudyPlan)
class StudyPlanTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Discipline)
class MangerProfileTranslationOptions(TranslationOptions):
    fields = ('name', 'content',)


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


@register(Aphorism)
class AphorismTranslationOptions(TranslationOptions):
    fields = ('text',)
