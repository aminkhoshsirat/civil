from django.contrib import admin
from .models import UserProject, UserProjectImage, UserCoworking, UserCoworkingImage, UserCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

    def delete_queryset(self, request, queryset):
        for category in queryset:
            category.delete()



class ProjectImageInline(admin.TabularInline):
    model = UserProjectImage
    extra = 1

@admin.register(UserProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption')

@admin.register(UserProject)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    inlines = [ProjectImageInline]



class CoworkImageInline(admin.TabularInline):
    model = UserCoworkingImage
    extra = 1

@admin.register(UserCoworkingImage)
class CoworkingImageAdmin(admin.ModelAdmin):
    list_display = ('coworking', 'caption')

@admin.register(UserCoworking)
class CoworkingAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    inlines = [CoworkImageInline]

admin.site.register(UserCategory, CategoryAdmin)