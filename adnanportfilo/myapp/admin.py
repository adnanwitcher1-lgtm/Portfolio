from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'created_at', 'is_featured')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('is_featured',)
    
admin.site.register(Project, ProjectAdmin)