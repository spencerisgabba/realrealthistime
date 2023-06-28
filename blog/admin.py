from django.contrib import admin

from .models import Category,Tag,Post

@admin.register(Category)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class GradeAdmin(admin.ModelAdmin):
    pass
