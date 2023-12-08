from modeltranslation.translator import TranslationOptions, register

from .models import CenterInfo, CenterTask, Discipline, EducationalMaterial, ManagerProfile, StudyPlan, TeachingStaff


@register(EducationalMaterial)
class EducationalMaterialTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(TeachingStaff)
class TeachingStaffTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position',)


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
class DisciplineTranslationOptions(TranslationOptions):
    fields = ('name', 'content',)
