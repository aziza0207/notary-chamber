from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline, TranslationTabularInline

from ..mixins import AdminFieldMixin
from ..models import CenterInfo, CenterTask, ManagerProfile, StudyPlan, Discipline, TeachingStaff, EducationalMaterial


@admin.register(CenterInfo)
class CenterInfoAdmin(AdminFieldMixin, TabbedTranslationAdmin):
    list_display = ['id', 'title', 'get_little_image',]
    list_display_links = ['title']
    
    readonly_fields = ['get_little_image',]
    fields = ['title', 'description', 'thesis', ('image', 'get_little_image',),]
    search_fields = ['title',]

@admin.register(CenterTask)
class CenterTaskAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'get_small_text',)
    list_display_links = ('get_small_text',)

    def get_small_text(self, object):
        return f'{object.text[:67]}...' if len(object.text) > 70 else object.text

    get_small_text.short_description = ""


@admin.register(ManagerProfile)
class ManagerProfileAdmin(AdminFieldMixin, TabbedTranslationAdmin):
    list_display = ('id', 'full_name', 'get_little_image',)
    list_display_links = ('full_name',)
    
    readonly_fields = ['get_little_image',]
    fields = ['full_name', 'text', ('image', 'get_little_image',),]


class DisciplineInline(TranslationStackedInline):
    extra = 0
    model = Discipline


@admin.register(StudyPlan)
class StudyPlanAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    inlines = (DisciplineInline,)


@admin.register(TeachingStaff)
class TeachingStaffAdmin(AdminFieldMixin, TabbedTranslationAdmin):
    list_display = ('id', 'full_name', 'office', 'email', 'get_little_image',)
    list_display_links = ('full_name',)
    
    readonly_fields = ['get_little_image',]
    fields = ['full_name', 'office', 'email', ('image', 'get_little_image',),]


@admin.register(EducationalMaterial)
class EducationalMaterialAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'url',)
    list_display_links = ('title',)
