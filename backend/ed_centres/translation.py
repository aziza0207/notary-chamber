from modeltranslation.translator import TranslationOptions, register

from .models import CenterInfo, CenterTask, ManagerProfile, StudyPlan, Discipline, TeachingStaff, EducationalMaterial


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
