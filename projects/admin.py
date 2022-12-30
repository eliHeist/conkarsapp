from django.contrib import admin

from images.models import Image
from projects.models import Category, Project

# Register your models here.
class InlineImage(admin.StackedInline):
    model = Image
    extra = 1
    show_change_link = True
    can_delete = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

admin.site.register(Category)