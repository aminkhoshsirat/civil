from django.contrib import admin
from .models import HomeProject, HomeProjectImage, HomeCoworking, HomeCoworkingImage, HomeCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

    def delete_queryset(self, request, queryset):
        for category in queryset:
            category.delete()



class ProjectImageInline(admin.TabularInline):
    model = HomeProjectImage
    extra = 1

@admin.register(HomeProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption')

@admin.register(HomeProject)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    inlines = [ProjectImageInline]



class CoworkImageInline(admin.TabularInline):
    model = HomeCoworkingImage
    extra = 1

@admin.register(HomeCoworkingImage)
class CoworkingImageAdmin(admin.ModelAdmin):
    list_display = ('coworking', 'caption')

@admin.register(HomeCoworking)
class CoworkingAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    inlines = [CoworkImageInline]

admin.site.register(HomeCategory, CategoryAdmin)